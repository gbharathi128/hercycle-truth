import os
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("GEMINI_API_KEY")
genai.configure(api_key=API_KEY)

def gemini_agent(message: str) -> str:
    """
    Sends the user's message to Gemini and returns the AI's reply.
    """

    model_name = "models/gemini-2.5-flash"
    model = genai.GenerativeModel(model_name)

    system_prompt = (
        "You are HerCycle — a friendly, empathetic, and knowledgeable PCOS assistant. "
        "Answer questions clearly and accurately. "
        "Provide general guidance, lifestyle tips, diet help, exercises and motivation. "
        "Avoid strict medical or prescription advice. "
        "Use soft language and be very supportive."
    )

    try:
        response = model.generate_content(
            [
                {"role": "system", "parts": [system_prompt]},
                {"role": "user", "parts": [message]},
            ]
        )
        return response.text

    except Exception as e:
        return f"Oops babe… something went wrong 💛 Try again?\n\nError: {str(e)}"
