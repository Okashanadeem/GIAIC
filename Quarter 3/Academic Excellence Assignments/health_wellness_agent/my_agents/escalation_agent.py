from openai import Agent

escalation_agent = Agent(
    name="EscalationAgent",
    system_message="You are a human wellness coach.",
    instructions="Help the user personally and resolve complex questions."
)
