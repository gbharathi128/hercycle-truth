import streamlit as st
from graph import graph
import os
from dotenv import load_dotenv

load_dotenv()

st.set_page_config(page_title="HerCycle Truth ♀️", page_icon="♀️", layout="centered")

st.title("♀️ HerCycle Truth")
st.markdown("**Your caring AI sister for PCOS truth & support — free, forever**")
st.markdown("_Built for Kaggle Agents for Good Capstone 2025_")

if "messages" not in st.session_state:
    st.session_state.messages = []

for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

if prompt := st.chat_input("Ask anything about PCOS — symptoms, fertility, myths, lifestyle..."):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):
        with st.spinner("Thinking with care ♀️..."):
            response = graph.invoke({
                "messages": st.session_state.messages[-10:],  # last 10 for context
                "language": "English"
            }, config={"configurable": {"thread_id": "pcos_session"}})
            answer = response["messages"][-1].content
            st.markdown(answer)
            st.session_state.messages.append({"role": "assistant", "content": answer})

st.markdown("---")
st.caption("Always consult your doctor • Built with love for 116 million women with PCOS")
