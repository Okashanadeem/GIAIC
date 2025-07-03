import streamlit as st
import asyncio
from openai import Runner
from agent import planner_agent
from context import UserSessionContext

st.set_page_config(page_title="Health & Wellness Planner", page_icon="💪")
st.title("🧠 AI Health & Wellness Planner")
st.write("Talk to your AI health coach and get personalized wellness plans.")

user_input = st.chat_input("Say something like 'I want to lose 5kg in 2 months'")

if "chat" not in st.session_state:
    st.session_state.chat = []

if user_input:
    context = UserSessionContext(name="User", uid=1)
    st.session_state.chat.append(("You", user_input))

    with st.spinner("Thinking..."):
        steps = []

        async def run_agent():
            async for step in Runner.stream(starting_agent=planner_agent, input=user_input, context=context):
                steps.append(step.pretty_output)

        asyncio.run(run_agent())

        for response in steps:
            st.session_state.chat.append(("Agent", response))

for sender, message in st.session_state.chat:
    st.chat_message(sender).write(message)
