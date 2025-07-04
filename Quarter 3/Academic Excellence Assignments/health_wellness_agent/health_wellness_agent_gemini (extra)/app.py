# app.py

import os
import streamlit as st
from dotenv import load_dotenv
import google.generativeai as genai

from context import UserSessionContext
from tools.goal_analyzer import analyze_goal
from tools.meal_planner import get_meal_plan
from tools.workout_recommender import get_workout_plan
from tools.scheduler import schedule_checkin
from tools.tracker import track_progress

from my_agents.injury_support_agent import support_injury
from my_agents.nutrition_expert_agent import expert_nutrition
from my_agents.escalation_agent import escalate

from utils.logger import log_event

load_dotenv()
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

model = genai.GenerativeModel("models/gemini-1.5-flash")
chat = model.start_chat(history=[])

# Initialize context
if 'ctx' not in st.session_state:
    st.session_state.ctx = UserSessionContext()

st.title("🧠 Health & Wellness Planner")
st.write("Chat with your AI wellness assistant.")

user_input = st.text_input("💬 Enter your message:")

if user_input:
    ctx = st.session_state.ctx
    log_event(f"User said: {user_input}")

    if "exit" in user_input.lower():
        st.stop()

    elif "lose" in user_input or "gain" in user_input:
        ctx.goal = analyze_goal(user_input)
        st.success(f"✅ Goal saved: {ctx.goal['details']}")
        log_event("Goal analyzed")

    elif "vegetarian" in user_input or "vegan" in user_input or "diabetic" in user_input:
        ctx.diet_preferences = user_input
        meals = get_meal_plan(ctx.diet_preferences)
        ctx.meal_plan = meals
        st.info("🥗 Meal Plan:")
        for m in meals:
            st.write("•", m)
        if "diabetic" in user_input:
            st.warning(expert_nutrition(user_input))
            log_event("Handoff to Nutrition Expert")

    elif "injury" in user_input or "pain" in user_input:
        ctx.injury_notes = user_input
        st.warning(support_injury(ctx.injury_notes))
        log_event("Handoff to Injury Support Agent")

    elif "talk to human" in user_input or "real trainer" in user_input:
        st.warning(escalate())
        log_event("Handoff to Escalation Agent")

    elif "workout" in user_input or "exercise" in user_input:
        goal_type = ctx.goal["type"] if ctx.goal else "general"
        workouts = get_workout_plan(goal_type)
        ctx.workout_plan = {"type": goal_type, "plan": workouts}
        st.info("💪 Workout Plan:")
        for w in workouts:
            st.write("•", w)
        log_event("Workout planned")

    elif "check-in" in user_input:
        st.success(schedule_checkin())
        log_event("Check-in scheduled")

    elif "progress" in user_input:
        result = track_progress(user_input, ctx)
        st.info(result)
        log_event("Progress updated")

    else:
        response = chat.send_message(user_input)
        st.write("🤖 Gemini:", response.text)
        log_event("Gemini response given")
