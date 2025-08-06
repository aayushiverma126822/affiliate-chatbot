import streamlit as st

st.title("📝 Feedback")

if not st.session_state.get("logged_in", False):
    st.warning("Please log in first.")
    st.stop()

feedback = st.text_area("What did you think of the chatbot?")
if st.button("Submit Feedback"):
    st.success("Thanks for your feedback!")
