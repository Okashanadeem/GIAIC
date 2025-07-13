# simple_travel_agent.py

import os
from dotenv import load_dotenv
from agents import Agent, tool
import google.generativeai as genai

# Load .env file and set Gemini key
load_dotenv()
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

# 🔧 Helper to safely call Gemini
def ask_gemini(prompt):
    try:
        model = genai.GenerativeModel("gemini-pro")  # Free-tier model
        response = model.generate_content(prompt)
        return response.text.strip() if response.text else "No response from Gemini."
    except Exception as e:
        return f"Error: {e}"

# 🔨 Tool 1: Destination suggestion
@tool
def suggest_destination(interest: str) -> str:
    """Suggest one travel destination based on interest."""
    prompt = f"Suggest one popular travel destination for someone who likes {interest}. Reply with only the place name."
    return ask_gemini(prompt)

# 🔨 Tool 2: Budget estimation
@tool
def estimate_budget(destination: str) -> str:
    """Estimate a 5-day solo trip budget."""
    prompt = f"Estimate the cost for a 5-day solo trip to {destination}, including flight, hotel, and food. Keep it simple."
    return ask_gemini(prompt)

# 🤖 Agents
travel_agent = Agent(
    name="TravelAgent",
    instructions="Help the user pick a destination using Gemini.",
    tools=[suggest_destination],
)

budget_agent = Agent(
    name="BudgetAgent",
    instructions="Estimate a simple travel budget using Gemini.",
    tools=[estimate_budget],
)

# 🏁 App logic
def main():
    print("🌍 Welcome to Gemini Travel Planner!")
    interest = input("What are you interested in? (e.g., beaches, hiking, culture): ")

    # Step 1: Get destination
    destination = travel_agent.run(f"Suggest a destination for: {interest}")
    print(f"\n📍 TravelAgent suggests: {destination}")

    # Step 2: Get budget
    print("\n💸 Estimating trip cost...")
    budget = budget_agent.run(f"Estimate budget for {destination}")
    print(f"\nEstimated Budget for {destination}:\n{budget}")

if __name__ == "__main__":
    main()
