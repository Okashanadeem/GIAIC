import os
from agents import Agent, OpenAIChatCompletionsModel, AsyncOpenAI, set_tracing_disabled,RunContextWrapper

from tools.fetch_user_name import fetch_user_name
set_tracing_disabled(True)
from context import UserSessionContext
from agents_folder.escalation_agent import EscalationAgent
from agents_folder.nutrition_expert_agent import NutritionExpertAgent
from agents_folder.injury_support_agent import InjurySupportAgent
from tools.goal_analyzer import analyze_goal
from tools.meal_planner import generate_meal_plan
from tools.workout_recommender import recommend_workout
from tools.scheduler import schedule_checkin
from tools.tracker import track_progress
from guardrails_ext import health_guardrail, validate_meal_output
from hooks import hooks



HealthWellness = Agent[UserSessionContext](
        name="HealthWellnessAgent",
        model=OpenAIChatCompletionsModel(
            
            model="deepseek/deepseek-chat-v3-0324:free",
            openai_client=AsyncOpenAI(
                api_key=os.getenv("OPENAI_ROUTER_KEY"),
                base_url="https://openrouter.ai/api/v1"
            )
        ),
         instructions="""        
            Always reply in English.

            You are a friendly and knowledgeable digital health assistant.

            Start by greeting the user using their name (from context).

            Your responsibilities:
            - Help users clarify their fitness goals
            - Suggest weekly meal and workout plans
            - Track their progress
            - Refer to other expert agents if needed

            Use the `analyze_goal` tool to understand goals in structured format.

            📌 Output Formatting Rules:
            - When returning tool results or final answers, return only valid JSON matching the output schema.
            - Do NOT include any explanation, notes, or extra text outside the JSON object.
            - Do not wrap JSON inside triple backticks or markdown.
            - Keep the JSON clean and valid — no comments, no trailing content.

            🔹 If someone asks for the user name (e.g. 'What is my name?'), use the `fetch_user_name` tool.

            🔁 Handoff Rules:
            - If user mentions "injury" → hand off to InjurySupportAgent
            - If user says "diabetic" or "allergy" → NutritionExpertAgent
            - If user wants a human trainer → EscalationAgent

            Once control is handed over to another agent, do not respond further.
            Use tools when needed.
            """,


    tools=[analyze_goal, generate_meal_plan, recommend_workout, schedule_checkin, track_progress,fetch_user_name],
    handoffs=[NutritionExpertAgent, InjurySupportAgent, EscalationAgent],
    input_guardrails=[health_guardrail],
    hooks=hooks
        
        
    )