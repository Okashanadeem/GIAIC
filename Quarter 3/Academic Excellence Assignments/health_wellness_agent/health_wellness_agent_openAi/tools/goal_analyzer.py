"""
Goal Analyzer Tool
Converts user goals into structured format using input/output guardrails
"""

import asyncio
from typing import Dict, Any
from context import UserSessionContext
from guardrails import validate_user_input, ToolOutputGuardrail

class GoalAnalyzerTool:
    """
    This tool analyzes user health goals and converts them into structured data
    """
    
    def __init__(self):
        self.name = "goal_analyzer"
        self.description = "Analyzes user health goals and creates structured goal data"
    
    async def analyze_goal(self, user_input: str, context: UserSessionContext) -> Dict[str, Any]:
        """
        Main function to analyze user goals
        """
        print(f"🎯 Goal Analyzer: Processing goal - {user_input}")
        
        # Step 1: Validate input using guardrails
        validation_result = validate_user_input(user_input, "goal")
        
        if not validation_result["is_valid"]:
            return {
                "success": False,
                "error": "Invalid goal format",
                "details": validation_result["errors"],
                "suggestion": "Please provide a goal like 'lose 5kg in 2 months' or 'build muscle'"
            }
        
        # Step 2: Extract structured goal data
        goal_data = validation_result["parsed_data"]
        
        # Step 3: Enhance goal data with recommendations
        enhanced_goal = self._enhance_goal_data(goal_data)
        
        # Step 4: Validate output using guardrails
        output_validator = ToolOutputGuardrail(
            tool_name=self.name,
            output_data=enhanced_goal
        )
        
        if not output_validator.validate_output():
            return {
                "success": False,
                "error": "Goal analysis failed validation",
                "details": output_validator.validation_errors
            }
        
        # Step 5: Update context with goal
        context.goal = enhanced_goal
        context.add_conversation("system", f"Goal analyzed: {enhanced_goal['goal_type']}")
        
        print(f"✅ Goal Analyzer: Successfully analyzed goal - {enhanced_goal['goal_type']}")
        
        return {
            "success": True,
            "goal_data": enhanced_goal,
            "message": f"Great! I've analyzed your goal to {enhanced_goal['goal_type']}. Let me help you create a plan!"
        }
    
    def _enhance_goal_data(self, goal_data: Dict[str, Any]) -> Dict[str, Any]:
        """
        Add recommendations and structure to goal data
        """
        enhanced = goal_data.copy()
        
        # Add timeline recommendations
        if enhanced["goal_type"] == "weight_loss":
            enhanced["recommended_timeline"] = "8-12 weeks for sustainable results"
            enhanced["weekly_target"] = "0.5-1kg per week"
            enhanced["focus_areas"] = ["calorie deficit", "cardio exercise", "strength training"]
        
        elif enhanced["goal_type"] == "muscle_gain":
            enhanced["recommended_timeline"] = "12-16 weeks for noticeable results"
            enhanced["weekly_target"] = "0.25-0.5kg muscle gain per week"
            enhanced["focus_areas"] = ["strength training", "protein intake", "progressive overload"]
        
        elif enhanced["goal_type"] == "general_fitness":
            enhanced["recommended_timeline"] = "6-8 weeks for fitness improvements"
            enhanced["weekly_target"] = "consistent exercise 3-4 times per week"
            enhanced["focus_areas"] = ["cardio health", "strength", "flexibility"]
        
        else:
            enhanced["recommended_timeline"] = "8-12 weeks"
            enhanced["weekly_target"] = "consistent progress"
            enhanced["focus_areas"] = ["balanced nutrition", "regular exercise"]
        
        # Add difficulty level
        if enhanced["quantity"] and enhanced["duration"]:
            # Simple difficulty calculation based on quantity and time
            if enhanced["quantity"] > 10 or "month" in str(enhanced["duration"]):
                enhanced["difficulty"] = "challenging"
            else:
                enhanced["difficulty"] = "moderate"
        else:
            enhanced["difficulty"] = "moderate"
        
        # Add next steps
        enhanced["next_steps"] = [
            "Set up meal planning",
            "Create workout schedule",
            "Track progress weekly"
        ]
        
        return enhanced
    
    def get_goal_summary(self, context: UserSessionContext) -> str:
        """
        Generate a summary of the user's goal
        """
        if not context.goal:
            return "No goal set yet."
        
        goal = context.goal
        summary = f"Goal: {goal['goal_type'].replace('_', ' ').title()}\n"
        
        if goal.get("quantity"):
            summary += f"Target: {goal['quantity']} {goal.get('metric', '')}\n"
        
        if goal.get("duration"):
            summary += f"Timeline: {goal['duration']}\n"
        
        if goal.get("difficulty"):
            summary += f"Difficulty: {goal['difficulty']}\n"
        
        return summary

# Simple test function
async def test_goal_analyzer():
    """Test the goal analyzer tool"""
    tool = GoalAnalyzerTool()
    context = UserSessionContext()
    
    # Test cases
    test_goals = [
        "I want to lose 5kg in 2 months",
        "Build muscle and get stronger",
        "Improve my fitness level"
    ]
    
    for goal in test_goals:
        print(f"\n🧪 Testing: {goal}")
        result = await tool.analyze_goal(goal, context)
        print(f"Result: {result}")

if __name__ == "__main__":
    # Run test if file is executed directly
    asyncio.run(test_goal_analyzer())