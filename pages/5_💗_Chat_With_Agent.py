import streamlit as st
import sys
import os

# --- Fix import path (very important) ---
CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))
PARENT_DIR = os.path.dirname(CURRENT_DIR)
sys.path.append(PARENT_DIR)

from tools.pcos_tools import ask_agent   # now it will import correctly

# --- Page UI ---
st.set_page_config(page_title="HerCycle Agent 💗", page_icon="💗")

st.title("💗 Chat With Your PCOS Agent")
st.write("Ask anything about PCOS, diet, symptoms, motivation, lifestyle, myths… I'm here for you 🤍")

# Chat input
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

user_msg = st.text_input("Write your question:")

if st.button("Ask"):
    if user_msg:
        # Add user message
        st.session_state.chat_history.append(("You", user_msg))

        # Agent response
        reply = ask_agent(user_msg)
        st.session_state.chat_history.append(("HerCycle Agent 💗", reply))

# Show chat history
for sender, message in st.session_state.chat_history:
    if sender == "You":
        st.markdown(f"**🧍‍♀️ You:** {message}")
    else:
        st.markdown(f"**🤍 HerCycle Agent:** {message}")
