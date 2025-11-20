import os
from dotenv import load_dotenv
from typing import TypedDict, Annotated
import operator

from langgraph.graph import StateGraph, START, END
from langgraph.prebuilt import ToolNode
from langgraph.checkpoint.sqlite import SqliteSaver

import google.generativeai as genai
from tools.pcos_tools import tools

# Load environment variables (for local testing)
load_dotenv()

# Configure Gemini API key from Streamlit secrets or .env
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

# Define state
class AgentState(TypedDict):
    messages: Annotated[list, operator.add]
    language: str

# Create tool node
tool_node = ToolNode(tools)

# Updated Gemini model with correct tool binding (Nov 2025)
model = genai.GenerativeModel(
    "gemini-1.5-pro-exp-0827",
    generation_config={"temperature": 0.7},
    tools=tools  # This is the correct way now
)
model_with_tools = model  # Same object

# Supervisor agent — the caring heart of HerCycle Truth
def supervisor(state):
    system_prompt = """You are HerCycle Truth ♀️ — a deeply caring, empathetic AI sister for women with PCOS.

    Core Rules:
    - Always start with empathy and kindness
    - Never give direct medical advice — always say "Please consult your doctor"
    - Only use evidence from trusted sources: Endocrine Society, AE-PCOS Society, FIGO, RCOG, Monash University, WHO
    - Debunk myths firmly but gently (e.g., seed cycling, spearmint tea cure, inositol-only cure)
    - Be culturally sensitive — many women in India, Africa, and Latin America are reading this
    - Support mental health: many feel shame, fear, or hopelessness

    You are hope in the dark for millions of sisters."""

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
    lambda x: "tools" if x["messages"][-1].tool_calls else END
)
graph_builder.add_edge("tools", "supervisor")

# Use in-memory checkpoint for sessions
memory = SqliteSaver.from_conn_string(":memory:")
graph = graph_builder.compile(checkpointer=memory)
