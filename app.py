# app.py
import streamlit as st
from datetime import datetime
import base64, io
import json

from diet_plan import generate_weekly_diet
import reminder
from graph import invoke

# --------- Page config ----------
st.set_page_config(page_title="HerCycle Truth", layout="wide", page_icon="💗")

# --------- Theme CSS (Peach + Coral, glassmorphism) ----------
st.markdown("""
<style>
:root{
  --peach:#FFD6C2;
  --coral:#FF6B6B;
  --card:#fff7f5;
  --muted:#6b6b6b;
}
body { background: linear-gradient(180deg, #fff8f6 0%, #fff3f1 100%); }
.header {
  text-align:center;
  padding:18px;
  border-radius: 12px;
  margin-bottom: 18px;
}
.app-title { font-family: 'Poppins', sans-serif; color: #d64b63; font-size:28px; font-weight:700; }
.subtitle { color: var(--muted); margin-top:-8px; }

.card {
  background: rgba(255,255,255,0.8);
  border-radius: 14px;
  padding: 16px;
  box-shadow: 0 6px 24px rgba(255,107,107,0.08);
  border: 1px solid rgba(255,107,107,0.06);
}

.small { font-size:13px; color:var(--muted); }
.diet-card {
  border-radius:16px;
  padding:12px;
  background: linear-gradient(180deg, rgba(255,246,241,1), rgba(255,238,233,0.9));
  border: 1px solid rgba(255,107,107,0.06);
  box-shadow: 0 8px 30px rgba(255,107,107,0.06);
}
.diet-day { color:#d64b63; font-weight:700; font-size:18px; margin-bottom:6px; }
.meal { margin:6px 0; padding:8px; border-radius:10px; background:rgba(255,255,255,0.9); }
.swap-btn { background: transparent; border: 1px dashed rgba(214,75,99,0.25); border-radius:8px; padding:6px 10px; color:#d64b63; }
@media (max-width: 600px) {
  .desktop-only { display:none; }
}
</style>
""", unsafe_allow_html=True)

# --------- Header ----------
st.markdown('<div class="header">', unsafe_allow_html=True)
st.markdown('<div class="app-title">💗 HerCycle Truth</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle small">Your gentle PCOS companion — diet plans, reminders & supportive chat</div>', unsafe_allow_html=True)
st.markdown('</div>', unsafe_allow_html=True)

# --------- Layout: left (main) / right (sidebar) ----------
col_main, col_side = st.columns([2.4,1])

