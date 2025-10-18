from agents import Agent, handoff, RunContextWrapper, Runner
from dotenv import load_dotenv

_ : bool = load_dotenv()

billing_agent= Agent(name="Billing Agnet")
refund_agnet= Agent(name="Refund Agent")

async def on_handoff_func():
    print(f"Escalation agent called with reason")

triage_agent = Agent(
    name = "Triage Agent",
    handoffs=[billing_agent,
              handoff(agent=refund_agnet,
                      on_handoff=on_handoff_func)
              ]
)
rusult = Runner.run(triage_agent())