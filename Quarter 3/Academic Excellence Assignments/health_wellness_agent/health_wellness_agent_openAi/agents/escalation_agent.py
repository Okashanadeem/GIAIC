"""
Escalation Agent for Health & Wellness Planner
Handles requests to connect with human coaches/trainers
"""

from datetime import datetime
from openai_agents import Agent
from ..context import UserSessionContext


class EscalationAgent(Agent):
    """Agent for handling escalation to human coaches"""
    
    name = "escalation_agent"
    description = "Handles user requests to connect with human coaches or trainers"
    
    instructions = """
    You are an Escalation Agent for a health and wellness platform. Your role is to:
    
    1. Acknowledge the user's request to speak with a human coach
    2. Collect necessary information for the escalation
    3. Provide realistic expectations about response times
    4. Offer immediate helpful resources while they wait
    5. Log the escalation request in the system
    
    Be professional, empathetic, and helpful. Make the user feel heard and supported.
    """
    
    def __init__(self):
        super().__init__(
            name=self.name,
            description=self.description,
            instructions=self.instructions
        )
    
    async def on_handoff(self, context: UserSessionContext, handoff_reason: str = "") -> str:
        """
        Handle the handoff to escalation agent
        
        Args:
            context: User session context
            handoff_reason: Reason for handoff
            
        Returns:
            Initial response message
        """
        # Log the handoff
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        handoff_log = f"[{timestamp}] Escalated to human coach - Reason: {handoff_reason}"
        
        if not hasattr(context, 'handoff_logs'):
            context.handoff_logs = []
        context.handoff_logs.append(handoff_log)
        
        # Generate personalized response
        user_name = getattr(context, 'name', 'there')
        
        initial_response = f"""
        Hi {user_name}! I understand you'd like to speak with a human coach. I'm here to help connect you with the right person.
        
        I've logged your request and our team will reach out to you within 24-48 hours. In the meantime, let me gather some information to ensure you get the best possible support.
        
        Could you please share:
        1. What specific area you'd like coaching on (nutrition, fitness, motivation, etc.)?
        2. Any urgent concerns or questions you have?
        3. Your preferred contact method (email, phone, video call)?
        
        While you wait, I can also provide you with some immediate resources that might be helpful!
        """
        
        return initial_response.strip()
    
    async def process_escalation_request(self, context: UserSessionContext, user_input: str) -> str:
        """
        Process the escalation request and collect information
        
        Args:
            context: User session context
            user_input: User's input about their escalation needs
            
        Returns:
            Response with next steps
        """
        # Analyze the input for key information
        coaching_areas = []
        contact_preferences = []
        urgency_level = "normal"
        
        # Simple keyword detection
        input_lower = user_input.lower()
        
        # Detect coaching areas
        if any(word in input_lower for word in ['nutrition', 'diet', 'eating', 'food']):
            coaching_areas.append('nutrition')
        if any(word in input_lower for word in ['workout', 'exercise', 'fitness', 'training']):
            coaching_areas.append('fitness')
        if any(word in input_lower for word in ['motivation', 'mental', 'mindset']):
            coaching_areas.append('motivation')
        if any(word in input_lower for word in ['injury', 'pain', 'hurt']):
            coaching_areas.append('injury_support')
            urgency_level = "high"
        
        # Detect contact preferences
        if any(word in input_lower for word in ['email', 'mail']):
            contact_preferences.append('email')
        if any(word in input_lower for word in ['phone', 'call']):
            contact_preferences.append('phone')
        if any(word in input_lower for word in ['video', 'zoom', 'meet']):
            contact_preferences.append('video')
        
        # Detect urgency
        if any(word in input_lower for word in ['urgent', 'asap', 'immediately', 'emergency']):
            urgency_level = "urgent"
        
        # Create escalation summary
        escalation_summary = {
            "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "coaching_areas": coaching_areas or ["general"],
            "contact_preferences": contact_preferences or ["email"],
            "urgency_level": urgency_level,
            "user_message": user_input
        }
        
        # Add to context
        if not hasattr(context, 'escalation_requests'):
            context.escalation_requests = []
        context.escalation_requests.append(escalation_summary)
        
        # Generate response based on urgency
        if urgency_level == "urgent":
            response = f"""
            I understand this is urgent. I've marked your request as high priority and our team will contact you within 4-6 hours.
            
            For immediate support, please consider:
            - Contacting your doctor if this is a medical emergency
            - Calling our 24/7 support line at 1-800-WELLNESS
            
            Your request details:
            - Areas of focus: {', '.join(coaching_areas) if coaching_areas else 'General wellness'}
            - Contact method: {', '.join(contact_preferences) if contact_preferences else 'Email'}
            - Priority: High
            """
        else:
            response = f"""
            Perfect! I've recorded your information and created your coaching request.
            
            Your request summary:
            - Areas of focus: {', '.join(coaching_areas) if coaching_areas else 'General wellness'}
            - Contact method: {', '.join(contact_preferences) if contact_preferences else 'Email'}
            - Expected response: Within 24-48 hours
            
            While you wait, here are some resources that might help:
            
            🏃‍♂️ **Fitness**: Check out our beginner workout videos
            🥗 **Nutrition**: Browse our healthy recipe collection
            📱 **Motivation**: Download our daily wellness tips
            
            Is there anything else I can help you with while you wait for your human coach?
            """
        
        return response.strip()
    
    async def provide_resources(self, context: UserSessionContext, resource_type: str = "general") -> str:
        """
        Provide immediate resources while user waits
        
        Args:
            context: User session context
            resource_type: Type of resources to provide
            
        Returns:
            Resource recommendations
        """
        resources = {
            "fitness": """
            🏃‍♂️ **Fitness Resources While You Wait:**
            
            • **Quick Workouts**: 10-minute bodyweight exercises you can do anywhere
            • **Beginner Guide**: Step-by-step fitness fundamentals
            • **Workout Videos**: Free access to our video library
            • **Progress Tracker**: Log your workouts to share with your coach
            
            Would you like me to create a basic workout plan to get you started?
            """,
            
            "nutrition": """
            🥗 **Nutrition Resources While You Wait:**
            
            • **Healthy Recipes**: Quick, nutritious meal ideas
            • **Meal Planning**: Weekly meal prep strategies
            • **Nutrition Basics**: Understanding macros and calories
            • **Food Diary**: Track your meals to discuss with your coach
            
            I can also generate a sample meal plan if you'd like!
            """,
            
            "motivation": """
            🧠 **Motivation Resources While You Wait:**
            
            • **Daily Affirmations**: Positive mindset boosters
            • **Goal Setting**: Framework for achieving your wellness goals
            • **Success Stories**: Inspiring transformation journeys
            • **Habit Building**: Tips for creating lasting healthy habits
            
            Would you like help setting some achievable short-term goals?
            """,
            
            "general": """
            🌟 **General Wellness Resources While You Wait:**
            
            • **Wellness Assessment**: Quick health and fitness evaluation
            • **Goal Setting Tool**: Define your wellness objectives
            • **Progress Tracking**: Monitor your journey
            • **Community Support**: Connect with others on similar journeys
            
            I'm here to help with any immediate questions or guidance you need!
            """
        }
        
        return resources.get(resource_type, resources["general"]).strip()


# Agent instance for export
escalation_agent = EscalationAgent()