"""
Health & Wellness Planner Agent - Core Agent Implementation
Built using OpenAI Agents SDK for natural language health and wellness planning.
"""

import logging
from typing import Dict, List, Optional, Any
from openai import OpenAI
from openai.agents import Agent
from openai.agents.types import RunContextWrapper

# Import our custom modules
from context import UserSessionContext
from guardrails import HealthGuardrails
from tools.goal_analyzer import GoalAnalyzerTool
from tools.meal_planner import MealPlannerTool
from tools.workout_recommender import WorkoutRecommenderTool
from tools.scheduler import CheckinSchedulerTool
from tools.tracker import ProgressTrackerTool
from agents.escalation_agent import EscalationAgent
from agents.nutrition_expert_agent import NutritionExpertAgent
from agents.injury_support_agent import InjurySupportAgent

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class HealthWellnessAgent(Agent):
    """
    Main Health & Wellness Planner Agent that coordinates all health and wellness activities.
    
    This agent serves as the central coordinator for:
    - Goal analysis and planning through natural language conversation
    - Meal planning and nutrition guidance
    - Workout recommendations
    - Progress tracking and scheduling
    - Handoffs to specialized agents when needed
    """
    
    def __init__(self, client: OpenAI):
        """Initialize the Health & Wellness Agent with OpenAI client and tools."""
        logger.info("Initializing Health & Wellness Agent...")
        
        # Initialize guardrails
        self.guardrails = HealthGuardrails()
        
        # Initialize tools
        self.goal_analyzer = GoalAnalyzerTool()
        self.meal_planner = MealPlannerTool()
        self.workout_recommender = WorkoutRecommenderTool()
        self.scheduler = CheckinSchedulerTool()
        self.tracker = ProgressTrackerTool()
        
        # Initialize specialized agents for handoffs
        self.escalation_agent = EscalationAgent(client)
        self.nutrition_expert = NutritionExpertAgent(client)
        self.injury_support = InjurySupportAgent(client)
        
        # Define system instructions
        instructions = """
        You are a Health & Wellness Planner Agent, a friendly and knowledgeable AI assistant specialized in helping users achieve their health and fitness goals.

        Your primary responsibilities:
        1. Engage users in natural conversation to understand their health goals
        2. Analyze goals and create structured health plans
        3. Provide personalized meal and workout recommendations
        4. Track progress and schedule check-ins
        5. Handle handoffs to specialized agents when needed

        Key behaviors:
        - Be encouraging and supportive in your communication
        - Ask clarifying questions to better understand user needs
        - Provide actionable, personalized advice
        - Use tools to analyze goals and create structured plans
        - Know when to hand off to specialized agents

        Handoff triggers:
        - User wants to speak to a human coach → EscalationAgent
        - Complex dietary needs (diabetes, allergies) → NutritionExpertAgent
        - Physical limitations or injuries → InjurySupportAgent

        Always maintain context about the user's profile, goals, and progress throughout the conversation.
        """
        
        # Initialize the Agent with tools and handoffs
        super().__init__(
            client=client,
            instructions=instructions,
            tools=[
                self.goal_analyzer,
                self.meal_planner,
                self.workout_recommender,
                self.scheduler,
                self.tracker
            ],
            handoffs=[
                self.escalation_agent,
                self.nutrition_expert,
                self.injury_support
            ]
        )
        
        logger.info("Health & Wellness Agent initialized successfully!")
    
    def get_system_message(self, context: RunContextWrapper[UserSessionContext]) -> str:
        """
        Generate a personalized system message based on current user context.
        
        Args:
            context: Current user session context
            
        Returns:
            Personalized system message string
        """
        user_info = []
        
        if context.data.name:
            user_info.append(f"User name: {context.data.name}")
        
        if context.data.goal:
            user_info.append(f"Current goal: {context.data.goal}")
        
        if context.data.diet_preferences:
            user_info.append(f"Dietary preferences: {context.data.diet_preferences}")
        
        if context.data.injury_notes:
            user_info.append(f"Injury/limitation notes: {context.data.injury_notes}")
        
        if context.data.workout_plan:
            user_info.append("Has active workout plan")
        
        if context.data.meal_plan:
            user_info.append("Has active meal plan")
        
        context_info = "\n".join(user_info) if user_info else "No previous context available"
        
        return f"""
        Current user context:
        {context_info}
        
        Use this context to provide personalized responses and avoid asking for information you already have.
        """
    
    def should_handoff_to_escalation(self, message: str) -> bool:
        """Check if user wants to speak to a human coach."""
        escalation_keywords = [
            "human coach", "real trainer", "speak to someone", "talk to a person",
            "human help", "real person", "live coach", "personal trainer"
        ]
        return any(keyword in message.lower() for keyword in escalation_keywords)
    
    def should_handoff_to_nutrition_expert(self, message: str, context: RunContextWrapper[UserSessionContext]) -> bool:
        """Check if user has complex dietary needs requiring nutrition expert."""
        nutrition_keywords = [
            "diabetes", "diabetic", "allergy", "allergies", "celiac", "gluten",
            "medical condition", "health condition", "medication", "insulin",
            "blood sugar", "cholesterol", "hypertension", "heart condition"
        ]
        return any(keyword in message.lower() for keyword in nutrition_keywords)
    
    def should_handoff_to_injury_support(self, message: str, context: RunContextWrapper[UserSessionContext]) -> bool:
        """Check if user has injury or physical limitations."""
        injury_keywords = [
            "injury", "injured", "pain", "hurt", "limitation", "disability",
            "knee pain", "back pain", "shoulder pain", "arthritis", "surgery",
            "physical therapy", "rehabilitation", "can't do", "unable to"
        ]
        return any(keyword in message.lower() for keyword in injury_keywords)
    
    def analyze_handoff_needs(self, message: str, context: RunContextWrapper[UserSessionContext]) -> Optional[str]:
        """
        Analyze if the user's message requires a handoff to a specialized agent.
        
        Args:
            message: User's message
            context: Current user session context
            
        Returns:
            Name of the agent to handoff to, or None if no handoff needed
        """
        if self.should_handoff_to_escalation(message):
            return "escalation_agent"
        elif self.should_handoff_to_nutrition_expert(message, context):
            return "nutrition_expert"
        elif self.should_handoff_to_injury_support(message, context):
            return "injury_support"
        
        return None
    
    async def process_user_input(self, message: str, context: RunContextWrapper[UserSessionContext]) -> Dict[str, Any]:
        """
        Process user input and determine appropriate response strategy.
        
        Args:
            message: User's input message
            context: Current user session context
            
        Returns:
            Dictionary containing processing results and next steps
        """
        logger.info(f"Processing user input: {message[:50]}...")
        
        # Apply input guardrails
        validated_input = self.guardrails.validate_input(message)
        
        # Check if handoff is needed
        handoff_target = self.analyze_handoff_needs(message, context)
        
        # Update context with new interaction
        context.data.handoff_logs.append(f"User input: {message[:100]}")
        
        return {
            "validated_input": validated_input,
            "handoff_target": handoff_target,
            "context_updated": True,
            "timestamp": context.data.handoff_logs[-1] if context.data.handoff_logs else None
        }
    
    def get_conversation_summary(self, context: RunContextWrapper[UserSessionContext]) -> str:
        """
        Generate a summary of the current conversation and user progress.
        
        Args:
            context: Current user session context
            
        Returns:
            Formatted conversation summary
        """
        summary_parts = []
        
        if context.data.name:
            summary_parts.append(f"👤 User: {context.data.name}")
        
        if context.data.goal:
            summary_parts.append(f"🎯 Goal: {context.data.goal}")
        
        if context.data.diet_preferences:
            summary_parts.append(f"🥗 Diet: {context.data.diet_preferences}")
        
        if context.data.workout_plan:
            summary_parts.append("💪 Workout plan: Active")
        
        if context.data.meal_plan:
            summary_parts.append("🍽️ Meal plan: Active")
        
        if context.data.injury_notes:
            summary_parts.append(f"⚠️ Notes: {context.data.injury_notes}")
        
        if context.data.progress_logs:
            summary_parts.append(f"📊 Progress entries: {len(context.data.progress_logs)}")
        
        return "\n".join(summary_parts) if summary_parts else "No conversation history available"
    
    def __str__(self) -> str:
        """String representation of the agent."""
        return "HealthWellnessAgent(tools=5, handoffs=3)"
    
    def __repr__(self) -> str:
        """Detailed string representation of the agent."""
        return f"HealthWellnessAgent(tools=[{', '.join([tool.__class__.__name__ for tool in self.tools])}], handoffs=[{', '.join([agent.__class__.__name__ for agent in self.handoffs])}])"