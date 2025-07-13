from agents import RunHooks
from agents import RunContextWrapper, Agent, Tool

class CustomHooks(RunHooks):
    async def on_start(self, context: RunContextWrapper, agent: Agent):
        try:
            user_name = getattr(context.context, "name", "Unknown")
        except Exception:
            user_name = "Unknown"
        print(f"[Agent {agent.name} starting for user {user_name}]")

    async def on_end(self, context: RunContextWrapper, agent: Agent, output):
        print(f"[Agent {agent.name} ended with output: {output}]")

    async def on_tool_start(self, context: RunContextWrapper, agent: Agent, tool: Tool):
        print(f"[Tool {tool.name} started by {agent.name}]")

    async def on_tool_end(self, context: RunContextWrapper, agent: Agent, tool: Tool, result):
        print(f"[Tool {tool.name} result: {result}]")

    async def on_handoff(self, context_wrapper: RunContextWrapper, agent: Agent, source: Agent, message: str):
        print(f"[Handoff from {source.name} to {agent.name} | message: {message}]")

hooks = CustomHooks()
