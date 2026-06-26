import streamlit as st
from google import genai

st.set_page_config(page_title="WolfAI Assistant", layout="centered", page_icon="🐺")

# Wolf-themed background + styling
st.markdown(
    """
    <style>
    .stApp {
        background: linear-gradient(135deg, #0f0c29 0%, #302b63 50%, #24243e 100%);
    }
    h1 {
        color: #E5E5E5;
        text-align: center;
        font-weight: 800;
        text-shadow: 0 0 12px rgba(180,180,255,0.5);
    }
    p {
        text-align: center;
        font-size: 18px;
        color: #B8B8D1;
    }
    .stTextInput input {
        border-radius: 10px;
        border: 2px solid #6B6B9C;
        background-color: #1A1A2E;
        color: #FFFFFF;
    }
    .stButton button {
        background-color: #4A4A7A;
        color: #FFFFFF;
        border: 1px solid #8888C0;
        border-radius: 10px;
        font-weight: 600;
    }
    .stButton button:hover {
        background-color: #6B6B9C;
        color: #FFFFFF;
        box-shadow: 0 0 10px rgba(150,150,255,0.6);
    }
    .stMarkdown, .stWrite {
        color: #E5E5E5;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

st.markdown(
    """
    <h1>🐺 <span style='color:#9D9DFF;'>Wolf</span>AI Assistant</h1>
    <p>Ask any question — howl your way to an answer.</p>
    """,
    unsafe_allow_html=True,
)

robo = genai.Client(api_key=st.secrets["API_KEY"])
mychat = robo.chats.create(model="gemini-flash-lite-latest")

# Placeholder for the response
response_placeholder = st.empty()

question = st.text_input("", placeholder="🐾 Enter your question here...")

col1, col2, col3 = st.columns([1, 1, 2])
with col3:
    send = st.button("🐺 GO")

if send:
    response = mychat.send_message(question)
    response_placeholder.write(response.text)
