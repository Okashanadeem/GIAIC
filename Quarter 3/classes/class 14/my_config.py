from agents import OpenAIChatCompletionsModel, RunConfig, AsyncOpenAI
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

# Get the Gemini API key from .env
gemini_api_key = os.environ["GEMINI_API_KEY"]

# Set up the client and model
client = AsyncOpenAI(
    api_key=gemini_api_key,
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
)

model = OpenAIChatCompletionsModel(
    model="gemini-2.0-flash",
    openai_client=client
)

config = RunConfig(
    model=model,
    model_provider=client,
    tracing_disabled=False
)

