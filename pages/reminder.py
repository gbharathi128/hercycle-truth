import streamlit as st
from pathlib import Path

# ------------------------------
# Page Title
# ------------------------------
st.title("⏰ PCOS Health Reminders")

# ------------------------------
# Load Assets
# ------------------------------
assets_path = Path("assets")
bell_icon = assets_path / "bell_icon.png"

# ------------------------------
# Intro Text
# ------------------------------
st.write(
    """
### Smart Daily Reminders  
Stay consistent with your routine — it's the key to managing PCOS effectively.
Set simple reminders for hydration, meals, medication, sleep cycle, or workout.
    """
)

# ------------------------------
# Display Bell Icon
# ------------------------------
if bell_icon.exists():
    st.image(str(bell_icon), width=120)
else:
    st.warning(f"Image not found: {bell_icon}")

# ------------------------------
# Reminder Form
# ------------------------------
st.subheader("🔔 Create Your Reminder")

reminder_text = st.text_input("Reminder Name")
reminder_time = st.time_input("Select Time")

if st.button("Save Reminder"):
    if reminder_text.strip():
        st.success(f"Reminder saved: **{reminder_text} at {reminder_time}**")
    else:
        st.error("Please enter a reminder name.")

st.markdown("---")

st.info("Tip: Keep reminders simple and consistent — small actions daily create big changes.")
