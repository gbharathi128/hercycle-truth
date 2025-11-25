import streamlit as st

st.set_page_config(page_title="Diet Plan")

st.title("🥗 7-Day PCOS Diet Plan")

diet_plan = {
    "Day 1": {
        "Image": "assets/day1.png",
        "Breakfast": "Oats with chia seeds + Apple",
        "Lunch": "2 Rotis + Veg curry + Cucumber salad",
        "Dinner": "Brown rice + Dal + Stir-fried vegetables",
    },
    "Day 2": {
        "Image": "assets/day2.png",
        "Breakfast": "Sprouts bowl + Green tea",
        "Lunch": "Quinoa salad + Paneer cubes",
        "Dinner": "Roti + Paneer/Chicken curry + Veg soup",
    },
    "Day 3": {
        "Image": "assets/day3.png",
        "Breakfast": "Ragi dosa + Coconut chutney",
        "Lunch": "Millet khichdi + Veg raita",
        "Dinner": "Roti + Dal + Veg sabzi",
    },
    "Day 4": {
        "Image": "assets/day4.png",
        "Breakfast": "Upma + Lemon water",
        "Lunch": "Brown rice + Rajma + Salad",
        "Dinner": "Roti + Mushroom curry + Boiled veggies",
    },
    "Day 5": {
        "Image": "assets/day5.png",
        "Breakfast": "Smoothie (banana + oats + flaxseed)",
        "Lunch": "Rotis + Aloo gobi + Sprouts",
        "Dinner": "Vegetable soup + Grilled paneer",
    },
    "Day 6": {
        "Image": "assets/day6.png",
        "Breakfast": "Poha + Almonds",
        "Lunch": "Lemon rice + Chana curry",
        "Dinner": "Rotis + Egg curry or Paneer",
    },
    "Day 7": {
        "Image": "assets/day7.png",
        "Breakfast": "Idli + Sambar + Green tea",
        "Lunch": "Veg biryani (brown rice) + Raita",
        "Dinner": "Millet roti + Dal tadka + Veg sabzi",
    },
}

# 🌸 Styling (transparent card + hover)
st.markdown("""
<style>
.card {
    background: rgba(255, 255, 255, 0.6);
    padding: 22px;
    border-radius: 20px;
    margin-bottom: 22px;
    box-shadow: 0 4px 12px rgba(0,0,0,0.12);
    backdrop-filter: blur(8px);
}

.card-title {
    font-size: 26px;
    font-weight: bold;
    color: #d63384;
    padding-bottom: 10px;
}

.card-text {
    font-size: 19px;
    margin-bottom: 6px;
}

.img-hover {
    transition: 0.35s ease-in-out;
    border-radius: 16px;
}

.img-hover:hover {
    transform: scale(1.04);
}
</style>
""", unsafe_allow_html=True)

# 🖼️ FIX: load images using st.image()
for day, data in diet_plan.items():
    st.markdown('<div class="card">', unsafe_allow_html=True)

    col1, col2 = st.columns([1.2, 2])

    with col1:
        st.image(data["Image"], use_column_width=True)

    with col2:
        st.markdown(
            f"""
            <div class="card-title">{day} ✨</div>
            <div class="card-text"><b>🍳 Breakfast:</b> {data['Breakfast']}</div>
            <div class="card-text"><b>🥗 Lunch:</b> {data['Lunch']}</div>
            <div class="card-text"><b>🍛 Dinner:</b> {data['Dinner']}</div>
            """,
            unsafe_allow_html=True
        )

    st.markdown("</div>", unsafe_allow_html=True)
