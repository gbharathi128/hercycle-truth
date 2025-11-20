# app.py
import streamlit as st
from datetime import datetime
import json

# Import project modules
from graph import invoke
from diet_plan import generate_weekly_diet
import reminder

st.set_page_config(page_title="HerCycle Truth", layout="wide", page_icon="💗")
st.markdown("""
<style>
.chat-user {background-color:#e6f7ff; padding:10px; border-radius:8px;}
.chat-bot {background-color:#fff0f6; padding:10px; border-radius:8px;}
.container {max-width:1000px; margin:auto;}
</style>
""", unsafe_allow_html=True)

st.title("💗 HerCycle Truth — PCOS Support Companion")

tab1, tab2, tab3 = st.tabs(["Chatbot", "Weekly Diet Plan", "Reminders"])

# ---------------- Tab 1: Chatbot ----------------
with tab1:
    st.header("Ask a question (educational, non-medical)")
    query = st.text_area("Type your question here", height=120, key="chat_input")
    col1, col2 = st.columns([0.8, 0.2])
    with col2:
        send = st.button("Send")

    if send and query.strip():
        # Call backend
        result = invoke({"messages": [{"role": "user", "content": query}]})
        # extract text safely
        msg = result["messages"][-1]
        # If Gemini response object, try the parts attr; otherwise handle dict
        text = None
        try:
            # gemini-like object
            text = msg.candidates[0].content.parts[0].text  # may raise
        except Exception:
            # expect dict with 'content'
            text = msg.get("content") if isinstance(msg, dict) else str(msg)
        st.markdown("**Response:**")
        st.write(text)

    st.info("Tip: Ask about symptoms, diet ideas, myths or request 'Give me a weekly diet plan'.")

# ---------------- Tab 2: Diet Plan ----------------
with tab2:
    st.header("Personalized Weekly Diet Plan")
    goal = st.selectbox("Your goal", ["balanced", "weight_loss", "energy"])
    if st.button("Generate weekly diet plan"):
        plan = generate_weekly_diet(goal=goal)
        for day, meals in plan.items():
            st.subheader(day)
            st.write(f"**Breakfast:** {meals['Breakfast']}")
            st.write(f"**Lunch:** {meals['Lunch']}")
            st.write(f"**Dinner:** {meals['Dinner']}")

# ---------------- Tab 3: Reminders ----------------
with tab3:
    st.header("Reminders")
    st.subheader("Add a reminder")
    task = st.text_input("Reminder text")
    time = st.time_input("Time (local)")
    if st.button("Add reminder"):
        if not task.strip():
            st.warning("Please enter a reminder text.")
        else:
            tstr = time.strftime("%H:%M")
            reminder.add_reminder(task, tstr)
            st.success("Reminder added!")

    st.subheader("Your reminders")
    rems = reminder.load_reminders()
    if rems:
        for i, r in enumerate(rems):
            st.write(f"- **{r['task']}** at {r['time']} (created {r.get('created_at','')})")
            if st.button(f"Remove {i}", key=f"rm_{i}"):
                reminder.remove_reminder(i)
                st.experimental_rerun()
    else:
        st.write("No reminders yet.")
