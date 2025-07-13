from agents import function_tool, output_guardrail, RunContextWrapper, GuardrailFunctionOutput
from context import UserSessionContext
from guardrails import MealPlanOutput

@function_tool
async def generate_meal_plan(wrapper: RunContextWrapper[UserSessionContext], diet_preference: str) -> MealPlanOutput:
    plan = [f"{diet_preference} Meal - Day {i+1}" for i in range(7)]
    wrapper.context.meal_plan = plan
    return MealPlanOutput(plan=plan)

@output_guardrail
async def validate_meal_output(ctx: RunContextWrapper[UserSessionContext], agent, output: MealPlanOutput) -> GuardrailFunctionOutput:
    flagged = not isinstance(output.plan, list) or len(output.plan) != 7
    return GuardrailFunctionOutput(output_info=output, tripwire_triggered=flagged)
