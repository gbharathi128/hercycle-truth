import os
import operator
import inspect
from typing import TypedDict, Annotated

import google.generativeai as genai
from dotenv import load_dotenv

from langgraph.graph import StateGraph, START, END
from langgraph.checkpoint.memory import MemorySaver  # ✅ New correct import

from tools.pcos_tools import pcos_search, myth_checker, symptom_explain


# -----------------------------
# ENV + GEMINI SETUP
# -----------------------------

load_dotenv()
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))


# -----------------------------
# TOOL → GEMINI SCHEMA BUILDER
# -----------------------------

TOOLS = [pcos_search, myth_checker, symptom_explain]


def to_schema(fn):
    """Convert python function → Gemini function-call schema."""
    sig = inspect.signature(fn)
    props = {}
    required = []

    for name in sig.parameters:
        props[name] = {"type": "string"}
        required.append(name)

    return {
        "name": fn.__name__,
        "description": fn.__doc__ or "",
        "input_schema": {
            "type": "object",
            "properties": props,
            "required": required
        }
    }


gemini_tools = [to_schema(fn) for fn in TOOLS]


# -----------------------------
# GEMINI MODEL
# -----------------------------

model = genai.GenerativeModel(
    model_name="models/gemini-1.5-pro",
    tools=gemini_tools,
    generation_config={"temperature": 0.6}
)


# -----------------------------
# UTILITY
# -----------------------------

def convert_to_gemini(messages):
    """Convert normal messages → Gemini parts format."""
    out = []
    for m in messages:
        out.append({
            "role": m["role"],
            "parts": [{"text": m["content"]}]
        })
    return out


def detect_tool_call(resp):
    """Check if Gemini wants to call a tool."""
    try:
        parts = resp.candidates[0].content.parts
        return any(hasattr(p, "function_call") for p in parts)
    except:
        return False


# -----------------------------
# GRAPH NODES
# -----------------------------

def supervisor(state):
    system_prompt = """
You are HerCycle Truth — a kind, supportive AI sister for women with PCOS.

Guidelines:
- Always be empathetic
- Never give medical advice
- Cite trusted bodies: WHO, FIGO, AE-PCOS, RCOG
- Fight misinformation gently
- Use tools when needed
"""

    msgs = [{"role": "system", "content": system_prompt}] + state["messages"]

    history = convert_to_gemini(msgs)

    chat = model.start_chat(history=history)
    result = chat.send_message("")

    return {"messages": [result]}


def tool_executor(state):
    """Execute Gemini function call."""
    last = state["messages"][-1]
    parts = last.candidates[0].content.parts

    for p in parts:
        if hasattr(p, "function_call"):
            fn_name = p.function_call.name
            args = p.function_call.args

            fn = next(f for f in TOOLS if f.__name__ == fn_name)
            output = fn(**args)

            return {
                "messages": [{"role": "tool", "content": str(output)}]
            }

    return {"messages": []}


# -----------------------------
# STATE
# -----------------------------

class AgentState(TypedDict):
    messages: Annotated[list, operator.add]


# -----------------------------
# BUILD GRAPH
# -----------------------------

graph_builder = StateGraph(AgentState)

graph_builder.add_node("supervisor", supervisor)
graph_builder.add_node("tools", tool_executor)

graph_builder.add_edge(START, "supervisor")

graph_builder.add_conditional_edges(
    "supervisor",
    lambda s: "tools" if detect_tool_call(s["messages"][-1]) else END
)

graph_builder.add_edge("tools", "supervisor")

# ✅ New recommended checkpointer for Streamlit + LangGraph
memory = MemorySaver()

graph = graph_builder.compile(checkpointer=memory)
