from agents import Agent, Runner
import asyncio

spanish_agent = Agent(
    name= "Spanish Agent",
    instructions="You translate the user message to spanish"
)
french_agent= Agent(
    name= "french Agent",
    instructions="You translate the user message to french"
)

orchestrator_agnet=Agent(
    name="Orchestrator_agnet",
    instructions=(
        "you are a translation agent you use the tool given to you",
        "if asked for multiple trNALATION, YOU CALL THE RELEVANT."
    ),
    tools=[
        spanish_agent.as_tool(
            tool_name="translate_to_spanish",
            tool_description="Translate the user message to spanish",
            # custom_output_extractor=extract_json_payload
        ),
        french_agent.as_tool(
            tool_name="translate_to_french",
            tool_description="Translate the user message to french"
        )
    ]
    )

async def main():
    result = await Runner.run(orchestrator_agnet, input="say hello how are you in spanish")
    print(result.final_output)

asyncio.run(main())