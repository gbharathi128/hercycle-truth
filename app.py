from dotenv import load_dotenv
load_dotenv()
import streamlit as st
import os

st.set_page_config(
    page_title="HerCycle Truth",
    page_icon="💗",
    layout="wide"
)

# ---- LOAD LOGO ----
LOGO_PATH = "assets/logo.png"

if os.path.exists(LOGO_PATH):
    st.sidebar.image(LOGO_PATH, width=150)
else:
    st.sidebar.write("Logo missing in assets/")

st.sidebar.title("✨ Navigation")
st.sidebar.write("Choose a page from left sidebar menu.")

st.title("💗 HerCycle Truth — Women's PCOS Support App")
st.write("Your personalized companion for Diet • Yoga • Reminders • Daily Goals • AI Chat Assistant.")

st.markdown(
    """
    <div style="
        background-color:#ffe6f7;
        padding:25px;
        border-radius:12px;
        border-left: 8px solid #ff4da6;
        margin-top:20px;
        font-size:18px;
    ">
    🌸 <b>Welcome Queen!</b><br>
    This app is designed to take care of your PCOS journey with love, comfort and daily guidance.
    </div>
    """,
    unsafe_allow_html=True
)

# ---- MAIN BANNER ----
banner = "assets/banner_home.png"
if os.path.exists(banner):
    st.image(banner, use_column_width=True)
