import streamlit as st
import os

st.title("🥗 7-Day PCOS Diet Plan")

# Base path for local images
BASE_IMG = "assets"

diet_plan = {
    "Day 1": {
        "Breakfast": "Oats with chia seeds + Apple",
        "Lunch": "2 Rotis + Mixed veg curry + Cucumber salad",
        "Dinner": "Brown rice + Dal + Stir-fried vegetables",
        "Image": os.path.join(BASE_IMG, "day1.png")
    },
    "Day 2": {
        "Breakfast": "Sprouts bowl + Green tea",
        "Lunch": "Quinoa salad + Paneer cubes",
        "Dinner": "Roti + Chicken/Paneer curry + Veg soup",
        "Image": os.path.join(BASE_IMG, "day2.png")
    },
    "Day 3": {
        "Breakfast": "Ragi dosa + Coconut chutney",
        "Lunch": "Millet khichdi + Veg raita",
        "Dinner": "2 Rotis + Dal + Veg sabzi",
        "Image": os.path.join(BASE_IMG, "day3.png")
    },
    "Day 4": {
        "Breakfast": "Upma + Lemon water",
        "Lunch": "Brown rice + Rajma + Salad",
        "Dinner": "Roti + Mushroom curry + Boiled veggies",
        "Image": os.path.join(BASE_IMG, "day4.png")
    },
    "Day 5": {
        "Breakfast": "Smoothie (banana + oats + flaxseed)",
        "Lunch": "2 Rotis + Aloo gobi + Sprouts",
        "Dinner": "Vegetable soup + Grilled paneer",
        "Image": os.path.join(BASE_IMG, "day5.png")
    },
    "Day 6": {
        "Breakfast": "Poha + Almonds",
        "Lunch": "Lemon rice + Chana curry",
        "Dinner": "Roti + Egg curry (or paneer for veg)",
        "Image": os.path.join(BASE_IMG, "day6.png")
    },
    "Day 7": {
        "Breakfast": "Idli + Sambar + Green tea",
        "Lunch": "Veg biryani (brown rice) + Raita",
        "Dinner": "Millet roti + Dal tadka + Veg sabzi",
        "Image": os.path.join(BASE_IMG, "day7.png")
    }
}

for day, info in diet_plan.items():
    with st.expander(day):
        col1, col2 = st.columns([1, 2])

        with col1:
            st.image(info["Image"], width=180)

        with col2:
            st.markdown(f"""
                ### 🍽️ {day} Meal Plan  
                **🍳 Breakfast:** {info['Breakfast']}  
                **🥗 Lunch:** {info['Lunch']}  
                **🍛 Dinner:** {info['Dinner']}  
            """)
