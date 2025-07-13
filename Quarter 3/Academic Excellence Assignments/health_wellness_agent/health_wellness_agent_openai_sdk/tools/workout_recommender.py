from agents import function_tool, RunContextWrapper
from context import UserSessionContext
from guardrails import GoalInput, WorkoutPlanOutput, WorkoutWeekPlan

@function_tool 
def recommend_workout(wrapper: RunContextWrapper[UserSessionContext], goal: GoalInput) -> WorkoutPlanOutput:
    plan_data = WorkoutWeekPlan(week_1=["Squats", "Push-ups"], week_2=["Deadlifts", "Planks"])
    wrapper.context.workout_plan = plan_data
    return WorkoutPlanOutput(plan=plan_data)