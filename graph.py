# graph.py
import os
import inspect
from typing import Any, Dict, List

from dotenv import load_dotenv

# Try to import Gemini SDK — used only if API key is present.
try:
    import google.generativeai as genai
    GEMINI_AVAILABLE = True
except Exception:
    GEMINI_AVAILABLE = False

# load env
load_dotenv()

from tools.pcos_tools import pcos_search, myth_checker, symptom_explain

TOOLS = {
    "pcos_search": pcos_search,
    "myth_checker": myth_checker,
    "symptom_explain": symptom_explain
}

# Build a simple local responder (fallback)
def local_responder(user_text: str) -> str:
    txt = user_text.strip().lower()
    if txt.endswith("?"):
        txt = txt[:-1].strip()
    # prioritize direct tool-like questions
    if txt.startswith("is") or "myth" in txt or "cure" in txt:
        return myth_checker(user_text)
    if any(k in txt for k in ["symptom", "symptoms", "hair loss", "irregular", "acne"]):
        return pcos_search(user_text)
    if any(k in txt for k in ["how", "what", "why", "can i", "do i"]):
        # general answer + invite to clarify
        return ("I can help explain PCOS symptoms, diet suggestions, and common myths. "
                "Tell me specifically: do you want a diet plan, a symptom explanation, or myth-check?")
    # default fallback
    return ("Hi — I'm HerCycle Truth. I can offer educational info (not medical advice). "
            "Try: 'What are PCOS symptoms?', 'Does seed cycling cure PCOS?', or 'Give me a weekly diet plan'.")

# If GEMINI_API_KEY present and SDK available, initialize model
GEMINI_KEY = os.getenv("GEMINI_API_KEY")
USE_GEMINI = bool(GEMINI_KEY and GEMINI_AVAILABLE)

if USE_GEMINI:
    genai.configure(api_key=GEMINI_KEY)
    # Create simple model; avoid tools function-declarations to keep safe
    model = genai.GenerativeModel(model_name="models/gemini-1.5-pro",
                                 generation_config={"temperature": 0.6})
else:
    model = None

def invoke(payload: Dict[str, Any]) -> Dict[str, Any]:
    """
    Maintain compatibility with previous app: graph.invoke({"messages":[{"role":"user","content": "..."}]})
    Returns dict {"messages": [message_dicts...]}
    message_dicts: if using Gemini, lower-level response object will be present.
    For fallback, we return simple dicts with 'role' and 'content' strings.
    """
    messages = payload.get("messages", [])
    if not messages:
        return {"messages": [{"role": "assistant", "content": "No input provided."}]}

    user_msg = messages[-1].get("content", "")
    if USE_GEMINI and model is not None:
        # Use a simple chat invocation
        try:
            history = [{"role": "system", "content": "You are HerCycle Truth — empathetic, never give medical advice."}] + messages
            # convert to Gemini parts format expected by SDK
            gemini_history = []
            for m in history:
                gemini_history.append({"role": m.get("role", "user"), "parts": [{"text": m.get("content","")} ] })
            chat = model.start_chat(history=gemini_history)
            resp = chat.send_message("")  # empty message to get completion based on history
            return {"messages": [resp]}
        except Exception as e:
            # fallback to local responder on any SDK/runtime error
            return {"messages": [{"role": "assistant", "content": f"[Gemini error, fallback] {local_responder(user_msg)}"}]}
    else:
        # Local fallback responder (guaranteed)
        text = local_responder(user_msg)
        return {"messages": [{"role": "assistant", "content": text}]}
