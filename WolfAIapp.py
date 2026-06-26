import streamlit as st
from google import genai
import os

st.set_page_config(page_title="JAI AI Assistant", layout="centered")

# Colourful background + styling
st.markdown(
    """
    <style>
    .stApp {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 50%, #f093fb 100%);
    }
    h1 {
        color: #1E3A8A;
        text-align: center;
        font-weight: 800;
    }
    p {
        text-align: center;
        font-size: 18px;
        color: #FFFFFF;
    }
    .stTextInput input {
        border-radius: 10px;
        border: 2px solid #1E3A8A;
    }
    .stButton button {
        background-color: #1E3A8A;
        color: white;
        border-radius: 10px;
        font-weight: 600;
    }
    .stButton button:hover {
        background-color: #2563EB;
        color: white;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

st.markdown(
    """
    <h1><span style='color:#1E3A8A;'>j-AI</span> Assistant</h1>
    <p>Ask any question.</p>
    """,
    unsafe_allow_html=True,
)

robo = genai.Client(api_key=st.secrets["API_KEY"])
mychat = robo.chats.create(model="gemini-flash-lite-latest")

# Placeholder for the response
response_placeholder = st.empty()

question = st.text_input("", placeholder="Enter your question here...")

col1, col2, col3 = st.columns([1, 1, 2])

with col3:
    send = st.button("GO")

if send:
    response = mychat.send_message(question)
    response_placeholder.write(response.text)
