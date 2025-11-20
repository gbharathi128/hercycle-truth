# diet_plan.py
from typing import Dict

BASE_WEEK = {
    "Monday":    {"Breakfast": "Oats porridge + chia + berries", "Lunch": "Millet roti + dal + salad", "Dinner": "Grilled paneer + steamed veggies"},
    "Tuesday":   {"Breakfast": "Ragi dosa + sambar", "Lunch": "Brown rice + rajma + cucumber", "Dinner": "Quinoa bowl with chickpeas"},
    "Wednesday": {"Breakfast": "Protein smoothie (spinach+banana+protein)", "Lunch": "Whole-wheat chapati + veg curry", "Dinner": "Baked tofu + greens"},
    "Thursday":  {"Breakfast": "Greek yogurt + seeds + fruit", "Lunch": "Millet khichdi + stir-fried veg", "Dinner": "Mixed bean salad"},
    "Friday":    {"Breakfast": "Poha with peas + peanuts", "Lunch": "Brown rice + dal + veggies", "Dinner": "Vegetable soup + multigrain toast"},
    "Saturday":  {"Breakfast": "Besan chilla + spinach", "Lunch": "Quinoa pulao + raita", "Dinner": "Moong dal + salad"},
    "Sunday":    {"Breakfast": "Idli + sambar", "Lunch": "Multi-grain rotis + mixed sabzi", "Dinner": "Light stew + salad"}
}

def generate_weekly_diet(goal: str = "balanced", preference: str = "veg"):
    """
    goal: 'balanced' | 'weight_loss' | 'energy'
    preference: 'veg' | 'vegan' | 'nonveg'
    """
    out = {}
    for day, meals in BASE_WEEK.items():
        m = meals.copy()
        if goal == "weight_loss":
            m["Dinner"] = m["Dinner"] + " (lighter portion)"
        elif goal == "energy":
            m["Breakfast"] = m["Breakfast"] + " + boiled egg/protein (optional)"
        # preference tweaks (simple)
        if preference == "vegan":
            m = {k: v.replace("paneer", "tofu").replace("yogurt", "plant yogurt").replace("egg", "tofu scramble") for k,v in m.items()}
        elif preference == "nonveg":
            m = {k: (v + " + grilled chicken/fish") if k == "Lunch" else v for k,v in m.items()}
        out[day] = m
    return out
