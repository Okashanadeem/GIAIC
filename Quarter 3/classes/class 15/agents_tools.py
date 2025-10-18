# main.py

from my_config import config
from agents import Agent, Runner, function_tool, enable_verbose_stdout_logging
import asyncio
from dotenv import load_dotenv

load_dotenv()
enable_verbose_stdout_logging()

@function_tool(name_override="get_weather", 
               description_override="weather ka data le ao.", 
               use_docstring_info=False)
async def fetch_weather(city: str) -> str:
    """
    Fetch weather according to the given city.

    Args:
    city: Name of the city.
    """
    # raise UseError("Tool has error")
    return f"The weather in {city} is sunny."

simple_agent = Agent(
    name="Assistant",
    instructions="You are a helpful Assistant",
    tools=[fetch_weather],
)

result = Runner.run_sync(
    starting_agent=simple_agent,
    input="What is the weather in Karachi?",
    run_config=config
)

print("Result:", result.final_output)
