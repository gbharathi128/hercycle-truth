import streamlit as st
from tools.pcos_tools import gemini_agent

st.set_page_config(page_title="HerCycle — PCOS AI Agent", layout="wide")

st.title("💗 HerCycle — Your PCOS AI Companion")

if "chat" not in st.session_state:
    st.session_state.chat = []

query = st.text_input("Ask anything about PCOS...")

if st.button("Send") and query.strip():
    st.session_state.chat.append(("user", query))
    reply = gemini_agent(query)
    st.session_state.chat.append(("ai", reply))

for role, text in st.session_state.chat:
    if role == "user":
        st.markdown(f"**🧍‍♀️ You:** {text}")
    else:
        st.markdown(f"**🤖 HerCycle Agent:** {text}")
