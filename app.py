import streamlit as st
import requests
import json


def get_bot_response(user_input):
    # Normalize input
    user_input = user_input.lower().strip()

    # Static response for creatives in affiliate marketing
    if "why are creatives crucial in affiliate marketing" in user_input:
        return (
            "Creatives are the heart of affiliate marketing campaigns because they directly "
            "influence how a product or service is perceived by potential customers. They include "
            "visuals, videos, banners, ad copies, and other engaging content designed to capture "
            "attention and drive action. In a highly competitive digital space, good creatives help "
            "affiliates stand out, improve click-through rates (CTR), and boost conversions. They "
            "also ensure consistent branding across channels and enhance emotional connection with "
            "the audience, which is essential for long-term loyalty and trust. Without compelling "
            "creatives, even the best offers can go unnoticed."
        )

    # Add more rules or route to LLM here
    return "Sorry, I didn't understand that. Could you please rephrase?"


# --------------------- Simple In-Memory User Store ---------------------
users = {
    "demo@example.com": "password123"
}

# --------------------- Hugging Face Model Config ---------------------
API_URL = "https://api-inference.huggingface.co/models/google/flan-t5-large"
API_KEY = "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"  # Replace with your valid key
headers = {"Authorization": f"Bearer {API_KEY}"}

# --------------------- Chatbot Function ---------------------
def query_huggingface(prompt):
    payload = {"inputs": prompt}
    response = get_bot_response(user_input)

    if response.status_code == 200:
        return response.json()[0]['generated_text']
    else:
        return f"Error: {response.status_code} - {response.text}"

# --------------------- Login/Signup Logic ---------------------
def login_page():
    st.title("Login")
    email = st.text_input("Email")
    password = st.text_input("Password", type="password")
    if st.button("Login"):
        if email in users and users[email] == password:
            st.session_state['logged_in'] = True
            st.session_state['email'] = email
        else:
            st.error("Invalid email or password.")

    if st.button("Go to Signup"):
        st.session_state['page'] = 'signup'

def signup_page():
    st.title("Signup")
    email = st.text_input("Email")
    password = st.text_input("Password", type="password")
    if st.button("Signup"):
        if email in users:
            st.error("User already exists.")
        else:
            users[email] = password
            st.success("Signup successful. Please log in.")
            st.session_state['page'] = 'login'

    if st.button("Back to Login"):
        st.session_state['page'] = 'login'

# --------------------- Chat Page ---------------------
def chat_page():
    st.title("Affiliate Chatbot")

    user_input = st.text_input("You:", key="user_input")
    if st.button("Send"):
        if user_input:
            st.session_state["chat_history"].append(("You", user_input))
            response = query_huggingface(user_input)
            st.session_state["chat_history"].append(("Bot", response))

    for speaker, message in reversed(st.session_state["chat_history"]):
        st.markdown(f"**{speaker}**: {message}")

    if st.button("Logout"):
        st.session_state.clear()
        st.session_state['page'] = 'login'

# --------------------- Main App ---------------------
def main():
    if 'logged_in' not in st.session_state:
        st.session_state['logged_in'] = False
    if 'page' not in st.session_state:
        st.session_state['page'] = 'login'

    if st.session_state['logged_in']:
        chat_page()
    elif st.session_state['page'] == 'login':
        login_page()
    elif st.session_state['page'] == 'signup':
        signup_page()

if __name__ == "__main__":
    main()
