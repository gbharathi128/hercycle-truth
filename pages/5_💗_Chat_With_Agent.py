import streamlit as st
from tools.pcos_tools import ask_agent

st.set_page_config(page_title="Chat With HerCycle Agent", page_icon="💗")

# ---- PAGE HEADER ----
st.title("💗 Chat With Your PCOS Support Agent")
st.write("Ask anything about PCOS, diet, periods, symptoms, workouts, mental health, and more!")

# ---- USER INPUT ----
user_input = st.text_input("Type your question here...", "")

if st.button("Ask"):
    if user_input.strip() == "":
        st.warning("Please enter a question.")
    else:
        with st.spinner("Thinking..."):
            reply = ask_agent(user_input)

        # ---- SHOW RESPONSE ----
        st.markdown(
            f"""
            <div style="
                background-color:#ffe6f2;
                padding:15px; 
                border-radius:10px; 
                border-left:6px solid #ff4da6;
                margin-top:10px;
            ">
                <b>💗 Agent:</b> {reply}
            </div>
            """,
            unsafe_allow_html=True
        )

