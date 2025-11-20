import streamlit as st
from graph import graph

st.set_page_config(page_title="HerCycle Truth — PCOS Support", layout="wide")

st.title("💗 HerCycle Truth — Your PCOS Support Companion")

query = st.text_area("Ask anything about PCOS...")

if st.button("Send"):
    result = graph.invoke({
        "messages": [{"role": "user", "content": query}]
    })

    ai_response = result["messages"][-1]
    st.write(ai_response)
