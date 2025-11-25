import streamlit as st
from tools.pcos_tools import gemini_agent

st.set_page_config(page_title="HerCycle — PCOS AI Agent", layout="wide")

st.title("💗 HerCycle — Your PCOS AI Companion")

# Initialize chat history
if "chat" not in st.session_state:
    st.session_state.chat = []

# User input
query = st.text_input("Ask anything about PCOS...")

if st.button("Send") and query.strip():
    # Save user message
    st.session_state.chat.append(("user", query))

    # Get Gemini response
    reply = gemini_agent(query)
    st.session_state.chat.append(("ai", reply))

# Display chat conversation
for role, text in st.session_state.chat:
    if role == "user":
        st.markdown(f"**🧍‍♀️ You:** {text}")
    else:
        st.markdown(f"**🤖 HerCycle Agent:** {text}")
