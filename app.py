import streamlit as st
import os

# --- PAGE CONFIG ---
st.set_page_config(
    page_title="HerCycle Truth",
    page_icon="💗",
    layout="wide"
)

# --- LOAD ASSETS ---
ASSETS = "assets"

bg_image = os.path.join(ASSETS, "banner_home.jpg")
logo = os.path.join(ASSETS, "logo.png")
diet_img = os.path.join(ASSETS, "day1.png")
yoga_img = os.path.join(ASSETS, "yoga1.png")
reminder_img = os.path.join(ASSETS, "bell_icon.png")
goals_img = os.path.join(ASSETS, "exercise1.png")
chat_img = os.path.join(ASSETS, "day2.png")

# --- CUSTOM CSS FOR PRETTY UI ---
page_bg = f"""
<style>
[data-testid="stAppViewContainer"] {{
    background-image: url("{bg_image}");
    background-size: cover;
    background-position: center;
    background-repeat: no-repeat;
}}

.sidebar .sidebar-content {{
    background-color: rgba(255, 240, 245, 0.7);
    backdrop-filter: blur(10px);
}}
</style>
"""
st.markdown(page_bg, unsafe_allow_html=True)


# --- SIDEBAR ---
st.sidebar.image(logo, width=180)
st.sidebar.markdown("## 🌸 HerCycle Truth")
st.sidebar.write("Your PCOS Lifestyle Sister 💗")

st.sidebar.markdown("---")
st.sidebar.markdown("### Navigation")
st.sidebar.page_link("pages/1_✨_Diet_Plan.py", label="✨ Diet Plan")
st.sidebar.page_link("pages/2_🧘‍♀️_Yoga_Exercises.py", label="🧘 Yoga Exercises")
st.sidebar.page_link("pages/3_⏰_Reminders.py", label="⏰ Reminders")
st.sidebar.page_link("pages/4_📋_Daily_Goals.py", label="📋 Daily Goals")
st.sidebar.page_link("pages/5_💗_Chat_With_Agent.py", label="💗 Chat With Agent")


# --- HOME PAGE CONTENT ---
col1, col2 = st.columns([1, 1])

with col1:
    st.markdown("<h1 style='color:#d63384;'>Welcome to HerCycle Truth 💗</h1>", unsafe_allow_html=True)
    st.write("""
    Your personalized PCOS lifestyle companion —  
    made with love, empathy, and science 🌸  
    Choose any feature from the left menu.
    """)

with col2:
    st.image(bg_image, use_column_width=True)

st.markdown("### 🌼 What you can do here")
c1, c2, c3 = st.columns(3)

with c1:
    st.image(diet_img, width=120)
    st.markdown("**✨ Weekly Diet Plans**")

with c2:
    st.image(yoga_img, width=120)
    st.markdown("**🧘 Personalized Yoga**")

with c3:
    st.image(chat_img, width=120)
    st.markdown("**💗 Ask Anything Agent**")
