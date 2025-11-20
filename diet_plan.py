# diet_plan.py
"""
Simple weekly diet plan generator for PCOS-friendly meals.
This is a lightweight generator — you can expand rules later.
"""

from typing import Dict

BASE_WEEK = {
    "Monday":    {"Breakfast": "Oats porridge with chia + berries", "Lunch": "Millet roti + lentil curry + salad", "Dinner": "Grilled paneer + mixed veg"},
    "Tuesday":   {"Breakfast": "Ragi dosa + sambar", "Lunch": "Brown rice + rajma + cucumber salad", "Dinner": "Quinoa bowl with veggies and chickpeas"},
    "Wednesday": {"Breakfast": "Smoothie: spinach + banana + protein", "Lunch": "Whole-wheat chapati + dal + veggies", "Dinner": "Baked fish/tofu + steamed greens"},
    "Thursday":  {"Breakfast": "Greek yogurt + seeds + fruit", "Lunch": "Millet khichdi + stir-fried veggies", "Dinner": "Mixed bean salad + roasted veg"},
    "Friday":    {"Breakfast": "Poha with peanuts + veggies", "Lunch": "Brown rice + grilled vegetables + dal", "Dinner": "Lentil soup + small salad"},
    "Saturday":  {"Breakfast": "Besan chilla with spinach", "Lunch": "Quinoa pulao + raita", "Dinner": "Grilled chicken/soy + roasted veg"},
    "Sunday":    {"Breakfast": "Idli + sambar + chutney", "Lunch": "Multi-grain rotis + mixed sabzi", "Dinner": "Light vegetable stew + salad"}
}

def generate_weekly_diet(goal: str = "balanced") -> Dict[str, Dict[str, str]]:
    """
    goal: can be 'balanced', 'weight_loss', or 'energy'
    Apply minor adjustments based on goal.
    """
    out = {}
    for day, meals in BASE_WEEK.items():
        new = meals.copy()
        if goal == "weight_loss":
            # Slightly lighter dinners
            new["Dinner"] = new["Dinner"] + " (lighter portion, extra salad)"
        elif goal == "energy":
            new["Breakfast"] = new["Breakfast"] + " + boiled egg/protein"
        out[day] = new
    return out
