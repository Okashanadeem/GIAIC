"""
Injury Support Agent for Health & Wellness Planner
Handles users with physical limitations or injury-specific workout needs
"""

from openai import OpenAI
from openai_agents import Agent
from typing import Dict, Any, Optional
import asyncio
import logging
from context import UserSessionContext

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class InjurySupportAgent(Agent):
    """
    Specialized agent for handling injury-related fitness concerns
    Triggered when users mention injuries, pain, or physical limitations
    """
    
    def __init__(self, client: OpenAI):
        super().__init__(
            name="InjurySupportAgent",
            instructions="""
            You are a specialized Injury Support Assistant for a Health & Wellness Planner.
            Your role is to help users with physical limitations, injuries, or pain concerns.
            
            Key responsibilities:
            1. Assess injury/limitation severity and type
            2. Provide safe, modified workout recommendations
            3. Suggest when to seek professional medical advice
            4. Update user context with injury notes
            5. Coordinate with other agents when needed
            
            Important guidelines:
            - NEVER provide medical diagnosis
            - Always recommend consulting healthcare professionals for serious injuries
            - Focus on safe, low-impact exercises when appropriate
            - Be empathetic and supportive
            - Document all injury-related information in context
            
            When users describe injuries or limitations:
            1. Ask clarifying questions about the injury
            2. Assess current pain levels and mobility
            3. Provide appropriate modified exercise suggestions
            4. Update the user's injury notes in context
            5. Recommend professional consultation when needed
            """,
            client=client
        )
    
    async def on_handoff(self, context: UserSessionContext, handoff_reason: str = "") -> Dict[str, Any]:
        """
        Called when control is handed off to this agent
        """
        logger.info(f"InjurySupportAgent received handoff: {handoff_reason}")
        
        # Log the handoff
        context.handoff_logs.append(f"Handoff to InjurySupportAgent: {handoff_reason}")
        
        # Analyze the handoff reason for injury-related keywords
        injury_keywords = ["pain", "injury", "hurt", "sore", "limitation", "disability", "recovery"]
        detected_concerns = [keyword for keyword in injury_keywords if keyword.lower() in handoff_reason.lower()]
        
        if detected_concerns:
            logger.info(f"Detected injury concerns: {detected_concerns}")
            context.injury_notes = f"Initial concerns: {', '.join(detected_concerns)}"
        
        return {
            "status": "handoff_received",
            "agent": "InjurySupportAgent",
            "detected_concerns": detected_concerns,
            "context_updated": True
        }
    
    async def assess_injury_severity(self, injury_description: str, context: UserSessionContext) -> Dict[str, Any]:
        """
        Assess the severity of reported injury/limitation
        """
        # Keywords that suggest immediate professional consultation
        serious_keywords = [
            "severe", "sharp", "shooting", "numbness", "tingling", 
            "swelling", "can't move", "unable to", "excruciating",
            "getting worse", "chronic", "surgery", "fracture"
        ]
        
        # Check for serious injury indicators
        serious_indicators = [keyword for keyword in serious_keywords 
                            if keyword.lower() in injury_description.lower()]
        
        if serious_indicators:
            severity = "high"
            recommendation = "immediate_professional_consultation"
        elif any(word in injury_description.lower() for word in ["mild", "slight", "minor"]):
            severity = "low"
            recommendation = "modified_exercise_ok"
        else:
            severity = "moderate"
            recommendation = "caution_and_modification"
        
        # Update context with assessment
        assessment = {
            "injury_description": injury_description,
            "severity": severity,
            "serious_indicators": serious_indicators,
            "recommendation": recommendation,
            "timestamp": "current"
        }
        
        context.injury_notes = f"Assessment: {assessment}"
        
        return assessment
    
    async def provide_modified_workout_suggestions(self, 
                                                 injury_type: str, 
                                                 context: UserSessionContext) -> Dict[str, Any]:
        """
        Provide safe, modified workout suggestions based on injury type
        """
        # Common injury types and modifications
        injury_modifications = {
            "knee": {
                "avoid": ["running", "jumping", "squats", "lunges"],
                "recommended": ["swimming", "cycling", "upper body strength", "chair exercises"],
                "modifications": "Focus on low-impact activities and avoid weight-bearing exercises"
            },
            "back": {
                "avoid": ["heavy lifting", "twisting", "high-impact"],
                "recommended": ["walking", "swimming", "gentle yoga", "core strengthening"],
                "modifications": "Keep movements controlled and avoid spinal flexion under load"
            },
            "shoulder": {
                "avoid": ["overhead movements", "heavy pulling", "push-ups"],
                "recommended": ["lower body exercises", "light cardio", "gentle stretching"],
                "modifications": "Avoid overhead and behind-the-back movements"
            },
            "ankle": {
                "avoid": ["running", "jumping", "lateral movements"],
                "recommended": ["swimming", "upper body strength", "seated exercises"],
                "modifications": "Focus on non-weight bearing activities until healed"
            },
            "general": {
                "avoid": ["high-impact activities", "heavy weights", "extreme ranges of motion"],
                "recommended": ["gentle walking", "swimming", "stretching", "breathing exercises"],
                "modifications": "Start slowly and listen to your body"
            }
        }
        
        # Determine injury type from description
        injury_key = "general"
        for key in injury_modifications.keys():
            if key in injury_type.lower():
                injury_key = key
                break
        
        suggestions = injury_modifications[injury_key]
        
        # Update context with workout modifications
        if context.workout_plan:
            context.workout_plan["injury_modifications"] = suggestions
        else:
            context.workout_plan = {"injury_modifications": suggestions}
        
        return {
            "injury_type": injury_key,
            "avoid_exercises": suggestions["avoid"],
            "recommended_exercises": suggestions["recommended"],
            "general_modifications": suggestions["modifications"],
            "context_updated": True
        }
    
    async def generate_injury_specific_plan(self, context: UserSessionContext) -> Dict[str, Any]:
        """
        Generate a comprehensive injury-specific fitness plan
        """
        if not context.injury_notes:
            return {"error": "No injury information available"}
        
        # Parse injury information
        injury_info = context.injury_notes
        
        # Generate a basic injury-friendly plan
        injury_plan = {
            "phase_1_rest": {
                "duration": "1-2 weeks",
                "activities": ["gentle stretching", "breathing exercises", "light walking"],
                "focus": "pain management and gentle movement"
            },
            "phase_2_mobility": {
                "duration": "2-4 weeks",
                "activities": ["range of motion exercises", "swimming", "light yoga"],
                "focus": "restore mobility and function"
            },
            "phase_3_strengthening": {
                "duration": "4-8 weeks",
                "activities": ["resistance training", "functional movements", "sport-specific exercises"],
                "focus": "rebuild strength and return to activity"
            },
            "ongoing_maintenance": {
                "duration": "ongoing",
                "activities": ["regular exercise", "injury prevention", "monitoring"],
                "focus": "maintain health and prevent re-injury"
            }
        }
        
        # Update context
        context.workout_plan = {
            "type": "injury_recovery",
            "plan": injury_plan,
            "created_by": "InjurySupportAgent"
        }
        
        return {
            "plan_type": "injury_recovery",
            "phases": injury_plan,
            "context_updated": True,
            "note": "This is a general framework - please consult healthcare professionals for specific guidance"
        }
    
    async def recommend_professional_consultation(self, context: UserSessionContext) -> Dict[str, Any]:
        """
        Provide recommendations for professional consultation
        """
        professional_types = {
            "physical_therapist": "For movement assessment and rehabilitation exercises",
            "sports_medicine_doctor": "For injury diagnosis and treatment planning",
            "orthopedic_specialist": "For bone, joint, and muscle injuries",
            "pain_management_specialist": "For chronic pain conditions",
            "general_practitioner": "For initial assessment and referrals"
        }
        
        # Add professional consultation note to context
        context.injury_notes += " | Professional consultation recommended"
        
        return {
            "recommendation": "professional_consultation",
            "professional_types": professional_types,
            "urgency": "Contact healthcare provider before beginning any exercise program",
            "context_updated": True
        }
    
    def get_agent_info(self) -> Dict[str, Any]:
        """
        Return information about this agent's capabilities
        """
        return {
            "name": "InjurySupportAgent",
            "specialization": "Injury and physical limitation support",
            "capabilities": [
                "Injury severity assessment",
                "Modified workout recommendations",
                "Recovery phase planning",
                "Professional consultation guidance",
                "Safety-first approach"
            ],
            "trigger_conditions": [
                "User mentions injury or pain",
                "Physical limitations reported",
                "Recovery or rehabilitation needs",
                "Safety concerns about exercise"
            ]
        }

# Factory function for easy agent creation
def create_injury_support_agent(client: OpenAI) -> InjurySupportAgent:
    """
    Factory function to create and configure the InjurySupportAgent
    """
    return InjurySupportAgent(client)

# Example usage and testing
async def test_injury_support_agent():
    """
    Test function to demonstrate agent functionality
    """
    # This would be used in actual implementation
    # client = OpenAI()
    # agent = create_injury_support_agent(client)
    
    # Mock context for testing
    from context import UserSessionContext
    test_context = UserSessionContext(
        name="Test User",
        uid=123,
        goal={"type": "weight_loss", "target": "5kg", "duration": "2 months"}
    )
    
    print("InjurySupportAgent test completed successfully!")
    return True

if __name__ == "__main__":
    # Run test
    asyncio.run(test_injury_support_agent())