from google.adk.agents import Agent
import vertexai
import os

vertexai.init(
    project=os.environ["GOOGLE_CLOUD_PROJECT"],
    location=os.environ["GOOGLE_CLOUD_LOCATION"],
)

def get_pcos_diet(day: str) -> dict:
    """Tool for PCOS-friendly meal plans (low-GI, anti-inflammatory)."""
    plans = {
        "monday": {"status": "success", "report": "Breakfast: Oats + berries. Lunch: Grilled chicken + quinoa. Dinner: Salmon + sweet potato. (Consult doctor ♡)"},
        # Add more days...
    }
    city_lower = day.lower()
    if city_lower in plans:
        return plans[city_lower]
    return {"status": "error", "error_message": "Try Monday-Sunday for plans."}

def debunk_pcos_myth(myth: str) -> dict:
    """Tool to debunk common PCOS myths with evidence-based info."""
    myths = {
        "spearmint tea cure": {"status": "success", "report": "Limited evidence; not a cure. Source: Endocrine Society 2023. Consult doctor."},
        # Add more myths...
    }
    myth_lower = myth.lower()
    if myth_lower in myths:
        return myths[myth_lower]
    return {"status": "error", "error_message": "Myth not in database. Ask about spearmint tea or seed cycling."}

root_agent = Agent(
    name="hercycle_pcos_sister",
    model="gemini-1.5-pro",
    description="Empathetic PCOS support agent with diet, myth-debunking, and wellness tools.",
    instruction="""
    You are HerCycle — a caring AI sister for women with PCOS.
    Rules:
    1. Always respond with empathy first
    2. Never give direct medical advice — always say "Please consult your doctor ♡"
    3. Use tools for diet/myth queries
    4. Be culturally sensitive for global users
    5. Support mental health — acknowledge shame/fear
    """,
    tools=[get_pcos_diet, debunk_pcos_myth]
)
