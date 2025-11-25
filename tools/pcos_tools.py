import os
import streamlit as st
import google.generativeai as genai
from dotenv import load_dotenv

# Load local .env (for local testing)
load_dotenv()

# Load GEMINI_API_KEY from Streamlit Secrets or environment variable
try:
    API_KEY = st.secrets["GEMINI"]["GEMINI_API_KEY"]
except KeyError:
    API_KEY = os.getenv("GEMINI_API_KEY")

if not API_KEY:
    raise ValueError(
        "GEMINI_API_KEY not found! Set it in .env (local) or Streamlit Secrets (cloud)."
    )

genai.configure(api_key=API_KEY)


def gemini_agent(message: str) -> str:
    """
    Sends the user's message to Gemini and returns the AI's reply.
    Uses fallback if PermissionDenied occurs.
    """
    # Use the most likely accessible model; you can replace with your available model
    model_name = "models/gemini-2.5-flash"

    model = genai.GenerativeModel(model_name)

    # Optimized system prompt for accurate PCOS answers
    system_prompt = (
        "You are HerCycle — a friendly, empathetic, and knowledgeable PCOS assistant. "
        "Answer questions clearly and accurately. "
        "Provide general guidance, tips for lifestyle, diet, and exercises. "
        "Avoid strict medical advice. "
        "Use simple, easy-to-understand language and be supportive."
    )

    try:
        response = model.generate_content(
            [
                {"role": "system", "parts": [system_prompt]},
                {"role": "user", "parts": [message]},
            ]
        )
        return response.text
    except genai.error.PermissionError:
        return (
            "Sorry, this AI model cannot be accessed with your API key. "
            "Please check your API permissions."
        )
    except Exception as e
