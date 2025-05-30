import google.generativeai as genai
from dotenv import load_dotenv
import os

load_dotenv()
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

def ask_gemini(question):
    model = genai.GenerativeModel(model_name="models/gemini-1.5-pro-latest")
    response = model.generate_content(question)
    return response.text

while True:
    user_input = input("You: ")
    if user_input.lower() in ['exit', 'quit']:
        break
    answer = ask_gemini(user_input)
    print("Gemini:", answer)
