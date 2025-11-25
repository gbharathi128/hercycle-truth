import streamlit as st
from dotenv import load_dotenv
import google.generativeai as genai
import os

load_dotenv()
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

st.set_page_config(
    page_title="HerCycle Truth — PCOS Support",
    page_icon="💗",
    layout="wide"
)

st.markdown(
    "<h1 style='text-align: center; color: #ff6fb3;'>💗 HerCycle Truth — Your PCOS Support Companion</h1>",
    unsafe_allow_html=True
)

st.write("Use the left sidebar to explore diet plans, yoga, reminders, goals, and chat with the agent.")
