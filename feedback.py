import streamlit as st

def feedback_page():
    st.title("📝 Feedback")
    feedback = st.text_area("Leave your feedback here:")
    if st.button("Submit"):
        if feedback:
            st.success("✅ Thanks for your feedback!")
        else:
            st.warning("Please enter some feedback before submitting.")
