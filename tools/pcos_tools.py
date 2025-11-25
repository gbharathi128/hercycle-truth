import os
import streamlit as st
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()
try:
    API_KEY = st.secrets["GEMINI"]["GEMINI_API_KEY"]
except KeyError:
    API_KEY = os.getenv("GEMINI_API_KEY")

if not API_KEY:
    raise ValueError("GEMINI_API_KEY not found!")

genai.configure(api_key=API_KEY)

def gemini_agent(message: str) -> str:
    model = genai.GenerativeModel("models/gemini-2.5-flash")  # Change to a valid model

    response = model.generate_content(
        [
            {"role": "system", "parts": [
                "You are HerCycle — a friendly, empathetic PCOS assistant.",
                "Answer clearly, simply, and supportively.",
                "Avoid strict medical advice."
            ]},
            {"role": "user", "parts": [message]}
        ]
    )

    try:
        return response.text
    except Exception as e:
        return f"Error: {e}"
