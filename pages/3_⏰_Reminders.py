import streamlit as st

st.set_page_config(page_title="Reminders", page_icon="⏰")

st.title("⏰ Daily Healthy Reminders")

st.write("Stay consistent with small healthy habits. These reminders help you manage PCOS better every day.")

# Reminder Icons
st.image("assets/bell_icon.png", width=80)

st.subheader("🔔 Your Daily Reminders")

reminders = [
    "💧 Drink 3–4 liters of water daily",
    "🚶‍♀️ Walk at least 6,000 steps",
    "🧘‍♀️ Do 10 minutes of deep breathing",
    "🍽️ Avoid sugar & junk food",
    "😴 Sleep 7–8 hours",
    "📅 Track your menstrual cycle regularly"
]

for r in reminders:
    st.checkbox(r)

