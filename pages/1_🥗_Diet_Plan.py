import streamlit as st

st.title("🥗 7-Day PCOS Diet Plan")

BASE = "assets"   # image folder

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

# --------- ADD GLOBAL CSS FOR HOVER + TEXT SIZE ----------
st.markdown("""
<style>
.card-box {
    background: rgba(255, 255, 255, 0.55); /* transparent white */
    border-radius: 18px;
    padding: 25px;
    margin-bottom: 30px;
    backdrop-filter: blur(8px);
    box-shadow: 0 4px 12px rgba(0,0,0,0.06);
}

.card-title {
    font-size: 26px;
    font-weight: 700;
    color: #d63384;
}

.card-text {
    font-size: 18px;
}

.img-hover:hover {
    transform: scale(1.06);
    transition: 0.4s ease-in-out;
}

.img-hover {
    border-radius: 14px;
    transition: 0.4s;
}
</style>
""", unsafe_allow_html=True)
# ---------------------------------------------------------


for day, data in diet_plan.items():
    st.markdown('<div class="card-box">', unsafe_allow_html=True)

    col1, col2 = st.columns([1.1, 2])

    with col1:
        st.markdown(
            f'<img src="{data["Image"]}" class="img-hover" width="100%">',
            unsafe_allow_html=True
        )

    with col2:
        st.markdown(
            f"""
            <div class="card-title">✨ {day} Meal Plan</div>
            <div class="card-text"><b>🍳 Breakfast:</b> {data['Breakfast']}</div>
            <div class="card-text"><b>🥗 Lunch:</b> {data['Lunch']}</div>
            <div class="card-text"><b>🍛 Dinner:</b> {data['Dinner']}</div>
            """,
            unsafe_allow_html=True
        )

    st.markdown('</div>', unsafe_allow_html=True)
