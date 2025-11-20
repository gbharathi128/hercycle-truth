import os
from dotenv import load_dotenv
from typing import TypedDict, Annotated
import operator

from langgraph.graph import StateGraph, START, END
from langgraph.prebuilt import ToolNode
from langgraph.checkpoint.sqlite import SqliteSaver

import google.generativeai as genai
from tools.pcos_tools import tools

# Load env (local + Streamlit secrets)
load_dotenv()
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

class AgentState(TypedDict):
    messages: Annotated[list, operator.add]
    language: str

# Tool node
tool_node = ToolNode(tools)

# CORRECT Gemini 1.5 Pro tool binding (Nov 2025)
model = genai.GenerativeModel(
    "gemini-1.5-pro-exp-0827",
    generation_config={"temperature": 0.7},
    tools=tools
)
model_with_tools = model  # No bind_tools needed anymore

def supervisor(state):
    system_prompt = """You are HerCycle Truth ♀️ — a deeply caring, empathetic AI sister for women with PCOS.

Core Rules:
- Always start with empathy and kindness
- Never give direct medical advice — always say "Please consult your doctor"
- Only cite trusted sources: Endocrine Society, AE-PCOS Society, FIGO, RCOG, Monash University, WHO
- Gently debunk myths (seed cycling cure, spearmint tea cure, etc.)
- Be culturally sensitive — many users are from India, Africa, Latin America
- Support mental health — many women feel shame, fear, or hopelessness"""

    messages = [{"role": "system", "content": system_prompt}] + state["messages"]
    response = model_with_tools.invoke(messages)
    return {"messages": [response]}

# Build the graph
graph_builder = StateGraph(AgentState)
graph_builder.add_node("supervisor", supervisor)
graph_builder.add_node("tools", tool_node)

graph_builder.add_edge(START, "supervisor")
graph_builder.add_conditional_edges(
    "supervisor",
    lambda x: "tools" if hasattr(x["messages"][-1], "tool_calls") and x["messages"][-1].tool_calls else END
)
graph_builder.add_edge("tools", "supervisor")

# In-memory session persistence
memory = SqliteSaver.from_conn_string(":memory:")
graph = graph_builder.compile(checkpointer=memory)
