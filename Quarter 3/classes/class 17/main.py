from config import openai_client

# -------- Agent 1: Static Greeting --------
static_agent = openai_client.agents.create(
    name="Static Agent",
    model="gemini-2.5-flash",   
    instructions="Always greet the user with the name 'Okasha'."
)

# -------- Agent 2: Dynamic Greeting --------
dynamic_agent = openai_client.agents.create(
    name="Dynamic Agent",
    model="gemini-2.5-flash",
    instructions="Greet the user with the name they provide."
)

# -------- Threads (chat sessions) --------
static_thread = openai_client.threads.create()
dynamic_thread = openai_client.threads.create()

# -------- Messages to agents --------
# Static Agent test
openai_client.threads.messages.create(
    thread_id=static_thread.id,
    role="user",
    content="Say hello."
)

# Dynamic Agent test
openai_client.threads.messages.create(
    thread_id=dynamic_thread.id,
    role="user",
    content="My name is Ali."
)

openai_client.threads.messages.create(
    thread_id=dynamic_thread.id,
    role="user",
    content="Now greet Sana."
)

# -------- Run the agents --------
print("\n--- Static Agent Output ---")
run1 = openai_client.threads.runs.create_and_poll(
    thread_id=static_thread.id,
    agent_id=static_agent.id
)
print(run1.output_text)

print("\n--- Dynamic Agent Output ---")
run2 = openai_client.threads.runs.create_and_poll(
    thread_id=dynamic_thread.id,
    agent_id=dynamic_agent.id
)
print(run2.output_text)
