import os
from agents import Runner, set_tracing_disabled, RunContextWrapper
set_tracing_disabled(True)
from context import UserSessionContext
from openai.types.responses import ResponseTextDeltaEvent
from agent import HealthWellness
import asyncio
import random



    

async def main():

    # Step 1: Ask only for user name
    name = input("👤 \U0001F464 Enter your name: ")

    # Step 2: Automatically assign a user ID
    uid = random.randint(1000, 9999)

    my_ctx = UserSessionContext(name=name,uid=uid)
    # Step 3: Build context with goal=None (agent will ask goal)
    # user_context = RunContextWrapper(context=my_ctx)

    
    
    user_input = input(f"Hello {name} 👋 How can I help you today with your health goals? ")

    Result = Runner.run_streamed(
        starting_agent=HealthWellness,
        input=user_input,
        context=my_ctx
    )

    async for event in Result.stream_events():
        if event.type == "raw_response_event" and isinstance(event.data, ResponseTextDeltaEvent):
            token = event.data.delta
            print(token, end="", flush=True)



if __name__ == "__main__":
    asyncio.run(main())