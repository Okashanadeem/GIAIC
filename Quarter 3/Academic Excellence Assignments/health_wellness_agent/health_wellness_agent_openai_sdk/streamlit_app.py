import streamlit as st
import asyncio
from agent import HealthWellness
from context import UserSessionContext
from agents import Runner
from openai.types.responses import ResponseTextDeltaEvent
import random

st.set_page_config(page_title="🧠 Health & Wellness Chat", layout="centered")

# ----------------- Custom CSS Styling -------------------
st.markdown("""
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;600;700&display=swap');

        html, body, [class*="css"] {
            font-family: 'Inter', sans-serif;
            background-color: #f7f8fa;
        }

        .title {
            font-size: 36px;
            font-weight: 700;
            text-align: center;
            margin-bottom: 20px;
            color: #0072ff;
        }

        .subtitle {
            font-size: 16px;
            text-align: center;
            color: #555;
            margin-bottom: 25px;
        }

        .chat-container {
            max-height: 400px;
            overflow-y: auto;
            padding: 15px;
            background-color: #ffffff;
            border-radius: 12px;
            border: 1px solid #e0e0e0;
            margin-bottom: 20px;
        }

        .chat-message {
            margin-bottom: 14px;
            display: flex;
            flex-direction: column;
        }

        .user .bubble {
            background: #0072ff;
            color: white;
            align-self: flex-end;
            border-radius: 15px 15px 0 15px;
            padding: 10px 15px;
            max-width: 70%;
        }

        .assistant .bubble {
            background: #f0f0f0;
            color: #333;
            align-self: flex-start;
            border-radius: 15px 15px 15px 0;
            padding: 10px 15px;
            max-width: 70%;
        }

        .name {
            font-size: 12px;
            color: #888;
            margin-bottom: 3px;
        }

        .footer {
            text-align: center;
            margin-top: 40px;
            font-size: 13px;
            color: #999;
        }
    </style>
""", unsafe_allow_html=True)

# ----------------- Session State -------------------
if "username" not in st.session_state:
    st.session_state.username = ""
if "messages" not in st.session_state:
    st.session_state.messages = []
if "output_text" not in st.session_state:
    st.session_state.output_text = ""

# ----------------- Set Username -------------------
def set_username():
    if st.session_state.username_input.strip():
        st.session_state.username = st.session_state.username_input.strip()

# ----------------- Ask for Username -------------------
if not st.session_state.username:
    st.markdown("<div class='title'>🧠 Health & Wellness Chat</div>", unsafe_allow_html=True)
    st.markdown("<div class='subtitle'>👋 Welcome! Please enter your name to begin:</div>", unsafe_allow_html=True)
    st.text_input("Your Name:", key="username_input", on_change=set_username)
    st.stop()

# ----------------- Greeting Header -------------------
st.markdown(f"<div class='title'>Hello, {st.session_state.username}! 🌿</div>", unsafe_allow_html=True)
st.markdown("<div class='subtitle'>Ask about fitness, diet, injury recovery, or personal health plans:</div>", unsafe_allow_html=True)

# ----------------- Chat History -------------------
with st.container():
    st.markdown("<div class='chat-container'>", unsafe_allow_html=True)
    for msg in st.session_state.messages:
        st.markdown(f"""
            <div class='chat-message user'>
                <div class='name'>{st.session_state.username}</div>
                <div class='bubble'>{msg['user']}</div>
            </div>
            <div class='chat-message assistant'>
                <div class='name'>AI Assistant</div>
                <div class='bubble'>{msg['assistant']}</div>
            </div>
        """, unsafe_allow_html=True)
    st.markdown("</div>", unsafe_allow_html=True)

# ----------------- Input Form -------------------
with st.form("chat_form", clear_on_submit=True):
    user_input = st.text_input("💬 Type your message here:", placeholder="e.g. What’s a good post-workout meal?")
    send = st.form_submit_button("🚀 Send")

    if send and user_input.strip():
        st.session_state.latest_input = user_input.strip()

# ----------------- Chat Handler -------------------
async def talk_to_agent():
    uid = random.randint(1000, 9999)
    ctx = UserSessionContext(name=st.session_state.username, uid=uid)
    result = Runner.run_streamed(
        starting_agent=HealthWellness,
        input=st.session_state.latest_input,
        context=ctx
    )

    output_text = ""
    async for event in result.stream_events():
        if event.type == "raw_response_event" and isinstance(event.data, ResponseTextDeltaEvent):
            token = event.data.delta
            output_text += token
            st.session_state.output_text = output_text

    st.session_state.messages.append({
        "user": st.session_state.latest_input,
        "assistant": output_text
    })
    st.session_state.output_text = ""
    st.rerun()

if "latest_input" in st.session_state and st.session_state.latest_input:
    asyncio.run(talk_to_agent())
    st.session_state.latest_input = ""

# ----------------- Footer -------------------
st.markdown("""
    <div class='footer'>
        Built with ❤️ by <strong>Okasha Nadeem</strong><br>
        © 2025 Health & Wellness Chat
    </div>
""", unsafe_allow_html=True)