with col_main:
    # Tabs for core features
    tabs = st.tabs(["Chat", "Diet Plan", "My Reminders", "My Profile"])
    # ----- Tab: Chat -----
    with tabs[0]:
        st.markdown('<div class="card">', unsafe_allow_html=True)
        st.markdown("### 💬 Ask HerCycle anything (educational, non-medical)")
        user_q = st.text_area("Type your question...", key="chat_input", height=110, placeholder="e.g., What foods help with PCOS?")
        if st.button("Send 💗"):
            if user_q.strip() == "":
                st.warning("Please type a question to ask.")
            else:
                res = invoke({"messages":[{"role":"user","content":user_q}]})
                msg = res["messages"][-1]
                # extract text safely
                try:
                    text = msg.candidates[0].content.parts[0].text
                except Exception:
                    text = msg.get("content", str(msg))
                st.markdown(f'<div class="card"><strong>You:</strong> {user_q}</div>', unsafe_allow_html=True)
                st.markdown(f'<div class="card" style="margin-top:10px;"><strong>HerCycle:</strong> {text}</div>', unsafe_allow_html=True)
        st.markdown('</div>', unsafe_allow_html=True)

    # ----- Tab: Diet Plan -----
    with tabs[1]:
        st.markdown('<div class="card">', unsafe_allow_html=True)
        st.markdown("### 🥗 Personalized Weekly Diet")
        col1, col2 = st.columns([2,1])
        with col1:
            goal = st.selectbox("Goal", ["balanced","weight_loss","energy"])
            preference = st.selectbox("Preference", ["veg","vegan","nonveg"])
            if st.button("Generate Beautiful Weekly Plan"):
                plan = generate_weekly_diet(goal=goal, preference=preference)
                st.markdown('<div style="margin-top:12px"></div>', unsafe_allow_html=True)
                # show grid of cards (2 cols on desktop)
                days = list(plan.items())
                chunk = [days[i:i+2] for i in range(0,len(days),2)]
                for row in chunk:
                    cols = st.columns(len(row))
                    for c, (day, meals) in zip(cols, row):
                        with c:
                            st.markdown('<div class="diet-card">', unsafe_allow_html=True)
                            st.markdown(f'<div class="diet-day">🌸 {day}</div>', unsafe_allow_html=True)
                            # placeholder inline aesthetic image (SVG gradient) to avoid external images
                            svg = f"""<svg width="100%" height="120" viewBox="0 0 400 120" xmlns="http://www.w3.org/2000/svg">
                            <defs><linearGradient id="g" x1="0" x2="1"><stop offset="0" stop-color="#FFD6C2"/><stop offset="1" stop-color="#FFB3A7"/></linearGradient></defs>
                            <rect rx="12" y="0" x="0" width="100%" height="120" fill="url(#g)"/>
                            <text x="20" y="68" font-size="18" fill="#7a2a2a" font-family="Poppins">Aesthetic Meal</text>
                            </svg>"""
                            st.markdown(svg, unsafe_allow_html=True)
                            st.markdown(f'<div class="meal"><strong>🍳 Breakfast:</strong> {meals["Breakfast"]}</div>', unsafe_allow_html=True)
                            st.markdown(f'<div class="meal"><strong>🥗 Lunch:</strong> {meals["Lunch"]}</div>', unsafe_allow_html=True)
                            st.markdown(f'<div class="meal"><strong>🌙 Dinner:</strong> {meals["Dinner"]}</div>', unsafe_allow_html=True)
                            # swap and download small controls
                            if st.button(f"Swap meal (day:{day})", key=f"swap_{day}"):
                                st.info(f"Swap feature: you can swap any meal (placeholder).")
                            if st.button(f"Download {day} PDF", key=f"pdf_{day}"):
                                # generate simple text PDF
                                from reportlab.lib.pagesizes import letter
                                from reportlab.pdfgen import canvas
                                buffer = io.BytesIO()
                                c = canvas.Canvas(buffer, pagesize=letter)
                                c.setFont("Helvetica-Bold", 14)
                                c.drawString(40, 750, f"{day} - HerCycle Truth Diet Plan")
                                c.setFont("Helvetica", 12)
                                c.drawString(40, 720, f"Breakfast: {meals['Breakfast']}")
                                c.drawString(40, 700, f"Lunch: {meals['Lunch']}")
                                c.drawString(40, 680, f"Dinner: {meals['Dinner']}")
                                c.save()
                                buffer.seek(0)
                                st.download_button(f"Download {day} PDF", data=buffer, file_name=f"{day}_diet.pdf", mime="application/pdf")
                            st.markdown('</div>', unsafe_allow_html=True)
        with col2:
            st.markdown('<div class="card small">', unsafe_allow_html=True)
            st.write("Tips")
            st.write("- Keep portions balanced")
            st.write("- Prefer whole grains")
            st.write("- Stay hydrated and get protein each meal")
            st.markdown('</div>', unsafe_allow_html=True)
        st.markdown('</div>', unsafe_allow_html=True)

    # ----- Tab: Reminders -----
    with tabs[2]:
        st.markdown('<div class="card">', unsafe_allow_html=True)
        st.markdown("### ⏰ My Reminders")
        task = st.text_input("Reminder text", key="task")
        time_input = st.time_input("Time", key="remtime")
        if st.button("Add Reminder"):
            if not task.strip():
                st.warning("Add reminder text.")
            else:
                reminder.add_reminder(task, time_input.strftime("%H:%M"))
                st.success("Reminder saved.")
                st.experimental_rerun()
        st.markdown("#### Upcoming Reminders")
        rems = reminder.load_reminders()
        if rems:
            for i, r in enumerate(rems):
                st.markdown(f"- **{r['task']}** at {r['time']} (created {r.get('created_at','')})")
                if st.button(f"Remove {i}", key=f"rem_rm_{i}"):
                    reminder.remove_reminder(i)
                    st.experimental_rerun()
        else:
            st.write("No reminders yet.")
        st.markdown('</div>', unsafe_allow_html=True)

    # ----- Tab: Profile -----
    with tabs[3]:
        st.markdown('<div class="card">', unsafe_allow_html=True)
        st.markdown("### ✨ Your Profile (optional)")
        st.write("This is a placeholder to add user details like age, allergies, cycle length.")
        st.markdown('</div>', unsafe_allow_html=True)

with col_side:
    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.markdown("### Quick Actions")
    if st.button("Generate Balanced Plan (quick)"):
        plan = generate_weekly_diet()
        st.success("Plan generated — see Diet tab")
    st.markdown("---")
    st.markdown("### Wellness tips")
    st.write("- Short daily walks")
    st.write("- Balanced meals")
    st.write("- Sleep 7-8 hours")
    st.markdown('</div>', unsafe_allow_html=True)
