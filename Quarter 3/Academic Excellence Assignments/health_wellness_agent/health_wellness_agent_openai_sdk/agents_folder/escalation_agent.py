import os
from agents import Agent, OpenAIChatCompletionsModel, AsyncOpenAI, set_tracing_disabled
set_tracing_disabled(True)

# Sub-agent: Escalation Agent
EscalationAgent = Agent(
    name="EscalationAgent",
    model=OpenAIChatCompletionsModel(
        model="deepseek/deepseek-chat-v3-0324:free",
        openai_client=AsyncOpenAI(
            api_key=os.getenv("OPENAI_ROUTER_KEY"),
            base_url="https://openrouter.ai/api/v1"
        )
    ),
    instructions="""
            when call you first say Asslam o alikum then continoue your advice.
            You are a friendly and knowledgeable digital health assistant.
            Your job is to assist users who want to escalate their concerns to a human trainer.
            If a user requests to talk to a human trainer, provide them with the necessary information
            and ensure they feel supported. Always speak clearly and provide concise, helpful responses.
            Use tools when needed, and remember user context.
            Connects user to a human trainer.
        """
    )