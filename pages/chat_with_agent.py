import streamlit as st
from tools.pcos_tools import ask_pcos_agent

# Page Config
st.set_page_config(page_title="Chat With HerCycle Agent", layout="wide")

# Title Section
st.markdown("""
    <h1 style='text-align:center; color:#d63384;'>💗 Chat With Your PCOS Companion</h1>
    <p style='text-align:center; color:#444;'>Ask anything about diet, periods, hormones, workouts, cravings, mood, skin, hair fall or lifestyle.</p>
""", unsafe_allow_html=True)

# Layout
left, right = st.columns([2, 3])

with left:
    st.image("assets/chat.png", use_column_width=True)

with right:
    st.markdown("""
        <div style='padding:15px; background:#ffe6f2; border-radius:20px;'>
            <b style='color:#d63384;'>✨ Your comfort zone:</b>  
            Ask with no fear. Your agent understands PCOS deeply and replies softly like a friend.  
        </div>
    """, unsafe_allow_html=True)

st.markdown("---")

# Chat Box
st.markdown("<h3 style='color:#d63384;'>💬 Ask your question</h3>", unsafe_allow_html=True)
user_input = st.text_area("", placeholder="Type here... (Example: What should I eat during periods?)")

if st.button("Ask Agent 💗"):
    if user_input.strip() == "":
        st.warning("Please type something to ask.")
    else:
        with st.spinner("Thinking with love... 💗"):
            reply = ask_pcos_agent(user_input)
        st.markdown("""
            <div style='background:#fff0f7; padding:15px; border-radius:15px; margin-top:15px;'>
                <b>HerCycle Agent 💗:</b><br>
            </div>
        """, unsafe_allow_html=True)
        st.success(reply)

# Footer
st.markdown("<br><hr>", unsafe_allow_html=True)
st.markdown("<p style='text-align:center; color:#999;'>Made with 💗 for every girl healing PCOS.</p>", unsafe_allow_html=True)
