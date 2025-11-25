import streamlit as st

st.set_page_config(page_title="Daily Goals", page_icon="📋")

st.title("📋 Daily Goals Tracker")

st.write("Tick off your daily wellness goals and stay consistent on your PCOS healing journey.")

# Icons
col1, col2, col3 = st.columns(3)

with col1:
    st.image("assets/water_icon.png", width=80)
    st.checkbox("Drink 8 glasses of water")

with col2:
    st.image("assets/sleep_icon.png", width=80)
    st.checkbox("Sleep 7–8 hours")

with col3:
    st.image("assets/bell_icon.png", width=80)
    st.checkbox("Take medications on time")

st.subheader("✨ Additional Goals")
st.checkbox("10 minutes meditation")
st.checkbox("30 minutes walk")
st.checkbox("Avoid junk food")
st.checkbox("Track today's symptoms")

