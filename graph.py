import os
import operator
import inspect
from typing import TypedDict, Annotated

from dotenv import load_dotenv
import google.generativeai as genai

from langgraph.graph import StateGraph, START, END
from langgraph.checkpoint.sqlite import SqliteSaver

# Load .env
load_dotenv()
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

# ------------------------------
# 1. IMPORT YOUR PYTHON TOOLS
# ------------------------------

from tools.pcos_tools import tools   # This must be a list of Python functions


# ------------------------------
# 2. CONVERT PYTHON FUNCTIONS → GEMINI TOOL SCHEMA
# ------------------------------

def python_to_schema(fn):
    """Convert a Python function signature → Gemini JSON schema."""
    sig = inspect.signature(fn)
    props = {}
    required = []

    for name, param in sig.parameters.items():
        props[name] = {"type": "string"}  # Simple mapping (all inputs as str)
        required.append(name)

    return {
        "type": "object",
        "properties": props,
        "required": required
    }


gemini_tools = []
for fn in tools:
    gemini_tools.append({
        "name": fn.__name__,
        "description": fn.__doc__ or "PCOS tool",
        "input_schema": python_to_schema(fn)
    })


# ------------------------------
# 3. INIT GEMINI MODEL
# ------------------------------

model = genai.GenerativeModel(
    model_name="gemini-1.5-pro",
    tools=gemini_tools,
    generation_config={"temperature": 0.7}
)


# ------------------------------
# 4. MESSAGE FORMATTER
# ------------------------------

def to_gemini_messages(messages):
    """Convert LangGraph-style messages → Gemini format."""
    out = []
    for m in messages:
        out.append({
            "role": m["role"],
            "parts": [{"text": m["content"]}]
        })
    return out


# ------------------------------
# 5. SUPERVISOR NODE
# ------------------------------

def supervisor(state):
    system_prompt = """
You are HerCycle Truth ♀️ — a deeply caring, empathetic AI sister for women with PCOS.

Core Rules:
- Always respond kindly and supportively.
- Never give direct medical advice — instead say “Please consult your doctor for medical guidance.”
- Debunk myths gently.
- Respect cultural contexts (India, Africa, Latin America).
- Always support emotional wellbeing.
    """

    # Convert everything to Gemini format
    msgs = to_gemini_messages(
        [{"role": "user", "content": system_prompt}] + state["messages"]
    )

    chat = model.start_chat(history=msgs)
    response = chat.send_message("")

    return {"messages": [response]}


# ------------------------------
# 6. TOOL CALL DETECTION
# ------------------------------

def has_tool_call(response):
    """Return True if Gemini triggered a tool."""
    try:
        parts = response.candidates[0].content.parts
        return any(getattr(p, "function_call", None) for p in parts)
    except:
        return False


# ------------------------------
# 7. TOOL EXECUTION NODE
# ------------------------------

def tool_executor(state):
    """Execute Python tool requested by Gemini."""
    resp = state["messages"][-1]
    parts = resp.candidates[0].content.parts

    for p in parts:
        if hasattr(p, "function_call"):
            fn_name = p.function_call.name
            args = p.function_call.args

            # Find matching Python function
            fn = next(f for f in tools if f.__name__ == fn_name)

            result = fn(**args)

            # Return as tool message
            return {
                "messages": [{
                    "role": "tool",
                    "content": str(result)
                }]
            }

    return {"messages": []}


# ------------------------------
# 8. LANGGRAPH STATE
# ------------------------------

class AgentState(TypedDict):
    messages: Annotated[list, operator.add]
    language: str


# ------------------------------
# 9. BUILD LANGGRAPH WORKFLOW
# ------------------------------

graph_builder = StateGraph(AgentState)

graph_builder.add_node("supervisor", supervisor)
graph_builder.add_node("tools", tool_executor)

graph_builder.add_edge(START, "supervisor")

graph_builder.add_conditional_edges(
    "supervisor",
    lambda s: "tools" if has_tool_call(s["messages"][-1]) else END
)

graph_builder.add_edge("tools", "supervisor")

# Memory
memory = SqliteSaver.from_conn_string(":memory:")

# FINAL GRAPH
graph = graph_builder.compile(checkpointer=memory)
