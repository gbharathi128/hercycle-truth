import streamlit as st
import os

st.title("🥗 7-Day PCOS Diet Plan")

BASE = "assets"   # folder where your images are stored

diet_plan = {
    "Day 1": {
        "Image": f"{BASE}/day1.png",
        "Breakfast": "Oats with chia seeds + Apple",
        "Lunch": "2 Rotis + Mixed veg curry + Cucumber salad",
        "Dinner": "Brown rice + Dal + Stir-fried vegetables",
    },
    "Day 2": {
        "Image": f"{BASE}/day2.png",
        "Breakfast": "Sprouts bowl + Green tea",
        "Lunch": "Quinoa salad + Paneer cubes",
        "Dinner": "Roti + Paneer/Chicken curry + Veg soup",
    },
    "Day 3": {
        "Image": f"{BASE}/day3.png",
        "Breakfast": "Ragi dosa + Coconut chutney",
        "Lunch": "Millet khichdi + Veg raita",
        "Dinner": "Rotis + Dal + Veg sabzi",
    },
    "Day 4": {
        "Image": f"{BASE}/day4.png",
        "Breakfast": "Upma + Lemon water",
        "Lunch": "Brown rice + Rajma + Salad",
        "Dinner": "Roti + Mushroom curry + Boiled veggies",
    },
    "Day 5": {
        "Image": f"{BASE}/day5.png",
        "Breakfast": "Smoothie (banana + oats + flaxseed)",
        "Lunch": "Rotis + Aloo gobi + Sprouts",
        "Dinner": "Vegetable soup + Grilled paneer",
    },
    "Day 6": {
        "Image": f"{BASE}/day6.png",
        "Breakfast": "Poha + Almonds",
        "Lunch": "Lemon rice + Chana curry",
        "Dinner": "Rotis + Egg curry or Paneer",
    },
    "Day 7": {
        "Image": f"{BASE}/day7.png",
        "Breakfast": "Idli + Sambar + Green tea",
        "Lunch": "Veg biryani (brown rice) + Raita",
        "Dinner": "Millet roti + Dal tadka + Veg sabzi",
    },
}

for day, data in diet_plan.items():
    with st.container():

        st.markdown(
            f"""
            <div style="
                background-color: #ffe6f2;
                border-radius: 18px;
                padding: 20px;
                margin-bottom: 25px;
                box-shadow: 0 4px 12px rgba(0,0,0,0.07);
            ">
            """,
            unsafe_allow_html=True
        )

        col1, col2 = st.columns([1.1, 2])

        with col1:
            st.image(data["Image"], use_column_width=True)

        with col2:
            st.markdown(
                f"""
                <h3 style="margin-top: -5px;">✨ {day} Meal Plan</h3>
                <p><strong>🍳 Breakfast:</strong> {data['Breakfast']}</p>
                <p><strong>🥗 Lunch:</strong> {data['Lunch']}</p>
                <p><strong>🍛 Dinner:</strong> {data['Dinner']}</p>
                """,
                unsafe_allow_html=True
            )

        st.markdown("</div>", unsafe_allow_html=True)
