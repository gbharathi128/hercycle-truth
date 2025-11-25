import os
from dotenv import load_dotenv
import google.generativeai as genai

# Load .env file
load_dotenv()

# Configure Gemini API Key
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

SYSTEM_INSTRUCTIONS = """
You are HerCycle Truth — an emotionally supportive AI sister for women with PCOS.

Rules:
• Be warm, kind and non-judgmental.
• Never give medical advice or prescribe medicines.
• You may give lifestyle guidance (diet, yoga, sleep, habits).
• You may debunk myths softly.
• Encourage and support the user emotionally.
• Use soft, girly, comforting language.
"""

def format_reply(text: str) -> str:
    return text.replace("PCOS", "PCOS 💗")

def ask_agent(user_input: str) -> str:
    """Main chat logic"""

    try:
        model = genai.GenerativeModel(
            model_name="gemini-1.5-pro",
            generation_config={"temperature": 0.7}
        )

        response = model.generate_content(
            [
                {"role": "system", "parts": [SYSTEM_INSTRUCTIONS]},
                {"role": "user", "parts": [user_input]},
            ]
        )

        reply = response.text
        return format_reply(reply)

    except Exception as e:
        print("ERROR:", e)
        return "Oops sweet girl… something went wrong. Try again? 💛"

# Optional small tools
def pcos_search(query: str):
    return f"Here’s what I found about {query} 💗 (More info coming soon!)"

def myth_checker(statement: str):
    if "cure" in statement.lower():
        return "Baby, PCOS cannot be cured — but it can be managed beautifully 💗"
    return "Let me explain that softly for you… 💗"

def symptom_explain(symptom: str):
    return f"Feeling {symptom}? Here’s what it usually means, softly… 💗"
