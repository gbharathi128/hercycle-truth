import streamlit as st
from pathlib import Path

# ------------------------------
# Page Title
# ------------------------------
st.title("📋 Daily Wellness Goals")

# ------------------------------
# Load Icons
# ------------------------------
assets_path = Path("assets")

water_icon = assets_path / "water_icon.png"
sleep_icon = assets_path / "sleep_icon.png"
bell_icon = assets_path / "bell_icon.png"

# ------------------------------
# Aesthetic Intro
# ------------------------------
st.write(
    """
### Build Healthy Habits 🌿  
Small routine changes help balance hormones, boost energy & reduce PCOS symptoms.  
Track your daily goals below — stay consistent, stay kind to your body. 💗
"""
)

st.markdown("---")

# ------------------------------
# Water Intake Goal
# ------------------------------
st.subheader("💧 Water Intake")

if water_icon.exists():
    st.image(str(water_icon), width=90)

water = st.slider("How many glasses did you drink today?", 0, 12, 6)
st.success(f"Great! You logged **{water} glasses** today.")

st.markdown("---")

# ------------------------------
# Sleep Goal
# ------------------------------
st.subheader("😴 Sleep Tracker")

if sleep_icon.exists():
    st.image(str(sleep_icon), width=90)

sleep_hours = st.slider("Hours slept last night", 0, 12, 7)
st.info(f"You slept **{sleep_hours} hours**. Aim for 7–9 hours daily.")

st.markdown("---")

# ------------------------------
# Medication / Supplements Reminder
# ------------------------------
st.subheader("💊 Medication / Supplements")

if bell_icon.exists():
    st.image(str(bell_icon), width=80)

med_taken = st.checkbox("I took my medication/supplements today")

if med_taken:
    st.success("✔️ Good job! Consistency matters.")
else:
    st.warning("Make sure to take them on time 💗")

st.markdown("---")

# ------------------------------
# Mood Check
# ------------------------------
st.subheader("💗 Mood Check-In")

mood = st.selectbox(
    "How are you feeling today?",
    ["😊 Good", "😐 Okay", "😔 Low", "😤 Stressed", "💪 Motivated"]
)

st.write(f"**Mood logged:** {mood}")

st.markdown("---")

st.caption("✨ Keep going — every small step counts.")

