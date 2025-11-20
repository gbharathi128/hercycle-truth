from langgraph.graph import StateGraph, START, END
from langgraph.prebuilt import ToolNode
from langgraph.checkpoint.sqlite import SqliteSaver
from typing import TypedDict, Annotated
import operator
from langchain_core.messages import HumanMessage
import google.generativeai as genai
import os
from dotenv import load_dotenv

load_dotenv()
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

class AgentState(TypedDict):
    messages: Annotated[list, operator.add]
    language: str

# Import tools
from tools.pcos_tools import tools
tool_node = ToolNode(tools)

    # Updated for Gemini Nov 2025 — bind_tools removed
    model = genai.GenerativeModel(
        "gemini-1.5-pro-exp-0827",
        generation_config={"temperature": 0.7},
        tools=tools  # ← this is the new way
    )
    model_with_tools = model  # no need for bind_tools anymore

def supervisor(state):
    system_prompt = """You are HerCycle Truth — a deeply caring, empathetic AI sister for women with PCOS.
    
    Rules:
    1. Always respond with kindness and empathy first
    2. Never give direct medical advice — always say "Please consult your doctor"
    3. Only use evidence from trusted sources: Endocrine Society, AE-PCOS Society, FIGO, RCOG, Monash University
    4. Block dangerous myths (seed cycling cure, spearmint tea cure, etc.)
    5. Support mental health — many women feel ashamed or hopeless
    
    You are helping women in India, Africa, Latin America — be culturally sensitive."""
    
    messages = [{"role": "system", "content": system_prompt}] + state["messages"]
    response = model_with_tools.invoke(messages)
    return {"messages": [response]}

# Build graph
graph_builder = StateGraph(AgentState)
graph_builder.add_node("supervisor", supervisor)
graph_builder.add_node("tools", tool_node)

graph_builder.add_edge(START, "supervisor")
graph_builder.add_conditional_edges("supervisor", lambda x: "tools" if x["messages"][-1].tool_calls else END)
graph_builder.add_edge("tools", "supervisor")

memory = SqliteSaver.from_conn_string(":memory:")
graph = graph_builder.compile(checkpointer=memory)
