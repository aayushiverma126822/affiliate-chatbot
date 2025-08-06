import streamlit as st
from utils.auth import login, signup

if "logged_in" not in st.session_state:
    st.session_state["logged_in"] = False
    st.session_state["user_db"] = {}

st.title("🔐 Welcome to GenAI Affiliate Chatbot")

menu = ["Login", "Sign Up"]
choice = st.selectbox("Choose an option", menu)

if choice == "Login":
    login()
else:
    signup()
