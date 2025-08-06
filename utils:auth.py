import streamlit as st

def signup():
    st.subheader("Sign Up")
    new_user = st.text_input("Username")
    new_password = st.text_input("Password", type="password")
    if st.button("Create Account"):
        st.success("Account created. Please log in.")
        st.session_state["user_db"][new_user] = new_password

def login():
    st.subheader("Login")
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")
    if st.button("Login"):
        if st.session_state["user_db"].get(username) == password:
            st.session_state["logged_in"] = True
            st.session_state["username"] = username
        else:
            st.error("Invalid credentials")
