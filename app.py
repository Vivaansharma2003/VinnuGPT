import os
import streamlit as st
from groq import Groq
from dotenv import load_dotenv

# Load API key from .env
load_dotenv()
api_key = os.getenv("GROQ_API_KEY")
client = Groq(api_key=api_key)

# Page Setup
st.set_page_config(page_title="💖 VinnuGPT - Naughty Chat", page_icon="💖", layout="centered")

# Inject CSS for style
st.markdown("""
    <style>
    .stChatMessage.user {background-color: #f0f0f0; border-radius: 10px; padding: 8px; margin: 5px 0;}
    .stChatMessage.assistant {background-color: #ffe6f0; border-radius: 10px; padding: 8px; margin: 5px 0;}
    .vinnu-img {
        display: block;
        margin-left: auto;
        margin-right: auto;
        width: 150px;
        border-radius: 50%;
        border: 4px solid #ff69b4;
    }
    </style>
""", unsafe_allow_html=True)

# Funny Vinayak image at top
st.image("./vinnu.jpg", use_container_width=False, width=150, caption="😈 VinnuGPT Mode On 😈")

# Title + description
st.title("💖 VinnuGPT")
st.markdown("Your *naughty, oversmart, heighted hero from Bengaluru* 😏")

# Gender mode selector
user_gender = st.selectbox("You are chatting as a:", ["👦 Boy", "👧 Girl"], index=0)

# Create personality prompt based on gender
if "chat_history" not in st.session_state:
    if "Boy" in user_gender:
        system_prompt = (
            "You are VinnuGPT, an 18-year-old from Bengaluru, 6'7 tall. "
            "You're naughty, oversmart, and love trolling other boys. "
            "Your style is full of sarcastic banter, cheap jokes, and teasing. "
            "You're super irritating, say trash things, and always try to one-up boys. "
            "You repeatedly use lines like 'dekhte hai bhai' and 'ek ek plate laga de bhai'. "
            "Answer in Hinglish."
        )
    else:
        system_prompt = (
            "You are VinnuGPT, an 18-year-old from Bengaluru, 6'7 tall. "
            "You're a shameless flirt and believe every girl is crazy about you. "
            "You throw cheesy pickup lines, show oversmart attitude, and act like a full-time rizz lord. "
            "Talk in Hinglish and assume every girl likes you."
        )

    st.session_state.chat_history = [{"role": "system", "content": system_prompt}]

# Chat Input
user_input = st.chat_input("Say something to VinnuGPT...")

if user_input:
    st.session_state.chat_history.append({"role": "user", "content": user_input})

    with st.spinner("VinnuGPT is preparing a scandalous reply... 😏"):
        response = client.chat.completions.create(
            model="meta-llama/llama-4-scout-17b-16e-instruct",
            messages=st.session_state.chat_history,
            temperature=0.95,
            max_completion_tokens=300
        )

    message = response.choices[0].message.content
    st.session_state.chat_history.append({"role": "assistant", "content": message})

# Display chat history
for msg in st.session_state.chat_history[1:]:
    role = "user" if msg["role"] == "user" else "assistant"
    with st.chat_message(role):
        st.markdown(msg["content"])
