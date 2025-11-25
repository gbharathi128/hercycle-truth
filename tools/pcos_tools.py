import os
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

def gemini_agent(message):
    model = genai.GenerativeModel("gemini-1.5-pro")  # safer than flash

    response = model.generate_content(
        input=[
            {"role": "system", "content": (
                "You are HerCycle — a friendly, empathetic PCOS assistant. "
                "Answer clearly, simply, and supportively. Avoid strict medical advice."
            )},
            {"role": "user", "content": message}
        ]
    )

    return response.text
