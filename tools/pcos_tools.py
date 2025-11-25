import google.generativeai as genai
import os

# ---------------------------------------------------
# INITIALIZE GEMINI API CORRECTLY (IMPORTANT)
# ---------------------------------------------------
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

# -------------------------------------------
# PCOS AGENT — BASE LOGIC
# -------------------------------------------

SYSTEM_INSTRUCTIONS = """
You are HerCycle Truth — an emotionally supportive AI sister for women with PCOS.

Rules you MUST follow:
• Be warm, kind and non-judgmental.
• Never give medical advice or prescriptions.
• You may give lifestyle guidance like diet, self-care, sleep, exercise, yoga.
• You may debunk myths gently.
• Encourage the user emotionally.
• Use simple, soft language (girly aesthetic tone).
"""

def format_reply(text: str) -> str:
    """Make responses softer, more aesthetic."""
    return text.replace("PCOS", "PCOS 💗")

# -------------------------------------------
# AGENT TOOL (CALLED BY STREAMLIT CHAT PAGE)
# -------------------------------------------

def ask_agent(user_input: str) -> str:
    """
    Main function the chat page calls.
    Sends user question → Gemini → returns soft reply.
    """

    try:
        model = genai.GenerativeModel(
            model_name="models/gemini-1.5-pro",
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
        return "Oops sweet girl… something went wrong. Try again? 💛"

# -------------------------------------------
# OPTIONAL TOOLS
# -------------------------------------------

def pcos_search(query: str):
    return f"Here’s what I found about: {query}. (Soft explanation coming soon 💗)"

def myth_checker(statement: str):
    if "cure" in statement.lower():
        return "Baby, PCOS cannot be cured — but it can be beautifully managed 💗"
    return "Let me explain this softly for you… 💗"

def symptom_explain(symptom: str):
    return f"Feeling {symptom}? Let me tell you what it usually means, softly… 💗"
