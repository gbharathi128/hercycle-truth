import streamlit as st
from streamlit_chat import message

# Page settings
st.set_page_config(
    page_title="Chat With AI Agent",
    page_icon="💗",
    layout="wide"
)

# ------- Custom Aesthetic CSS -------
st.markdown("""
<style>
body {
    background: linear-gradient(135deg, #ffe6ec 0%, #fff5f8 100%);
}
.chat-container {
    background-color: #ffffffd9;
    padding: 20px;
    border-radius: 20px;
    box-shadow: 0 4px 20px rgba(255, 120, 155, 0.15);
}
h1 {
    font-family: 'Segoe UI', sans-serif;
    color: #ff4d6d;
    font-weight: 800;
}
</style>
""", unsafe_allow_html=True)

# Chat History
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

# --------- Title ---------
st.markdown("<h1 style='text-align:center;'>💗 Chat With Your AI Agent</h1>",
            unsafe_allow_html=True)
st.write("")

# Place chat inside container
with st.container():
    st.markdown('<div class="chat-container">', unsafe_allow_html=True)

    # Input area
    user_input = st.text_input("💬 Type your message here…")

    # Send button
    if st.button("Send 💗"):
        if user_input.strip() != "":
            st.session_state.chat_history.append(("user", user_input))

            # Basic AI response
            ai_reply = (
                "✨ I'm always here for you! 💗\n"
                "You said: **" + user_input + "**"
            )
            st.session_state.chat_history.append(("ai", ai_reply))

    # Divider
    st.write("----")

    # Chat display
    for sender, msg in st.session_state.chat_history:
        if sender == "user":
            message(msg, is_user=True, key=msg)
        else:
            message(msg, key=msg+"ai")

    st.markdown("</div>", unsafe_allow_html=True)

# Footer
st.write("---")
st.caption("🌸 Your soft & aesthetic wellness companion AI 💗")

