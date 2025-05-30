import google.generativeai as genai
from dotenv import load_dotenv
import os

load_dotenv()
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

class SimpleAgent:
    def __init__(self):
        self.model = genai.GenerativeModel(model_name="models/gemini-1.5-pro-latest")

    def chat(self, message):
        response = self.model.generate_content(message)
        return response.text

agent = SimpleAgent()
reply = agent.chat("Hello Agent, what can you do?")
print("Agent:", reply)
