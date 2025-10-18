from openai import OpenAI
from openai import ExternalClient

# ✅ Gemini external client
gemini_client = ExternalClient(
    name="gemini",
    api_key="YOUR_GEMINI_API_KEY",   # put your real API key here
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
)

# ✅ OpenAI Agents entrypoint
openai_client = OpenAI()
