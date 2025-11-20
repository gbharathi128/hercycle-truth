import os
import operator
import inspect
from typing import TypedDict, Annotated

import google.generativeai as genai
from dotenv import load_dotenv

from langgraph.graph import StateGraph, START, END
from langgraph.checkpoint.sqlite import SqliteSaver

from tools.pcos_tools import pcos_search, myth_checker, symptom_explain

load_dotenv()
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))


# -------------------
# TOOLS → Gemini Schema
# -------------------

TOOLS = [pcos_search, myth_checker, symptom_explain]

def to_schema(fn):
    sig = inspect.signature(fn)
    props, req = {}, []

    for name in sig.parameters:
        props[name] = {"type": "string"}
        req.append(name)

    return {
        "name": fn.__name__,
        "description": fn.__doc__,
        "input_schema": {"type": "object", "properties": props, "required": req}
    }


gemini_tools = [to_schema(fn) for fn in TOOLS]


model = genai.GenerativeModel(
    model_name="gemini-1.5-pro",
    tools=gemini_tools,
    generation_config={"temperature": 0.6}
)


# -------------------
# Utility
# -------------------

def convert(messages):
    gemini_msgs = []
    for m in messages:
        gemini_msgs.append({"role": m["role"], "parts": [{"text": m["content"]}]})
    return gemini_msgs


def detect_tool_call(response):
    try:
        parts = response.candidates[0].content.parts
        return any(getattr(p, "function_call", None) for p in parts)
    except:
        return False


# -------------------
# Agent Nodes
# -------------------

def supervisor(state):
    sys = """
You are HerCycle Truth — an emotionally supportive AI sister for women with PCOS.

Rules:
- Be empathetic
- Never give medical advice
- Cite trusted medical bodies
- Fight misinformation gently
- Use tools when needed
"""
    msgs = convert(
        [{"role": "system", "content": sys}] + state["messages"]
    )
    chat = model.start_chat(history=msgs)
    result = chat.send_message("")

    return {"messages": [result]}


def tool_executor(state):
    last = state["messages"][-1]
    parts = last.candidates[0].content.parts

    for p in parts:
        if hasattr(p, "function_call"):
            name = p.function_call.name
            args = p.function_call.args

            fn = next(f for f in TOOLS if f.__name__ == name)
            output = fn(**args)

            return {"messages": [{"role": "tool", "content": str(output)}]}

    return {"messages": []}


# -------------------
# State
# -------------------

class AgentState(TypedDict):
    messages: Annotated[list, operator.add]


# -------------------
# Build Graph
# -------------------

graph_builder = StateGraph(AgentState)

graph_builder.add_node("supervisor", supervisor)
graph_builder.add_node("tools", tool_executor)

graph_builder.add_edge(START, "supervisor")

graph_builder.add_conditional_edges(
    "supervisor",
    lambda s: "tools" if detect_tool_call(s["messages"][-1]) else END
)

graph_builder.add_edge("tools", "supervisor")

memory = SqliteSaver.from_conn_string(":memory:")

graph = graph_builder.compile(checkpointer=memory)
