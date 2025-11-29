import os
import streamlit as st
import google.generativeai as genai
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Get API key from .env or Streamlit secrets (cloud safe)
try:
    API_KEY = st.secrets["GEMINI"]["GEMINI_API_KEY"]
except KeyError:
    API_KEY = os.getenv("GEMINI_API_KEY")

if not API_KEY:
    raise ValueError("❌ GEMINI_API_KEY missing! Add it to .env")

# Configure Gemini
genai.configure(api_key=API_KEY)

# System Instructions
SYSTEM_PROMPT = """
You are HerCycle 💗 — a soft, supportive PCOS companion.
Be caring, emotional, human-like, and compassionate.
Give lifestyle guidance like diet, exercise, motivation, myths, symptoms.
Never give medical prescriptions or drugs.
Talk like a supportive elder sister.
"""

def gemini_agent(message: str) -> str:
    """Send message to Gemini and return friendly reply"""
    model = genai.GenerativeModel("models/gemini-2.5-flash")

    try:
        response = model.generate_content(
            [
                {"role": "system", "parts": [SYSTEM_PROMPT]},
                {"role": "user", "parts": [message]},
            ]
        )
        return response.text

    except Exception as e:
        print("DEBUG ERROR:", e)
        return "Oops babe… something went wrong 💛 Try again?"
