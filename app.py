import streamlit as st
from pcos_tools import gemini_agent

st.set_page_config(page_title="HerCycle — PCOS Chat", page_icon="💗")

st.title("💗 HerCycle — Chat With Your PCOS Sister")
st.write("Ask anything about PCOS, periods, mood, diet, symptoms, motivation… I’m here for you 🤍")

user_input = st.text_input("Write your question:")

if st.button("Send"):
    if user_input.strip() == "":
        st.warning("Please type something first 🥺")
    else:
        reply = gemini_agent(user_input)
        st.chat_message("user").write(user_input)
        st.chat_message("assistant").write(reply)
