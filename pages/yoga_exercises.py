import streamlit as st
from pathlib import Path

# ------------------------------
# Page Title
# ------------------------------
st.title("🧘‍♀️ Yoga & Stretching for PCOS")

# ------------------------------
# Load Images
# ------------------------------
assets_path = Path("assets")

yoga_images = {
    "Yoga Pose 1": assets_path / "yoga1.png",
    "Yoga Pose 2": assets_path / "yoga2.png",
    "Stretch 1": assets_path / "stretch1.png",
    "Exercise 1": assets_path / "exercise1.png",
}

# ------------------------------
# Intro Text
# ------------------------------
st.write(
    """
### Gentle Daily Yoga to Reduce Stress & Balance Hormones  
These poses help improve blood flow, reduce bloating, and support hormonal balance.
    """
)

# ------------------------------
# Display Yoga Images
# ------------------------------
for title, img_path in yoga_images.items():
    st.subheader(f"🌿 {title}")
    if img_path.exists():
        st.image(str(img_path), use_column_width=True)
    else:
        st.warning(f"Image not found: {img_path}")

    st.markdown("---")

