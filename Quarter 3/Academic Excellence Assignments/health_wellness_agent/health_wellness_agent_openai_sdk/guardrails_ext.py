from agents import input_guardrail, output_guardrail, GuardrailFunctionOutput, RunContextWrapper,OpenAIChatCompletionsModel, AsyncOpenAI
import os
from context import UserSessionContext
from agents import Agent, Runner
from guardrails import GoalInput, MealPlanOutput

health_check_agent = Agent(
    name="HealthChecker",
    model=OpenAIChatCompletionsModel(
            model="deepseek/deepseek-chat-v3-0324:free",
            openai_client=AsyncOpenAI(
                api_key=os.getenv("OPENAI_ROUTER_KEY"),
                base_url="https://openrouter.ai/api/v1"
            )
        ),
    instructions="Check if user input relates to health or wellness.",
    output_type=GoalInput,
)

@input_guardrail
async def health_guardrail(ctx: RunContextWrapper[UserSessionContext], agent, user_input: str) -> GuardrailFunctionOutput:
    result = await Runner.run(health_check_agent, user_input, context=ctx.context)

    # ✅ Access nested value safely
    try:
        flagged = result.final_output.goal.objective not in ["lose", "gain", "maintain"]
    except AttributeError:
        # If goal or objective doesn't exist, flag it
        flagged = True

    return GuardrailFunctionOutput(output_info=result.final_output, tripwire_triggered=flagged)


@output_guardrail
async def validate_meal_output(ctx: RunContextWrapper[UserSessionContext], agent, output: MealPlanOutput) -> GuardrailFunctionOutput:
    flagged = not isinstance(output.plan, list) or len(output.plan) != 7
    return GuardrailFunctionOutput(output_info=output, tripwire_triggered=flagged)
