
import streamlit as st

st.set_page_config(page_title="Diet Plan", page_icon="🥗")

st.title("🥗 PCOS Diet Plan (Day-wise)")

st.write("Follow this simple 7-day PCOS-friendly diet plan.")

col1, col2 = st.columns(2)

with col1:
    st.image("assets/day1.png", caption="Day 1")
    st.image("assets/day2.png", caption="Day 2")
    st.image("assets/day3.png", caption="Day 3")
    st.image("assets/day4.png", caption="Day 4")

with col2:
    st.image("assets/day5.png", caption="Day 5")
    st.image("assets/day6.png", caption="Day 6")
    st.image("assets/day7.png", caption="Day 7")
