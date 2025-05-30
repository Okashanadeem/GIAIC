import google.generativeai as genai
from dotenv import load_dotenv
import os

load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")
genai.configure(api_key=api_key)
model = genai.GenerativeModel(model_name="models/gemini-1.5-pro-latest")

try:
    response = model.generate_content("Say Hello!")
    print("Gemini says:", response.text)
except Exception as e:
    print("Error calling Gemini API:", e)
