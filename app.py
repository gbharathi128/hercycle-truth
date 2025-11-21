import streamlit as st
from graph import graph
import os
from dotenv import load_dotenv
load_dotenv()

# Page config
st.set_page_config(page_title="HerCycle Companion ♀️", page_icon="💕", layout="centered")

# Light/Dark mode + Pink theme
st.markdown("""
<style>
    .css-1d391kg {padding-top: 1rem; padding-bottom: 3rem;}
    .css-1v0mbdj {font-family: 'Georgia', serif;}
    .stButton>button {background-color: #FF69B4; color: white; border-radius: 20px;}
    .stTextInput>div>div>input {border-radius: 20px;}
</style>
""", unsafe_allow_html=True)

# Sidebar menu
st.sidebar.title("💕 HerCycle Companion")
page = st.sidebar.radio("Go to", [
    "🏠 Home & Chat",
    "🍎 Diet Plan",
    "🧘 Yoga & Exercise",
    "✅ Daily Goals & Reminders"
])

if page == "🏠 Home & Chat":
    st.title("💕 HerCycle Truth – Your PCOS Sister")
    st.markdown("Ask me anything about PCOS, symptoms, fertility, myths, or just talk ♡")
    
    if "messages" not in st.session_state:
        st.session_state.messages = []

    for msg in st.session_state.messages:
        with st.chat_message(msg["role"]):
            st.markdown(msg["content"])

    if prompt := st.chat_input("How can I support you today?"):
        st.session_state.messages.append({"role": "user", "content": prompt})
        with st.chat_message("user"):
            st.markdown(prompt)
        with st.chat_message("assistant"):
            with st.spinner("Thinking with love..."):
                response = graph.invoke({"messages": [("human", prompt)]}, config={"configurable": {"thread_id": "1"}})
                answer = response["messages"][-1].content
                st.markdown(answer)
                st.session_state.messages.append({"role": "assistant", "content": answer})

elif page == "🍎 Diet Plan":
    st.header("🍎 Your Weekly PCOS-Friendly Diet Plan")
    st.write("Anti-inflammatory, low-GI, balanced meals")
    # Simple weekly view
    days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    selected = st.select_slider("Choose day", options=days)
    st.success(f"**{selected} Meal Ideas** (low GI, high protein, healthy fats):\n\n"
               "• Breakfast: Oats with berries & almonds\n"
               "• Lunch: Grilled chicken + quinoa + veggies\n"
               "• Snack: Greek yogurt + cinnamon\n"
               "• Dinner: Salmon + sweet potato + greens")

elif page == "🧘 Yoga & Exercise":
    st.header("🧘 Yoga & Exercise for PCOS")
    st.image("https://imgur.com/a/pcos-yoga-poses.jpg")  # I'll give real link
    st.write("• Child's Pose – reduces stress\n"
             "• Cobra Pose – improves insulin sensitivity\n"
             "• Butterfly Pose – helps ovulation\n"
             "• 30-min brisk walk daily")

elif page == "✅ Daily Goals & Reminders":
    st.header("✅ Daily Goals Tracker")
    col1, col2, col3 = st.columns(3)
    with col1:
        st.checkbox("Drink 3L water", key="water")
    with col2:
        st.checkbox("30 min movement", key="move")
    with col3:
        st.checkbox("Took supplements", key="supp")
    st.success("You're doing amazing today! Keep going ♡")

st.sidebar.markdown("---")
st.sidebar.markdown("Made with love for every woman with PCOS ♀️")
