import os
from agents import Agent, OpenAIChatCompletionsModel, AsyncOpenAI, set_tracing_disabled
set_tracing_disabled(True)


# Sub-agent: Nutrition Expert
NutritionExpertAgent = Agent(
    name="NutritionExpertAgent",
    model=OpenAIChatCompletionsModel(
        model="deepseek/deepseek-chat-v3-0324:free",
        openai_client=AsyncOpenAI(
                api_key=os.getenv("OPENAI_ROUTER_KEY"),
                base_url="https://openrouter.ai/api/v1"
            )
        ),
    instructions="""
            You are a friendly and knowledgeable nutrition expert.
            Your job is to help users with dietary needs, especially those with diabetes.
            Provide personalized meal plans, and respond with clarity and empathy.
            Use tools when needed.
            Specialist in diabetes and allergy-aware meal planning.
        """
    )
