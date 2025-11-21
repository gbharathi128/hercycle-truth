import streamlit as st
from pathlib import Path

# ------------------------------
# Page Title
# ------------------------------
st.title("🥗 Weekly Diet Plan")

# ------------------------------
# Load Images
# ------------------------------
assets_path = Path("assets")

day_images = {
    "Day 1": assets_path / "day1.png",
    "Day 2": assets_path / "day2.png",
    "Day 3": assets_path / "day3.png",
    "Day 4": assets_path / "day4.png",
    "Day 5": assets_path / "day5.png",
    "Day 6": assets_path / "day6.png",
    "Day 7": assets_path / "day7.png",
}

# ------------------------------
# Intro Text
# ------------------------------
st.write(
    """
### Your Personalized 7-Day PCOS Diet Guide  
Nutrient-dense, hormone-friendly meals designed to reduce inflammation, balance insulin levels, and boost energy.
    """
)

# ------------------------------
# Display Each Day’s Diet
# ------------------------------
for day, img_path in day_images.items():
    st.subheader(f"📅 {day}")
    if img_path.exists():
        st.image(str(img_path), use_column_width=True)
    else:
        st.warning(f"Image missing: {img_path}")

    st.markdown("---")
