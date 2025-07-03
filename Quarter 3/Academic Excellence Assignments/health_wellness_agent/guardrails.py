"""
Guardrails for Input and Output Validation
This ensures user inputs are safe and tool outputs are properly structured.
"""

import re
from typing import Dict, Any, Optional, List
from pydantic import BaseModel, validator

class GoalInputGuardrail(BaseModel):
    """
    Validates goal input format: quantity, metric, duration
    Example: "lose 5kg in 2 months"
    """
    raw_input: str
    quantity: Optional[float] = None
    metric: Optional[str] = None
    duration: Optional[str] = None
    goal_type: Optional[str] = None
    
    @validator('raw_input')
    def validate_input_format(cls, v):
        if not v or len(v.strip()) < 3:
            raise ValueError("Goal input too short. Please provide more details.")
        
        # Block potentially harmful inputs
        harmful_keywords = ['delete', 'drop', 'remove', 'hack', 'exploit']
        if any(keyword in v.lower() for keyword in harmful_keywords):
            raise ValueError("Invalid input detected. Please provide a health goal.")
        
        return v.strip()
    
    def parse_goal(self) -> Dict[str, Any]:
        """Extract structured goal information from natural language"""
        text = self.raw_input.lower()
        
        # Extract numbers (quantity)
        numbers = re.findall(r'\d+(?:\.\d+)?', text)
        if numbers:
            self.quantity = float(numbers[0])
        
        # Extract metrics (weight, muscle, etc.)
        weight_keywords = ['kg', 'pounds', 'lbs', 'weight', 'kilos']
        muscle_keywords = ['muscle', 'strength', 'bulk', 'mass']
        fitness_keywords = ['fitness', 'cardio', 'endurance', 'stamina']
        
        if any(keyword in text for keyword in weight_keywords):
            self.metric = "weight"
        elif any(keyword in text for keyword in muscle_keywords):
            self.metric = "muscle"
        elif any(keyword in text for keyword in fitness_keywords):
            self.metric = "fitness"
        else:
            self.metric = "general"
        
        # Extract duration
        duration_patterns = [
            r'(\d+)\s*(day|days|week|weeks|month|months|year|years)',
            r'(daily|weekly|monthly)'
        ]
        
        for pattern in duration_patterns:
            match = re.search(pattern, text)
            if match:
                self.duration = match.group(0)
                break
        
        # Determine goal type
        if 'lose' in text or 'weight loss' in text:
            self.goal_type = "weight_loss"
        elif 'gain' in text or 'build' in text or 'muscle' in text:
            self.goal_type = "muscle_gain"
        elif 'maintain' in text:
            self.goal_type = "maintenance"
        else:
            self.goal_type = "general_fitness"
        
        return {
            "quantity": self.quantity,
            "metric": self.metric,
            "duration": self.duration,
            "goal_type": self.goal_type,
            "raw_input": self.raw_input
        }

class DietaryInputGuardrail(BaseModel):
    """Validates dietary preferences and restrictions"""
    raw_input: str
    dietary_type: Optional[str] = None
    restrictions: List[str] = []
    allergies: List[str] = []
    
    @validator('raw_input')
    def validate_dietary_input(cls, v):
        if not v:
            return v
        
        # Clean input
        clean_input = v.strip().lower()
        
        # Block harmful content
        if any(word in clean_input for word in ['poison', 'toxic', 'harmful']):
            raise ValueError("Invalid dietary input. Please provide valid dietary preferences.")
        
        return v
    
    def parse_dietary_preferences(self) -> Dict[str, Any]:
        """Extract dietary information"""
        text = self.raw_input.lower()
        
        # Common dietary types
        dietary_types = {
            'vegetarian': ['vegetarian', 'veggie'],
            'vegan': ['vegan'],
            'keto': ['keto', 'ketogenic'],
            'paleo': ['paleo'],
            'mediterranean': ['mediterranean'],
            'low-carb': ['low carb', 'low-carb'],
            'gluten-free': ['gluten free', 'gluten-free', 'celiac']
        }
        
        for diet_type, keywords in dietary_types.items():
            if any(keyword in text for keyword in keywords):
                self.dietary_type = diet_type
                break
        
        # Extract allergies
        allergy_keywords = ['allergic', 'allergy', 'intolerant', 'intolerance']
        common_allergens = ['nuts', 'dairy', 'eggs', 'shellfish', 'soy', 'wheat']
        
        if any(keyword in text for keyword in allergy_keywords):
            for allergen in common_allergens:
                if allergen in text:
                    self.allergies.append(allergen)
        
        return {
            "dietary_type": self.dietary_type,
            "restrictions": self.restrictions,
            "allergies": self.allergies,
            "raw_input": self.raw_input
        }

class ToolOutputGuardrail(BaseModel):
    """Ensures tool outputs are properly structured"""
    tool_name: str
    output_data: Any
    is_valid: bool = True
    validation_errors: List[str] = []
    
    def validate_output(self) -> bool:
        """Validate that tool output is properly structured"""
        try:
            if self.tool_name == "goal_analyzer":
                # Should return a dictionary with goal structure
                if not isinstance(self.output_data, dict):
                    self.validation_errors.append("Goal analyzer should return a dictionary")
                    self.is_valid = False
                elif 'goal_type' not in self.output_data:
                    self.validation_errors.append("Goal analyzer missing goal_type")
                    self.is_valid = False
            
            elif self.tool_name == "meal_planner":
                # Should return a list of meal plans
                if not isinstance(self.output_data, (list, dict)):
                    self.validation_errors.append("Meal planner should return a list or dict")
                    self.is_valid = False
            
            elif self.tool_name == "workout_recommender":
                # Should return workout plan structure
                if not isinstance(self.output_data, dict):
                    self.validation_errors.append("Workout recommender should return a dictionary")
                    self.is_valid = False
                elif 'exercises' not in self.output_data:
                    self.validation_errors.append("Workout plan missing exercises")
                    self.is_valid = False
            
            return self.is_valid
            
        except Exception as e:
            self.validation_errors.append(f"Validation error: {str(e)}")
            self.is_valid = False
            return False

def validate_user_input(input_text: str, input_type: str = "general") -> Dict[str, Any]:
    """
    Main validation function for user inputs
    """
    try:
        if input_type == "goal":
            guardrail = GoalInputGuardrail(raw_input=input_text)
            return {
                "is_valid": True,
                "parsed_data": guardrail.parse_goal(),
                "errors": []
            }
        
        elif input_type == "dietary":
            guardrail = DietaryInputGuardrail(raw_input=input_text)
            return {
                "is_valid": True,
                "parsed_data": guardrail.parse_dietary_preferences(),
                "errors": []
            }
        
        else:
            # General validation
            if len(input_text.strip()) < 2:
                return {
                    "is_valid": False,
                    "parsed_data": None,
                    "errors": ["Input too short"]
                }
            
            return {
                "is_valid": True,
                "parsed_data": {"raw_input": input_text.strip()},
                "errors": []
            }
    
    except ValueError as e:
        return {
            "is_valid": False,
            "parsed_data": None,
            "errors": [str(e)]
        }
    except Exception as e:
        return {
            "is_valid": False,
            "parsed_data": None,
            "errors": [f"Unexpected error: {str(e)}"]
        }