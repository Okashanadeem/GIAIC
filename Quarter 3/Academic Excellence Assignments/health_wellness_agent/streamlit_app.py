import streamlit as st
import asyncio
import json
from datetime import datetime, timedelta
from typing import Dict, List, Optional
import pandas as pd
import threading
import time

# Import your existing modules
from main import Runner
from context import UserSessionContext
from agent import planner_agent

# Page configuration
st.set_page_config(
    page_title="Health & Wellness Planner Agent",
    page_icon="🏃‍♀️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for better styling
st.markdown("""
<style>
    .main-header {
        font-size: 2.5rem;
        font-weight: bold;
        color: #2E8B57;
        text-align: center;
        margin-bottom: 2rem;
    }
    .sub-header {
        font-size: 1.5rem;
        color: #4682B4;
        margin-bottom: 1rem;
    }
    .metric-card {
        background-color: #f0f8ff;
        padding: 1rem;
        border-radius: 0.5rem;
        border-left: 4px solid #2E8B57;
        margin-bottom: 1rem;
    }
    .chat-message {
        padding: 1rem;
        border-radius: 0.5rem;
        margin-bottom: 1rem;
    }
    .user-message {
        background-color: #e3f2fd;
        border-left: 4px solid #2196f3;
    }
    .agent-message {
        background-color: #f3e5f5;
        border-left: 4px solid #9c27b0;
    }
    .tool-message {
        background-color: #e8f5e8;
        border-left: 4px solid #4caf50;
        font-family: monospace;
        font-size: 0.9rem;
    }
    .handoff-message {
        background-color: #fff3e0;
        border-left: 4px solid #ff9800;
    }
    .progress-bar {
        background-color: #e0e0e0;
        border-radius: 10px;
        padding: 3px;
        margin: 10px 0;
    }
    .progress-fill {
        background-color: #2E8B57;
        height: 20px;
        border-radius: 8px;
        text-align: center;
        color: white;
        font-weight: bold;
    }
</style>
""", unsafe_allow_html=True)

# Initialize session state
if 'user_context' not in st.session_state:
    st.session_state.user_context = UserSessionContext(
        name="User",
        uid=1,
        goal=None,
        diet_preferences=None,
        workout_plan=None,
        meal_plan=None,
        injury_notes=None,
        handoff_logs=[],
        progress_logs=[]
    )

if 'conversation_history' not in st.session_state:
    st.session_state.conversation_history = []

if 'streaming_active' not in st.session_state:
    st.session_state.streaming_active = False

# Helper function to run async streaming
async def stream_agent_response(user_input: str, context: UserSessionContext):
    """Stream agent response and return all steps"""
    steps = []
    try:
        async for step in Runner.stream(
            starting_agent=planner_agent,
            input=user_input,
            context=context
        ):
            steps.append(step)
    except Exception as e:
        st.error(f"Error during streaming: {str(e)}")
    return steps

def run_streaming_in_thread(user_input: str, context: UserSessionContext):
    """Run async streaming in a separate thread"""
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    try:
        steps = loop.run_until_complete(stream_agent_response(user_input, context))
        return steps
    finally:
        loop.close()

# Header
st.markdown('<div class="main-header">🏃‍♀️ Health & Wellness Planner Agent</div>', unsafe_allow_html=True)
st.markdown("**Your AI-powered personal wellness assistant for fitness and nutrition planning**")

# Sidebar with user info and progress
with st.sidebar:
    st.markdown('<div class="sub-header">👤 User Profile</div>', unsafe_allow_html=True)
    
    # User basic info
    user_name = st.text_input("Your Name", value=st.session_state.user_context.name)
    if user_name != st.session_state.user_context.name:
        st.session_state.user_context.name = user_name
    
    # Current goal display
    st.markdown('<div class="sub-header">🎯 Current Goal</div>', unsafe_allow_html=True)
    if st.session_state.user_context.goal:
        goal_info = st.session_state.user_context.goal
        st.markdown(f"""
        <div class="metric-card">
            <strong>Goal:</strong> {goal_info.get('description', 'Not specified')}<br>
            <strong>Target:</strong> {goal_info.get('quantity', 'N/A')} {goal_info.get('metric', '')}<br>
            <strong>Timeline:</strong> {goal_info.get('duration', 'Not specified')}
        </div>
        """, unsafe_allow_html=True)
    else:
        st.info("No goal set yet. Start a conversation to set your wellness goals!")
    
    # Diet preferences
    st.markdown('<div class="sub-header">🥗 Diet Info</div>', unsafe_allow_html=True)
    if st.session_state.user_context.diet_preferences:
        st.markdown(f"""
        <div class="metric-card">
            <strong>Preferences:</strong> {st.session_state.user_context.diet_preferences}
        </div>
        """, unsafe_allow_html=True)
    else:
        st.info("No dietary preferences specified")
    
    # Injury notes
    if st.session_state.user_context.injury_notes:
        st.markdown('<div class="sub-header">🩹 Health Notes</div>', unsafe_allow_html=True)
        st.markdown(f"""
        <div class="metric-card">
            <strong>Notes:</strong> {st.session_state.user_context.injury_notes}
        </div>
        """, unsafe_allow_html=True)
    
    # Progress logs
    if st.session_state.user_context.progress_logs:
        st.markdown('<div class="sub-header">📈 Progress</div>', unsafe_allow_html=True)
        for log in st.session_state.user_context.progress_logs[-3:]:  # Show last 3 entries
            st.markdown(f"""
            <div class="metric-card">
                <strong>{log.get('date', 'Unknown')}:</strong><br>
                {log.get('note', 'No details')}
            </div>
            """, unsafe_allow_html=True)
    
    # Handoff logs
    if st.session_state.user_context.handoff_logs:
        st.markdown('<div class="sub-header">🔄 Agent Handoffs</div>', unsafe_allow_html=True)
        for log in st.session_state.user_context.handoff_logs[-3:]:  # Show last 3 entries
            st.markdown(f"""
            <div class="metric-card">
                {log}
            </div>
            """, unsafe_allow_html=True)
    
    # Clear conversation button
    if st.button("🗑️ Clear Conversation"):
        st.session_state.conversation_history = []
        st.session_state.user_context = UserSessionContext(
            name=user_name,
            uid=1,
            goal=None,
            diet_preferences=None,
            workout_plan=None,
            meal_plan=None,
            injury_notes=None,
            handoff_logs=[],
            progress_logs=[]
        )
        st.rerun()

# Main content area
col1, col2 = st.columns([2, 1])

with col1:
    st.markdown('<div class="sub-header">💬 Chat with Your Wellness Agent</div>', unsafe_allow_html=True)
    
    # Display conversation history
    chat_container = st.container()
    with chat_container:
        for message in st.session_state.conversation_history:
            if message['type'] == 'user':
                st.markdown(f"""
                <div class="chat-message user-message">
                    <strong>You:</strong> {message['content']}
                </div>
                """, unsafe_allow_html=True)
            elif message['type'] == 'agent':
                st.markdown(f"""
                <div class="chat-message agent-message">
                    <strong>Agent:</strong> {message['content']}
                </div>
                """, unsafe_allow_html=True)
            elif message['type'] == 'tool':
                st.markdown(f"""
                <div class="chat-message tool-message">
                    <strong>Tool ({message['tool_name']}):</strong> {message['content']}
                </div>
                """, unsafe_allow_html=True)
            elif message['type'] == 'handoff':
                st.markdown(f"""
                <div class="chat-message handoff-message">
                    <strong>Handoff to {message['agent_name']}:</strong> {message['content']}
                </div>
                """, unsafe_allow_html=True)
    
    # Chat input
    with st.form(key='chat_form', clear_on_submit=True):
        user_input = st.text_area(
            "Enter your message:",
            placeholder="Tell me about your health and wellness goals...",
            height=100,
            key="user_input"
        )
        
        col_send, col_examples = st.columns([1, 2])
        
        with col_send:
            submit_button = st.form_submit_button("Send Message", use_container_width=True)
        
        with col_examples:
            st.markdown("**Quick Examples:**")
            example_buttons = st.columns(3)
            with example_buttons[0]:
                if st.form_submit_button("🏃 Weight Loss"):
                    user_input = "I want to lose 5kg in 2 months"
                    submit_button = True
            with example_buttons[1]:
                if st.form_submit_button("🥗 Meal Plan"):
                    user_input = "I'm vegetarian and need a meal plan"
                    submit_button = True
            with example_buttons[2]:
                if st.form_submit_button("💪 Workout"):
                    user_input = "I need a beginner workout routine"
                    submit_button = True
    
    # Process user input
    if submit_button and user_input.strip():
        # Add user message to history
        st.session_state.conversation_history.append({
            'type': 'user',
            'content': user_input,
            'timestamp': datetime.now().isoformat()
        })
        
        # Show processing indicator
        with st.spinner("🤖 Agent is thinking..."):
            try:
                # Run streaming in thread
                steps = run_streaming_in_thread(user_input, st.session_state.user_context)
                
                # Process steps and update conversation
                for step in steps:
                    if hasattr(step, 'agent_name') and hasattr(step, 'content'):
                        # Agent response
                        st.session_state.conversation_history.append({
                            'type': 'agent',
                            'content': step.content,
                            'timestamp': datetime.now().isoformat()
                        })
                    elif hasattr(step, 'tool_name') and hasattr(step, 'result'):
                        # Tool execution
                        st.session_state.conversation_history.append({
                            'type': 'tool',
                            'tool_name': step.tool_name,
                            'content': str(step.result),
                            'timestamp': datetime.now().isoformat()
                        })
                    elif hasattr(step, 'handoff_to'):
                        # Agent handoff
                        st.session_state.conversation_history.append({
                            'type': 'handoff',
                            'agent_name': step.handoff_to,
                            'content': f"Transferring to {step.handoff_to}",
                            'timestamp': datetime.now().isoformat()
                        })
                
                # Update context if it was modified
                if hasattr(steps[-1], 'context'):
                    st.session_state.user_context = steps[-1].context
                
            except Exception as e:
                st.error(f"Error processing your request: {str(e)}")
                st.session_state.conversation_history.append({
                    'type': 'agent',
                    'content': f"I'm sorry, I encountered an error: {str(e)}. Please try again.",
                    'timestamp': datetime.now().isoformat()
                })
        
        # Refresh the page to show new messages
        st.rerun()

with col2:
    st.markdown('<div class="sub-header">📊 Quick Stats</div>', unsafe_allow_html=True)
    
    # Stats metrics
    col_stats1, col_stats2 = st.columns(2)
    
    with col_stats1:
        st.metric("Messages", len(st.session_state.conversation_history))
        st.metric("Handoffs", len(st.session_state.user_context.handoff_logs))
    
    with col_stats2:
        st.metric("Progress Logs", len(st.session_state.user_context.progress_logs))
        goal_status = "Set" if st.session_state.user_context.goal else "Not Set"
        st.metric("Goal Status", goal_status)
    
    # Current plans display
    if st.session_state.user_context.meal_plan:
        st.markdown('<div class="sub-header">🥗 Current Meal Plan</div>', unsafe_allow_html=True)
        with st.expander("View Meal Plan"):
            for i, meal in enumerate(st.session_state.user_context.meal_plan[:7], 1):
                st.write(f"**Day {i}:** {meal}")
    
    if st.session_state.user_context.workout_plan:
        st.markdown('<div class="sub-header">💪 Current Workout Plan</div>', unsafe_allow_html=True)
        with st.expander("View Workout Plan"):
            workout_plan = st.session_state.user_context.workout_plan
            if isinstance(workout_plan, dict):
                for day, exercises in workout_plan.items():
                    st.write(f"**{day}:** {exercises}")
            else:
                st.write(str(workout_plan))
    
    # Features info
    st.markdown('<div class="sub-header">✨ Features</div>', unsafe_allow_html=True)
    st.markdown("""
    - 🎯 **Goal Analysis**: Set and track wellness goals
    - 🥗 **Meal Planning**: Personalized nutrition plans
    - 💪 **Workout Plans**: Custom fitness routines
    - 📅 **Scheduling**: Progress check reminders
    - 🔄 **Expert Handoffs**: Specialized agent support
    - 📊 **Progress Tracking**: Monitor your journey
    """)

# Footer
st.markdown("---")
st.markdown("Built with ❤️ using OpenAI Agents SDK and Streamlit")
st.markdown("**Note:** This is a demo application. Always consult healthcare professionals for medical advice.")