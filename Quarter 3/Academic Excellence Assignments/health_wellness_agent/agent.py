from openai import Agent
from tools.goal_analyzer import goal_analyzer_tool
from tools.meal_planner import meal_planner_tool
from tools.workout_recommender import workout_recommender_tool
from tools.scheduler import checkin_scheduler_tool
from tools.tracker import progress_tracker_tool
from my_agents.escalation_agent import escalation_agent
from my_agents.nutrition_expert_agent import nutrition_expert_agent
from my_agents.injury_support_agent import injury_support_agent

planner_agent = Agent(
    name="HealthPlannerAgent",
    system_message="You are a friendly AI health planner.",
    instructions="Understand user fitness and dietary goals and generate health plans.",
    tools=[
        goal_analyzer_tool,
        meal_planner_tool,
        workout_recommender_tool,
        checkin_scheduler_tool,
        progress_tracker_tool
    ],
    handoffs={
        "EscalationAgent": escalation_agent,
        "NutritionExpertAgent": nutrition_expert_agent,
        "InjurySupportAgent": injury_support_agent
    }
)

