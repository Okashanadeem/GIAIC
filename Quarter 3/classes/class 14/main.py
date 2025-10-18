# main.py

from my_config import config
from agents import Agent, Runner, function_tool
from typing_extensions import TypedDict

class MyDataType(TypedDict):
    city: str
    weather: str
    temperature: str

@function_tool
async def fetch_weather(city: str) -> str:
    """
    Fetch weather according to the given city.

    Args:
    city: Name of the city.
    """
    return f"The weather in {city} is sunny."

simple_agent = Agent(
    name="Assistant",
    instructions="You are a helpful Assistant",
    tools=[fetch_weather],
    output_type=MyDataType
)

result = Runner.run_sync(
    starting_agent=simple_agent,
    input="What is the weather in Karachi?",
    run_config=config
)

print("Result:", result.final_output)
