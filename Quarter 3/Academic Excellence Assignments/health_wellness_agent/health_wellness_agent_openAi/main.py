"""
Health & Wellness Planner Agent - Main CLI Application
Entry point for running the Health & Wellness Agent with streaming support.
"""

import asyncio
import os
import sys
import logging
from typing import Optional
from openai import OpenAI
from openai.agents import Runner
from openai.agents.types import RunContextWrapper

# Import our modules
from agent import HealthWellnessAgent
from context import UserSessionContext
from utils.streaming import StreamingHandler

# Set up logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

class HealthWellnessCLI:
    """
    Command Line Interface for the Health & Wellness Planner Agent.
    
    Provides an interactive chat experience with real-time streaming responses.
    """
    
    def __init__(self):
        """Initialize the CLI with OpenAI client and agent."""
        # Initialize OpenAI client
        api_key = os.getenv('OPENAI_API_KEY')
        if not api_key:
            logger.error("OPENAI_API_KEY environment variable not set!")
            sys.exit(1)
        
        self.client = OpenAI(api_key=api_key)
        
        # Initialize the Health & Wellness Agent
        self.agent = HealthWellnessAgent(self.client)
        
        # Initialize streaming handler
        self.streaming_handler = StreamingHandler()
        
        # Initialize user context
        self.user_context = None
        
        logger.info("Health & Wellness CLI initialized successfully!")
    
    def setup_user_context(self) -> RunContextWrapper[UserSessionContext]:
        """
        Set up initial user context through interactive prompts.
        
        Returns:
            Initialized user context wrapper
        """
        print("\n🌟 Welcome to your Health & Wellness Planner! 🌟")
        print("Let's get to know you better so I can provide personalized recommendations.\n")
        
        # Collect basic user information
        name = input("What's your name? ").strip()
        if not name:
            name = "User"
        
        print(f"\nHi {name}! Nice to meet you! 👋")
        
        # Generate a simple user ID (in a real app, this would be more sophisticated)
        uid = hash(name) % 10000
        
        # Create initial context
        context_data = UserSessionContext(
            name=name,
            uid=uid,
            handoff_logs=[f"Session started for {name}"],
            progress_logs=[]
        )
        
        # Wrap in context wrapper
        context = RunContextWrapper[UserSessionContext](data=context_data)
        
        logger.info(f"User context initialized for {name} (ID: {uid})")
        return context
    
    def display_help(self):
        """Display available commands and help information."""
        help_text = """
        🔧 Available Commands:
        • /help - Show this help message
        • /status - Show current goals and plans
        • /progress - View progress summary
        • /reset - Reset conversation context
        • /quit - Exit the application
        
        💬 You can also just chat naturally! Try saying:
        • "I want to lose 10 pounds in 2 months"
        • "I'm vegetarian and need a meal plan"
        • "I have knee pain and need safe exercises"
        • "I want to talk to a human trainer"
        """
        print(help_text)
    
    def display_status(self, context: RunContextWrapper[UserSessionContext]):
        """Display current user status and active plans."""
        print(f"\n📊 Status for {context.data.name}:")
        print("=" * 40)
        
        if context.data.goal:
            print(f"🎯 Current Goal: {context.data.goal}")
        else:
            print("🎯 No current goal set")
        
        if context.data.diet_preferences:
            print(f"🥗 Dietary Preferences: {context.data.diet_preferences}")
        
        if context.data.workout_plan:
            print("💪 Workout Plan: Active")
        else:
            print("💪 No workout plan set")
        
        if context.data.meal_plan:
            print(f"🍽️ Meal Plan: {len(context.data.meal_plan)} meals planned")
        else:
            print("🍽️ No meal plan set")
        
        if context.data.injury_notes:
            print(f"⚠️ Notes: {context.data.injury_notes}")
        
        print(f"📈 Progress Entries: {len(context.data.progress_logs)}")
        print("=" * 40)
    
    def display_progress(self, context: RunContextWrapper[UserSessionContext]):
        """Display progress summary."""
        print(f"\n📈 Progress Summary for {context.data.name}:")
        print("=" * 40)
        
        if not context.data.progress_logs:
            print("No progress entries yet. Start tracking your progress!")
            return
        
        for i, log in enumerate(context.data.progress_logs[-5:], 1):  # Show last 5 entries
            print(f"{i}. {log}")
        
        if len(context.data.progress_logs) > 5:
            print(f"... and {len(context.data.progress_logs) - 5} more entries")
        
        print("=" * 40)
    
    def reset_context(self) -> RunContextWrapper[UserSessionContext]:
        """Reset the conversation context."""
        print("\n🔄 Resetting conversation context...")
        return self.setup_user_context()
    
    async def process_streaming_response(self, user_input: str, context: RunContextWrapper[UserSessionContext]):
        """
        Process user input with streaming response.
        
        Args:
            user_input: User's input message
            context: Current user session context
        """
        print(f"\n🤖 Health & Wellness Agent: ", end="", flush=True)
        
        try:
            # Use Runner.stream for real-time streaming
            response_text = ""
            async for step in Runner.stream(
                client=self.client,
                starting_agent=self.agent,
                input=user_input,
                context=context
            ):
                # Handle different types of streaming steps
                if hasattr(step, 'response') and step.response:
                    chunk = step.response
                    print(chunk, end="", flush=True)
                    response_text += chunk
                elif hasattr(step, 'tool_call') and step.tool_call:
                    print(f"\n🔧 Using tool: {step.tool_call.name}...", end="", flush=True)
                elif hasattr(step, 'tool_response') and step.tool_response:
                    print(" ✅", end="", flush=True)
                elif hasattr(step, 'handoff') and step.handoff:
                    print(f"\n🔄 Handing off to {step.handoff.agent_name}...", end="", flush=True)
            
            print("\n")  # New line after streaming completes
            
            # Log the interaction
            context.data.handoff_logs.append(f"User: {user_input}")
            context.data.handoff_logs.append(f"Agent: {response_text[:100]}...")
            
        except Exception as e:
            logger.error(f"Error during streaming: {e}")
            print(f"\n❌ Sorry, I encountered an error: {e}")
            print("Please try again or type /help for available commands.")
    
    async def run_interactive_session(self):
        """Run the main interactive session."""
        # Setup user context
        self.user_context = self.setup_user_context()
        
        # Display welcome message and help
        print(f"\n🎉 Great! I'm here to help you with your health and wellness goals.")
        print("You can ask me about meal planning, workouts, goal setting, and more!")
        print("Type /help to see available commands, or just start chatting!\n")
        
        # Main conversation loop
        while True:
            try:
                # Get user input
                user_input = input(f"\n{self.user_context.data.name}: ").strip()
                
                if not user_input:
                    continue
                
                # Handle special commands
                if user_input.startswith('/'):
                    if user_input == '/quit':
                        print(f"\n👋 Goodbye {self.user_context.data.name}! Keep working towards your goals!")
                        break
                    elif user_input == '/help':
                        self.display_help()
                    elif user_input == '/status':
                        self.display_status(self.user_context)
                    elif user_input == '/progress':
                        self.display_progress(self.user_context)
                    elif user_input == '/reset':
                        self.user_context = self.reset_context()
                    else:
                        print("❓ Unknown command. Type /help for available commands.")
                    continue
                
                # Process regular user input with streaming
                await self.process_streaming_response(user_input, self.user_context)
                
            except KeyboardInterrupt:
                print(f"\n\n👋 Goodbye {self.user_context.data.name}! Keep working towards your goals!")
                break
            except Exception as e:
                logger.error(f"Unexpected error: {e}")
                print(f"\n❌ An unexpected error occurred: {e}")
                print("Please try again or type /quit to exit.")
    
    def run(self):
        """Run the CLI application."""
        try:
            asyncio.run(self.run_interactive_session())
        except KeyboardInterrupt:
            print("\n\n👋 Goodbye! Keep working towards your goals!")
        except Exception as e:
            logger.error(f"Failed to run CLI: {e}")
            print(f"❌ Failed to start the application: {e}")
            sys.exit(1)

def main():
    """Main entry point for the Health & Wellness Planner Agent."""
    print("🚀 Starting Health & Wellness Planner Agent...")
    
    # Create and run CLI
    cli = HealthWellnessCLI()
    cli.run()

if __name__ == "__main__":
    main()