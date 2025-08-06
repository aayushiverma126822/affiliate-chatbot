import streamlit as st
from chatbot.hf_chat import get_bot_response

if not st.session_state.get("logged_in", False):
    st.warning("Please log in first.")
    st.stop()

st.title("💬 GenAI Affiliate Chatbot")

if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

user_input = st.text_input("You:", "")

if st.button("Send"):
    if user_input:
        bot_reply = get_bot_response(user_input)
        st.session_state.chat_history.append(("You", user_input))
        st.session_state.chat_history.append(("Bot", bot_reply))

for role, msg in reversed(st.session_state.chat_history):
    st.markdown(f"**{role}:** {msg}")
