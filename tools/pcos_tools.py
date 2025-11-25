import os
import google.generativeai as genai
from dotenv import load_dotenv
import streamlit as st

# Load .env locally
load_dotenv()

# GEMINI API key (works on local and Streamlit Cloud secrets)
API_KEY = os.getenv("GEMINI_API_KEY") or st.secrets["GEMINI"]["GEMINI_API_KEY"]
genai.configure(api_key=API_KEY)

def gemini_agent(message: str) -> str:
    """
    Sends the user's message to Gemini and returns the AI's reply.
    """
    model = genai.GenerativeModel("text-bison-001")  # safe model

    response = model.generate_content(
        input=[
            {"role": "system", "content": (
                "You are HerCycle — a friendly, empathetic PCOS assistant. "
                "Answer clearly, simply, and supportively. "
                "Avoid strict medical advice."
            )},
            {"role": "user", "content": message}
        ]
    )

    try:
        return response.text
    except Exception as e:
        return f"Sorry, something went wrong: {e}"
