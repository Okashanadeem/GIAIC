from agents import function_tool, RunContextWrapper
from context import UserSessionContext
from guardrails import GoalInput, Goal
import asyncio

@function_tool
async def analyze_goal(wrapper: RunContextWrapper[UserSessionContext], user_input: str) -> GoalInput:
    await asyncio.sleep(0)  # Ensures async behavior (even if no I/O)
    
    if "5kg" in user_input and "2 months" in user_input:
        goal_data = Goal(
            objective="lose",
            quantity=5.0,
            metric="kg",
            duration_months=2
        )
        goal_input = GoalInput(goal=goal_data)
        wrapper.context.goal = goal_input.model_dump()
        return goal_input

    raise ValueError("Invalid goal format.")
