import os
from agents import  Agent, OpenAIChatCompletionsModel, AsyncOpenAI, set_tracing_disabled
set_tracing_disabled(True)


# Sub-agent: Injury Support Expert
InjurySupportAgent = Agent(
    name="InjurySupportAgent",  
    model=OpenAIChatCompletionsModel(
        model="deepseek/deepseek-chat-v3-0324:free",
        openai_client=AsyncOpenAI(
            api_key=os.getenv("OPENAI_ROUTER_KEY"),
            base_url="https://openrouter.ai/api/v1"
        )
    ),
    instructions="""
            You are a friendly and knowledgeable digital health assistant.
            Your job is to help users with workout recommendations that accommodate their injuries.
            If a user mentions an injury, provide alternative exercises or modifications to their routine.
            Always speak clearly and provide concise, helpful responses.
            Use tools when needed.
            Expert in injury-friendly workout plans.
        """
    )
