import os
import operator
import inspect
from typing import TypedDict, Annotated

import google.generativeai as genai
from dotenv import load_dotenv

from langgraph.graph import StateGraph, START, END
from langgraph.checkpoint.sqlite import SqliteSaver

# Import your tools
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
    """Convert a python function into Gemini function-call schema."""
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
    """Convert standard chat messages → Gemini's 'parts' format."""
    converted = []
    for msg in messages:
        converted.append({
            "role": msg["role"],
            "parts": [{"text": msg["content"]}]
        })
    return converted


def detect_tool_call(response):
    """Check if Gemini has issued a function_call instruction."""
    try:
        parts = response.candidates[0].content.parts
        return any(hasattr(p, "function_call") for p in parts)
    except:
        return False


# -----------------------------
# GRAPH NODES
# -----------------------------

def supervisor(state):
    """Main reasoning node — uses Gemini with instructions."""
    
    system_instruction = """
You are HerCycle Truth — an emotionally supportive AI sister for women with PCOS.

Rules:
- Always be empathetic & warm
- Never provide medical advice — say “Please consult your doctor”
- Cite trusted medical sources (AE-PCOS Society, FIGO, WHO, RCOG)
- Gently fight PCOS misinformation
- Use tools for search, myth checking, or symptom explanations
"""

    msgs = [{"role": "system", "content": system_instruction}] + state["messages"]

    # Convert to Gemini format
    gemini_history = convert_to_gemini(msgs)

    chat = model.start_chat(history=gemini_history)
    result = chat.send_message("")

    return {"messages": [result]}


def tool_executor(state):
    """Executes the tool that Gemini requested."""

    last_msg = state["messages"][-1]
    parts = last_msg.candidates[0].content.parts

    for part in parts:
        if hasattr(part, "function_call"):
            name = part.function_call.name
            args = part.function_call.args

            fn = next(f for f in TOOLS if f.__name__ == name)
            output = fn(**args)

            return {
                "messages": [
                    {"role": "tool", "content": str(output)}
                ]
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

# SQLite in-memory checkpoint (safe for Streamlit)
memory = SqliteSaver.from_conn_string(":memory:")

graph = graph_builder.compile(checkpointer=memory)
