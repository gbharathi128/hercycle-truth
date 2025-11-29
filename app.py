import streamlit as st
from graph import main_chat

st.set_page_config(page_title="HerCycle AI Agent", page_icon="💗")

st.title("💗 Chat With HerCycle Agent")

if "chat" not in st.session_state:
    st.session_state.chat = []

user_input = st.text_input("🧍‍♀️ You:", "")

if st.button("Send") and user_input.strip() != "":
    response = main_chat(user_input)
    st.session_state.chat.append(("🧍‍♀️ You", user_input))
    st.session_state.chat.append(("🤍 HerCycle Agent", response))

for role, text in st.session_state.chat:
    st.markdown(f"**{role}:** {text}")
