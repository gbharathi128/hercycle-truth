import os
import google.generativeai as genai
from dotenv import load_dotenv
import streamlit as st

load_dotenv()

# GEMINI API key (works locally and on Streamlit Cloud)
API_KEY = os.getenv("GEMINI_API_KEY") or st.secrets["GEMINI"]["GEMINI_API_KEY"]
genai.configure(api_key=API_KEY)

def gemini_agent(message: str) -> str:
    """
    Sends the user's message to Gemini and returns the AI's reply.
    """
    model = genai.GenerativeModel("text-bison-001")  # safe model

    # Old-style syntax (positional list)
    response = model.generate_content(
        [
            {
                "role": "system",
                "parts": [
                    "You are HerCycle — a friendly, empathetic PCOS assistant.",
                    "Answer clearly, simply, and supportively.",
                    "Avoid strict medical advice."
                ]
            },
            {
                "role": "user",
                "parts": [message]
            }
        ]
    )

    try:
        return response.text
    except Exception as e:
        return f"Sorry, something went wrong: {e}"
