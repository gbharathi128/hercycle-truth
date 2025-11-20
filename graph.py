# graph.py
import os
from dotenv import load_dotenv
load_dotenv()

# Try to import Gemini SDK
try:
    import google.generativeai as genai
    GEMINI_AVAILABLE = True
except Exception:
    GEMINI_AVAILABLE = False

from tools.pcos_tools import pcos_search, myth_checker, symptom_explain

GEMINI_KEY = os.getenv("GEMINI_API_KEY")
USE_GEMINI = bool(GEMINI_KEY and GEMINI_AVAILABLE)

if USE_GEMINI:
    genai.configure(api_key=GEMINI_KEY)
    model = genai.GenerativeModel(model_name="models/gemini-1.5-pro",
                                 generation_config={"temperature": 0.6})
else:
    model = None

def local_responder(user_text: str) -> str:
    txt = user_text.strip().lower()
    if "diet" in txt or "weekly" in txt:
        return "You can generate a weekly diet plan from the Diet tab. Choose your preference (veg/vegan/non-veg) and goal."
    if "seed cycling" in txt or "spearmint" in txt or "cure" in txt:
        return myth_checker(user_text)
    if any(k in txt for k in ["symptom", "hair", "acne", "irregular", "period"]):
        return pcos_search(user_text)
    return ("Hi—I'm HerCycle Truth. I can explain PCOS symptoms, generate diet plans, and check myths. "
            "Try: 'Give me a weekly diet plan' or 'Does seed cycling cure PCOS?'")

def invoke(payload: dict):
    messages = payload.get("messages", [])
    if not messages:
        return {"messages":[{"role":"assistant","content":"No input provided."}]}
    user_text = messages[-1].get("content","")
    if USE_GEMINI and model is not None:
        try:
            # simple chat with system prompt
            history = [{"role":"system","content":"You are HerCycle Truth — empathetic, never give medical advice."}] + messages
            gem_history = [{"role":m.get("role","user"), "parts":[{"text": m.get("content","")}]} for m in history]
            chat = model.start_chat(history=gem_history)
            resp = chat.send_message("")  # let model respond to history
            return {"messages":[resp]}
        except Exception as e:
            return {"messages":[{"role":"assistant","content":f"[Gemini error, fallback] {local_responder(user_text)}"}]}
    else:
        return {"messages":[{"role":"assistant","content": local_responder(user_text)}]}
