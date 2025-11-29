import streamlit as st
from tools.pcos_tools import gemini_agent

st.set_page_config(page_title="HerCycle — PCOS AI Agent 💗", layout="wide")

st.title("💗 HerCycle — Chat With Your PCOS Sister")
st.write("Ask anything about PCOS, periods, mood, diet, symptoms, motivation… I’m here for you 🤍")

# Chat history
if "chat" not in st.session_state:
    st.session_state.chat = []

# Input box
query = st.text_input("Write your question:")

if st.button("Send") and query.strip():
    st.session_state.chat.append(("user", query))
    reply = gemini_agent(query)
    st.session_state.chat.append(("ai", reply))

# Chat UI
for role, text in st.session_state.chat:
    if role == "user":
        st.markdown(
            f"""
            <div style="background:#edf2f7;padding:10px;border-radius:10px;margin:8px 0;max-width:80%;">
            🧍‍♀️ <b>You:</b> {text}
            </div>
            """,
            unsafe_allow_html=True,
        )
    else:
        st.markdown(
            f"""
            <div style="background:#ffb6c1;padding:10px;border-radius:10px;margin:8px 0;max-width:80%;">
            🤍 <b>HerCycle Agent:</b> {text}
            </div>
            """,
            unsafe_allow_html=True,
        )
