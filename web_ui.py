import streamlit as st
import requests

# API Endpoint (Chatbot)
API_URL = "http://localhost:8000/chat"

# Streamlit UI
st.title("🛒 AI Customer Support Chatbot")

# User input field
user_input = st.text_input("Ask a question:", "")

# If user submits a query
if st.button("Send"):
    if user_input:
        # Send request to FastAPI chatbot
        response = requests.post(API_URL, json={"message": user_input})
        
        if response.status_code == 200:
            chatbot_response = response.json().get("response", "No response from chatbot.")
            st.text_area("Chatbot:", value=chatbot_response, height=100)
        else:
            st.error("Error connecting to chatbot API!")
    else:
        st.warning("Please enter a question before clicking Send.")
