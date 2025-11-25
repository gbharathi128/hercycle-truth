import streamlit as st

st.set_page_config(page_title="Yoga Exercises", page_icon="🧘‍♀️")

st.title("🧘‍♀️ PCOS Yoga & Stretching Exercises")

st.write("These poses are scientifically shown to help balance hormones, reduce stress, and improve PCOS symptoms.")

st.subheader("✨ Yoga Poses")

col1, col2 = st.columns(2)

with col1:
    st.image("assets/yoga1.png", caption="Yoga Pose 1")
    st.image("assets/yoga2.png", caption="Yoga Pose 2")

with col2:
    st.image("assets/stretch1.png", caption="Stretch Exercise 1")
    st.image("assets/exercise1.png", caption="Exercise 1")

