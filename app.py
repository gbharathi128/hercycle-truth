import streamlit as st
from PIL import Image

st.set_page_config(
    page_title="HerCycle Truth — PCOS Companion",
    layout="wide",
)

# ----------------------------
# Load images
# ----------------------------
logo = "assets/logo.png"
banner = "assets/banner_home.png"

# ----------------------------
# Custom CSS for Aesthetic UI
# ----------------------------
st.markdown("""
    <style>
        /* Remove padding */
        .block-container {
            padding-top: 0rem !important;
        }

        /* Hero section */
        .hero {
            background-image: url('assets/banner_home.png');
            background-size: cover;
            background-position: center;
            border-radius: 25px;
            height: 330px;
            padding: 40px;
            display: flex;
            align-items: center;
            justify-content: left;
            color: white;
            font-family: 'Poppins', sans-serif;
            position: relative;
        }

        .hero-overlay {
            position: absolute;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
            border-radius: 25px;
            background: rgba(255, 182, 193, 0.35);
        }

        .hero-content {
            position: relative;
            z-index: 2;
            max-width: 60%;
        }

        .big-title {
            font-size: 42px;
            font-weight: 700;
        }

        .subtitle {
            font-size: 20px;
            margin-top: -10px;
        }

        .card {
            background: rgba(255, 255, 255, 0.65);
            backdrop-filter: blur(12px);
            border-radius: 22px;
            padding: 25px;
            box-shadow: 0px 3px 15px rgba(0,0,0,0.08);
            text-align: center;
            transition: 0.3s ease;
            cursor: pointer;
        }

        .card:hover {
            transform: translateY(-5px);
            box-shadow: 0px 8px 20px rgba(0,0,0,0.12);
        }

        .card img {
            width: 70px;
            margin-bottom: 15px;
        }

        .card-title {
            font-size: 20px;
            font-weight: 600;
        }

    </style>
""", unsafe_allow_html=True)

# ----------------------------
# LOGO
# ----------------------------
st.image(logo, width=120)

# ----------------------------
# HERO SECTION
# ----------------------------
st.markdown("""
<div class="hero">
    <div class="hero-overlay"></div>
    <div class="hero-content">
        <div class="big-title">HerCycle Truth 💗</div>
        <div class="subtitle">Your PCOS Lifestyle Sister — Here for your Diet, Yoga, Goals & Emotional Support.</div>
    </div>
</div>
""", unsafe_allow_html=True)

st.write("")
st.write("")

# ----------------------------
# Feature Cards
# ----------------------------
features = {
    "Diet Plan": ("assets/day1.png", "Diet Plan"),
    "Yoga & Exercise": ("assets/yoga1.png", "Yoga Exercises"),
    "Daily Goals": ("assets/water_icon.png", "Daily Goals"),
    "Reminders": ("assets/bell_icon.png", "Reminders"),
    "Chat With Agent": ("assets/logo.png", "Chat With Agent")
}

col1, col2, col3 = st.columns(3)
col4, col5 = st.columns(2)

# Row 1
with col1:
    if st.button("🍽️ Diet Plan", key="d1"):
        st.switch_page("pages/diet_plan.py")
with col2:
    if st.button("🧘‍♀️ Yoga Exercises", key="y1"):
        st.switch_page("pages/yoga_exercises.py")
with col3:
    if st.button("📋 Daily Goals", key="g1"):
        st.switch_page("pages/daily_goals.py")

# Row 2
with col4:
    if st.button("⏰ Reminders", key="r1"):
        st.switch_page("pages/reminder.py")
with col5:
    if st.button("💗 Chat with Agent", key="c1"):
        st.switch_page("pages/chat_with_agent.py")
