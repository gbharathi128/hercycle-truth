import os
import inspect
import operator
from typing import TypedDict, Annotated

from dotenv import load_dotenv
import google.generativeai as genai

from langgraph.graph import StateGraph, START, END
from langgraph.checkpoint.sqlite import SqliteSaver

# Load API key from .env
load_dotenv()
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

# ----------------------------
# TOOLS (your functions)
# ----------------------------
from tools.pcos_tools import pcos_search, myth_checker, symptom_explain

TOOLS = [pcos_search, myth_checker, symptom_explain]

def to_schema(fn):
    """Convert python tools into Gemini-compatible schema."""
    sig = inspect.signature(fn)
    props = {name: {"type": "string"} for name in sig.parameters}
    req = list(sig.parameters.keys())

    return {
        "name": fn.__name__,
        "description": fn.__doc__,
        "input_schema": {
            "type": "object",
            "properties": props,
            "required": req
        }
    }

gemini_tools = [to_schema(fn) for fn in TOOLS]

# ----------------------------
# Gemini Model
# ----------------------------
model = genai.GenerativeModel(
    model_name="models/gemini-1.5-pro",
    tools=gemini_tools,
    generation_config={"temperature": 0.6}
)

# ----------------------------
# Utility
# ----------------------------
def convert(messages):
    formatted = []
    for m in messages:
        formatted.append({"role": m["role"], "parts": [{"text": m["content"]}]})
    return formatted

def detect_tool_call(result):
    try:
        parts = result.candidates[0].content.parts
        return any(getattr(p, "function_call", None) for p in parts)
    except:
        return False

# ----------------------------
# Agent Nodes
# ----------------------------
def supervisor(state):
    system_prompt = """
You are HerCycle Truth — an emotionally supportive AI sister for women with PCOS.
Rules:
- Be empathetic
- Never give medical advice
- Cite trusted medical bodies gently
- Debunk myths kindly
- Use tools only when helpful
"""

    msgs = convert([{"role": "system", "content": system_prompt}] + state["messages"])

    chat = model.start_chat(history=msgs)
    result = chat.send_message("")

    return {"messages": [result]}

def tool_executor(state):
    last = state["messages"][-1]
    parts = last.candidates[0].content.parts

    for p in parts:
        if hasattr(p, "function_call"):
            fn_name = p.function_call.name
            args = p.function_call.args

            fn = next(f for f in TOOLS if f.__name__ == fn_name)
            output = fn(**args)

            return {"messages": [{"role": "tool", "content": str(output)}]}

    return {"messages": []}

# ----------------------------
# State Definition
# ----------------------------
class AgentState(TypedDict):
    messages: Annotated[list, operator.add]

# ----------------------------
# Build Graph
# ----------------------------
builder = StateGraph(AgentState)

builder.add_node("supervisor", supervisor)
builder.add_node("tools", tool_executor)

builder.add_edge(START, "supervisor")

builder.add_conditional_edges(
    "supervisor",
    lambda s: "tools" if detect_tool_call(s["messages"][-1]) else END
)

builder.add_edge("tools", "supervisor")

memory = SqliteSaver.from_conn_string(":memory:")

graph = builder.compile(checkpointer=memory)
