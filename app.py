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

    # Get AI response
    reply = gemini_agent(query)
    st.session_state.chat.append(("ai", reply))

# Display chat with bubbles
for role, text in st.session_state.chat:
    if role == "user":
        st.markdown(
            f"""
            <div style="
                background-color:#f0f0f0;
                padding:10px;
                border-radius:10px;
                margin:10px 0;
                width:fit-content;
                max-width:80%;
            ">
                🧍‍♀️ <b>You:</b> {text}
            </div>
            """,
            unsafe_allow_html=True,
        )
    else:
        st.markdown(
            f"""
            <div style="
                background-color:#ffc0cb;
                padding:10px;
                border-radius:10px;
                margin:10px 0;
                width:fit-content;
                max-width:80%;
            ">
                🤖 <b>HerCycle Agent:</b> {text}
            </div>
            """,
            unsafe_allow_html=True,
        )
