import streamlit as st
import google.generativeai as genai

# Load GEMINI API key from Streamlit Secrets
API_KEY = st.secrets["GEMINI"]["GEMINI_API_KEY"]
genai.configure(api_key=API_KEY)

def gemini_agent(message: str) -> str:
    """
    Sends the user's message to Gemini and returns the AI's reply.
    Uses a safe model to avoid NotFound errors.
    """
    model = genai.GenerativeModel("models/text-bison-001")  # safest model

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
