import os
import streamlit as st
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()

API_KEY = st.secrets.get("GEMINI_API_KEY") or os.getenv("GEMINI_API_KEY")

if not API_KEY:
    raise ValueError("❌ GEMINI_API_KEY not found in secrets or .env")

genai.configure(api_key=API_KEY)
