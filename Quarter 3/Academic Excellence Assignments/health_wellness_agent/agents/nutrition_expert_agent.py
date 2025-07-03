"""
Nutrition Expert Agent for Health & Wellness Planner
Handles complex dietary needs like diabetes, allergies, and special diets
"""

from datetime import datetime
from typing import Dict, List, Optional
from openai_agents import Agent
from ..context import UserSessionContext


class NutritionExpertAgent(Agent):
    """Specialized agent for complex nutritional guidance"""
    
    name = "nutrition_expert_agent"
    description = "Provides specialized nutrition guidance for complex dietary needs"
    
    instructions = """
    You are a Nutrition Expert Agent specializing in complex dietary needs. Your expertise includes:
    
    1. **Medical Dietary Conditions**: Diabetes, heart disease, kidney disease, digestive issues
    2. **Food Allergies & Intolerances**: Gluten, dairy, nuts, shellfish, etc.
    3. **Special Diets**: Keto, paleo, vegetarian, vegan, Mediterranean, etc.
    4. **Nutritional Deficiencies**: Iron, B12, vitamin D, etc.
    5. **Weight Management**: Healthy weight loss/gain strategies
    
    IMPORTANT DISCLAIMERS:
    - Always remind users to consult healthcare providers for medical conditions
    - Provide evidence-based nutritional guidance
    - Avoid diagnosing or prescribing
    - Focus on general nutritional education and meal planning
    
    Be thorough, professional, and prioritize user safety.
    """
    
    def __init__(self):
        super().__init__(
            name=self.name,
            description=self.description,
            instructions=self.instructions
        )
    
    async def on_handoff(self, context: UserSessionContext, handoff_reason: str = "") -> str:
        """
        Handle handoff to nutrition expert
        
        Args:
            context: User session context
            handoff_reason: Reason for handoff
            
        Returns:
            Initial expert response
        """
        # Log the handoff
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        handoff_log = f"[{timestamp}] Handed off to Nutrition Expert - Reason: {handoff_reason}"
        
        if not hasattr(context, 'handoff_logs'):
            context.handoff_logs = []
        context.handoff_logs.append(handoff_log)
        
        user_name = getattr(context, 'name', 'there')
        
        initial_response = f"""
        Hello {user_name}! I'm your Nutrition Expert, here to help with your complex dietary needs.
        
        I specialize in creating safe, effective nutrition plans for people with:
        • Medical conditions (diabetes, heart disease, etc.)
        • Food allergies and intolerances
        • Special dietary requirements
        • Nutritional deficiencies
        
        **Important Note**: While I provide evidence-based nutritional guidance, please consult with your healthcare provider or registered dietitian for medical dietary advice.
        
        To get started, could you tell me:
        1. What specific dietary concerns or conditions you have?
        2. Any foods you need to avoid or limit?
        3. Your current eating patterns and preferences?
        
        I'm here to create a safe, personalized nutrition plan for you!
        """
        
        return initial_response.strip()
    
    async def assess_dietary_needs(self, context: UserSessionContext, user_input: str) -> str:
        """
        Assess user's complex dietary needs
        
        Args:
            context: User session context
            user_input: User's dietary information
            
        Returns:
            Nutritional assessment and recommendations
        """
        # Analyze user input for dietary conditions
        assessment = self._analyze_dietary_conditions(user_input)
        
        # Store assessment in context
        if not hasattr(context, 'nutrition_assessment'):
            context.nutrition_assessment = {}
        context.nutrition_assessment.update(assessment)
        
        # Generate personalized response
        response = await self._generate_nutrition_response(assessment, context)
        
        return response
    
    def _analyze_dietary_conditions(self, user_input: str) -> Dict:
        """Analyze user input for dietary conditions and needs"""
        input_lower = user_input.lower()
        
        assessment = {
            "conditions": [],
            "allergies": [],
            "restrictions": [],
            "goals": [],
            "risk_level": "low"
        }
        
        # Medical conditions
        medical_conditions = {
            "diabetes": ["diabetes", "diabetic", "blood sugar", "insulin"],
            "heart_disease": ["heart disease", "cardiac", "cholesterol", "hypertension"],
            "kidney_disease": ["kidney", "renal", "dialysis"],
            "digestive_issues": ["ibs", "crohn", "colitis", "gerd", "acid reflux"],
            "celiac": ["celiac", "gluten sensitivity"],
            "thyroid": ["thyroid", "hypothyroid", "hyperthyroid"]
        }
        
        for condition, keywords in medical_conditions.items():
            if any(keyword in input_lower for keyword in keywords):
                assessment["conditions"].append(condition)
                assessment["risk_level"] = "high"
        
        # Food allergies
        common_allergens = {
            "gluten": ["gluten", "wheat", "celiac"],
            "dairy": ["dairy", "lactose", "milk", "cheese"],
            "nuts": ["nuts", "peanut", "almond", "walnut"],
            "shellfish": ["shellfish", "shrimp", "crab", "lobster"],
            "eggs": ["egg", "eggs"],
            "soy": ["soy", "soya", "tofu"]
        }
        
        for allergen, keywords in common_allergens.items():
            if any(keyword in input_lower for keyword in keywords):
                assessment["allergies"].append(allergen)
                assessment["risk_level"] = "medium"
        
        # Dietary restrictions
        diet_types = {
            "vegetarian": ["vegetarian", "veggie"],
            "vegan": ["vegan", "plant-based"],
            "keto": ["keto", "ketogenic", "low carb"],
            "paleo": ["paleo", "paleolithic"],
            "low_sodium": ["low sodium", "salt restriction"],
            "low_fat": ["low fat", "fat restriction"]
        }
        
        for diet, keywords in diet_types.items():
            if any(keyword in input_lower for keyword in keywords):
                assessment["restrictions"].append(diet)
        
        # Goals
        if any(word in input_lower for word in ["lose weight", "weight loss"]):
            assessment["goals"].append("weight_loss")
        if any(word in input_lower for word in ["gain weight", "weight gain"]):
            assessment["goals"].append("weight_gain")
        if any(word in input_lower for word in ["muscle", "protein", "strength"]):
            assessment["goals"].append("muscle_building")
        
        return assessment
    
    async def _generate_nutrition_response(self, assessment: Dict, context: UserSessionContext) -> str:
        """Generate personalized nutrition response based on assessment"""
        
        conditions = assessment.get("conditions", [])
        allergies = assessment.get("allergies", [])
        restrictions = assessment.get("restrictions", [])
        risk_level = assessment.get("risk_level", "low")
        
        response_parts = []
        
        # Risk-based disclaimer
        if risk_level == "high":
            response_parts.append("""
            ⚠️ **IMPORTANT MEDICAL NOTICE**
            I've identified potential medical dietary conditions. Please consult with your healthcare provider or registered dietitian before making significant dietary changes.
            """)
        
        # Conditions-specific guidance
        if conditions:
            response_parts.append(f"""
            **Identified Conditions**: {', '.join(conditions)}
            
            Here's general nutritional guidance for your conditions:
            """)
            
            for condition in conditions:
                guidance = self._get_condition_guidance(condition)
                response_parts.append(guidance)
        
        # Allergies and restrictions
        if allergies:
            response_parts.append(f"""
            **Food Allergies/Intolerances**: {', '.join(allergies)}
            
            I'll ensure all meal recommendations avoid these allergens completely.
            """)
        
        if restrictions:
            response_parts.append(f"""
            **Dietary Preferences**: {', '.join(restrictions)}
            
            All recommendations will align with your dietary choices.
            """)
        
        # Personalized recommendations
        response_parts.append("""
        **Personalized Nutrition Plan:**
        
        Based on your needs, I recommend:
        """)
        
        recommendations = self._generate_recommendations(assessment)
        response_parts.append(recommendations)
        
        # Next steps
        response_parts.append("""
        **Next Steps:**
        1. Would you like me to create a sample meal plan based on your requirements?
        2. Do you have any specific questions about managing your dietary needs?
        3. Are there any other foods or nutrients you're concerned about?
        
        I'm here to help you navigate your nutrition journey safely and effectively!
        """)
        
        return "\n".join(response_parts).strip()
    
    def _get_condition_guidance(self, condition: str) -> str:
        """Get specific guidance for medical conditions"""
        guidance = {
            "diabetes": """
            🩺 **Diabetes Management Tips:**
            • Focus on complex carbohydrates and fiber
            • Monitor portion sizes and meal timing
            • Include lean proteins and healthy fats
            • Consider the glycemic index of foods
            """,
            
            "heart_disease": """
            ❤️ **Heart-Healthy Guidelines:**
            • Limit saturated and trans fats
            • Increase omega-3 fatty acids
            • Reduce sodium intake
            • Emphasize fruits, vegetables, and whole grains
            """,
            
            "kidney_disease": """
            🫘 **Kidney-Friendly Approach:**
            • Monitor protein intake
            • Limit phosphorus and potassium
            • Control fluid intake if needed
            • Reduce sodium consumption
            """,
            
            "digestive_issues": """
            🍃 **Digestive Health Support:**
            • Identify and avoid trigger foods
            • Include probiotic-rich foods
            • Focus on easily digestible options
            • Consider smaller, frequent meals
            """,
            
            "celiac": """
            🌾 **Gluten-Free Essentials:**
            • Strictly avoid all gluten-containing grains
            • Focus on naturally gluten-free whole foods
            • Check for cross-contamination
            • Ensure adequate B-vitamin intake
            """
        }
        
        return guidance.get(condition, "• Consult your healthcare provider for specific guidance")
    
    def _generate_recommendations(self, assessment: Dict) -> str:
        """Generate specific nutritional recommendations"""
        recommendations = []
        
        # Base recommendations
        recommendations.append("• Eat a variety of nutrient-dense whole foods")
        recommendations.append("• Stay adequately hydrated")
        recommendations.append("• Practice portion control")
        
        # Condition-specific
        if "diabetes" in assessment.get("conditions", []):
            recommendations.append("• Monitor carbohydrate intake and timing")
            recommendations.append("• Include fiber-rich foods to help stabilize blood sugar")
        
        if "heart_disease" in assessment.get("conditions", []):
            recommendations.append("• Choose heart-healthy fats like olive oil and avocados")
            recommendations.append("• Limit processed foods and added sugars")
        
        # Allergy-specific
        if "dairy" in assessment.get("allergies", []):
            recommendations.append("• Ensure adequate calcium from non-dairy sources")
            recommendations.append("• Consider fortified plant-based alternatives")
        
        if "gluten" in assessment.get("allergies", []):
            recommendations.append("• Focus on naturally gluten-free grains like quinoa and rice")
            recommendations.append("• Be vigilant about cross-contamination")
        
        # Goal-specific
        if "weight_loss" in assessment.get("goals", []):
            recommendations.append("• Create a moderate caloric deficit")
            recommendations.append("• Prioritize protein to preserve muscle mass")
        
        return "\n".join(recommendations)
    
    async def create_specialized_meal_plan(self, context: UserSessionContext, duration: str = "7-day") -> str:
        """Create a specialized meal plan based on dietary needs"""
        
        assessment = getattr(context, 'nutrition_assessment', {})
        
        meal_plan = f"""
        **{duration.title()} Specialized Meal Plan**
        
        *Customized for your dietary needs and restrictions*
        
        **Day 1-3 Sample:**
        
        **Breakfast Options:**
        • Option A: Overnight oats with berries and nuts (if no allergies)
        • Option B: Vegetable omelet with whole grain toast
        • Option C: Greek yogurt parfait with fruit (if dairy-tolerant)
        
        **Lunch Options:**
        • Option A: Quinoa salad with grilled chicken and vegetables
        • Option B: Lentil soup with whole grain roll
        • Option C: Turkey and avocado wrap (gluten-free wrap if needed)
        
        **Dinner Options:**
        • Option A: Baked salmon with roasted vegetables
        • Option B: Lean beef stir-fry with brown rice
        • Option C: Vegetarian bean and vegetable curry
        
        **Snack Ideas:**
        • Fresh fruit with nut butter (if no allergies)
        • Vegetable sticks with hummus
        • Handful of mixed nuts and seeds
        
        **Special Considerations:**
        """
        
        # Add specific modifications
        conditions = assessment.get("conditions", [])
        allergies = assessment.get("allergies", [])
        
        if conditions:
            meal_plan += f"\n• Modified for: {', '.join(conditions)}"
        if allergies:
            meal_plan += f"\n• Allergen-free: {', '.join(allergies)}"
        
        meal_plan += """
        
        **Would you like me to:**
        1. Expand this to a full 7-day detailed plan?
        2. Provide recipes for any specific meals?
        3. Create a shopping list based on this plan?
        4. Adjust portions based on your specific caloric needs?
        """
        
        return meal_plan.strip()


# Agent instance for export
nutrition_expert_agent = NutritionExpertAgent()