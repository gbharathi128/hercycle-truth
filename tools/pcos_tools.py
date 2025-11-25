import os
from dotenv import load_dotenv
import google.generativeai as genai

load_dotenv()  # loads GEMINI_API_KEY

genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

def gemini_agent(message):
    """
    Sends the user's message to Gemini and returns the AI's reply.
    """

    model = genai.GenerativeModel("gemini-1.5-flash")

    response = model.generate_content(
        [
            {
                "role": "system",
                "parts": [
                    "You are HerCycle — a friendly, empathetic PCOS assistant.",
                    "Answer clearly, simply, and supportively.",
                    "Avoid strict medical advice; give general guidance only.",
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
    except:
        return str(response)
