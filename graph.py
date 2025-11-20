import os
import operator
import inspect
from typing import TypedDict, Annotated

import google.generativeai as genai
from dotenv import load_dotenv

from langgraph.graph import StateGraph, START, END

from tools.pcos_tools import pcos_search, myth_checker, symptom_explain

load_dotenv()
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

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

model = genai.Generat
