"""
Meal Planner Tool
Async tool to suggest 7-day meal plan honoring dietary preferences
"""

import asyncio
from typing import Dict, Any, List
from context import UserSessionContext
from guardrails import validate_user_input, ToolOutputGuardrail

class MealPlannerTool:
    """
    This tool creates personalized 7-day meal plans based on user preferences
    """
    
    def __init__(self):
        self.name = "meal_planner"
        self.description = "Creates personalized 7-day meal plans based on dietary preferences"
        
        # Meal database organized by dietary type
        self.meal_database = {
            "vegetarian": {
                "breakfast": [
                    "Oatmeal with berries and nuts",
                    "Greek yogurt with granola",
                    "Vegetable omelet with whole grain toast",
                    "Smoothie bowl with banana and spinach",
                    "Avocado toast with tomatoes"
                ],
                "lunch": [
                    "Quinoa salad with vegetables",
                    "Lentil soup with whole grain bread",
                    "Caprese sandwich with basil",
                    "Buddha bowl with chickpeas",
                    "Vegetable stir-fry with tofu"
                ],
                "dinner": [
                    "Pasta with marinara and vegetables",
                    "Stuffed bell peppers with quinoa",
                    "Vegetable curry with brown rice",
                    "Eggplant parmesan with salad",
                    "Black bean tacos with guacamole"
                ]
            },
            "vegan": {
                "breakfast": [
                    "Chia pudding with almond milk",
                    "Oatmeal with plant milk and fruits",
                    "Smoothie with spinach and banana",
                    "Avocado toast with nutritional yeast",
                    "Quinoa breakfast bowl"
                ],
                "lunch": [
                    "Hummus and vegetable wrap",
                    "Lentil and vegetable soup",
                    "Quinoa salad with tahini dressing",
                    "Buddha bowl with tempeh",
                    "Vegetable sushi bowl"
                ],
                "dinner": [
                    "Lentil curry with brown rice",
                    "Stuffed portobello mushrooms",
                    "Vegetable pasta with cashew cream",
                    "Chickpea and vegetable stir-fry",
                    "Black bean and sweet potato tacos"
                ]
            },
            "keto": {
                "breakfast": [
                    "Scrambled eggs with avocado",
                    "Keto smoothie with coconut milk",
                    "Bacon and eggs with spinach",
                    "Chia seed pudding with berries",
                    "Omelet with cheese and herbs"
                ],
                "lunch": [
                    "Chicken Caesar salad (no croutons)",
                    "Zucchini noodles with pesto",
                    "Tuna salad with avocado",
                    "Cauliflower rice bowl",
                    "Lettuce wrap with turkey"
                ],
                "dinner": [
                    "Grilled salmon with vegetables",
                    "Chicken thighs with broccoli",
                    "Beef stir-fry with low-carb vegetables",
                    "Pork chops with cauliflower mash",
                    "Cod with asparagus"
                ]
            },
            "general": {
                "breakfast": [
                    "Oatmeal with fresh fruit",
                    "Scrambled eggs with toast",
                    "Greek yogurt with berries",
                    "Whole grain cereal with milk",
                    "Banana and peanut butter toast"
                ],
                "lunch": [
                    "Grilled chicken salad",
                    "Turkey and avocado sandwich",
                    "Vegetable soup with bread",
                    "Quinoa bowl with protein",
                    "Tuna salad wrap"
                ],
                "dinner": [
                    "Grilled chicken with vegetables",
                    "Salmon with sweet potato",
                    "Lean beef with brown rice",
                    "Turkey meatballs with pasta",
                    "Baked cod with quinoa"
                ]
            }
        }
    
    async def create_meal_plan(self, context: UserSessionContext, dietary_preferences: str = None) -> Dict[str, Any]:
        """
        Create a 7-day meal plan based on user preferences
        """
        print(f"🍽️ Meal Planner: Creating meal plan...")
        
        # Step 1: Determine dietary type
        if dietary_preferences:
            validation_result = validate_user_input(dietary_preferences, "dietary")
            if validation_result["is_valid"]:
                dietary_data = validation_result["parsed_data"]
                dietary_type = dietary_data.get("dietary_type", "general")
                context.diet_preferences = dietary_preferences
            else:
                dietary_type = "general"
        else:
            dietary_type = "general"
        
        print(f"📋 Dietary type: {dietary_type}")
        
        # Step 2: Create 7-day meal plan
        meal_plan = await self._generate_weekly_plan(dietary_type, context)
        
        # Step 3: Add nutritional guidance
        nutritional_tips = self._get_nutritional_tips(dietary_type, context)
        
        # Step 4: Validate output
        output_validator = ToolOutputGuardrail(
            tool_name=self.name,
            output_data=meal_plan
        )
        
        if not output_validator.validate_output():
            return {
                "success": False,
                "error": "Meal plan generation failed validation",
                "details": output_validator.validation_errors
            }
        
        # Step 5: Update context
        context.meal_plan = [f"Day {i+1}: {day['summary']}" for i, day in enumerate(meal_plan["days"])]
        context.add_conversation("system", f"Created {dietary_type} meal plan")
        
        print(f"✅ Meal Planner: Successfully created 7-day meal plan")
        
        return {
            "success": True,
            "meal_plan": meal_plan,
            "nutritional_tips": nutritional_tips,
            "dietary_type": dietary_type,
            "message": f"I've created a personalized 7-day {dietary_type} meal plan for you!"
        }
    
    async def _generate_weekly_plan(self, dietary_type: str, context: UserSessionContext) -> Dict[str, Any]:
        """
        Generate a 7-day meal plan
        """
        # Simulate async operation
        await asyncio.sleep(0.1)
        
        # Get meals for the dietary type
        meals = self.meal_database.get(dietary_type, self.meal_database["general"])
        
        days = []
        for day_num in range(1, 8):
            day_plan = {
                "day": day_num,
                "date": f"Day {day_num}",
                "breakfast": meals["breakfast"][(day_num - 1) % len(meals["breakfast"])],
                "lunch": meals["lunch"][(day_num - 1) % len(meals["lunch"])],
                "dinner": meals["dinner"][(day_num - 1) % len(meals["dinner"])],
                "snacks": self._get_snacks(dietary_type),
                "water_reminder": "Drink 8 glasses of water",
                "summary": f"{meals['breakfast'][(day_num - 1) % len(meals['breakfast'])]} | {meals['lunch'][(day_num - 1) % len(meals['lunch'])]} | {meals['dinner'][(day_num - 1) % len(meals['dinner'])]}"
            }
            days.append(day_plan)
        
        return {
            "dietary_type": dietary_type,
            "total_days": 7,
            "days": days,
            "shopping_list": self._generate_shopping_list(dietary_type),
            "prep_tips": self._get_prep_tips(dietary_type)
        }
    
    def _get_snacks(self, dietary_type: str) -> List[str]:
        """Get appropriate snacks for dietary type"""
        snack_options = {
            "vegetarian": ["Greek yogurt", "Mixed nuts", "Fruit and cheese", "Hummus with veggies"],
            "vegan": ["Mixed nuts", "Fresh fruit", "Vegetable sticks with hummus", "Smoothie"],
            "keto": ["Cheese cubes", "Nuts", "Avocado", "Hard-boiled eggs"],
            "general": ["Fresh fruit", "Yogurt", "Nuts", "Vegetable sticks"]
        }
        return snack_options.get(dietary_type, snack_options["general"])
    
    def _get_nutritional_tips(self, dietary_type: str, context: UserSessionContext) -> List[str]:
        """Get nutritional tips based on dietary type and goals"""
        tips = []
        
        # Base tips for dietary type
        if dietary_type == "vegetarian":
            tips.extend([
                "Ensure adequate protein from legumes, dairy, and eggs",
                "Include iron-rich foods like spinach and lentils",
                "Consider B12 supplementation"
            ])
        elif dietary_type == "vegan":
            tips.extend([
                "Focus on complete proteins like quinoa and legumes",
                "Include fortified foods for B12 and vitamin D",
                "Eat vitamin C with iron-rich foods for better absorption"
            ])
        elif dietary_type == "keto":
            tips.extend([
                "Keep carbs under 20-30g per day",
                "Include healthy fats like avocados and nuts",
                "Stay hydrated and consider electrolyte balance"
            ])
        else:
            tips.extend([
                "Aim for balanced macronutrients",
                "Include a variety of colorful vegetables",
                "Choose whole grains over refined carbs"
            ])
        
        # Add goal-specific tips
        if context.goal:
            goal_type = context.goal.get("goal_type")
            if goal_type == "weight_loss":
                tips.append("Focus on portion control and calorie-dense foods")
                tips.append("Include protein with each meal to maintain muscle")
            elif goal_type == "muscle_gain":
                tips.append("Increase protein intake to 1.6-2.2g per kg body weight")
                tips.append("Time protein intake around workouts")
        
        return tips
    
    def _generate_shopping_list(self, dietary_type: str) -> List[str]:
        """Generate shopping list for the meal plan"""
        shopping_lists = {
            "vegetarian": [
                "Eggs", "Greek yogurt", "Cheese", "Quinoa", "Lentils",
                "Mixed vegetables", "Fruits", "Nuts", "Olive oil", "Whole grain bread"
            ],
            "vegan": [
                "Almond milk", "Tofu", "Tempeh", "Quinoa", "Lentils",
                "Chickpeas", "Mixed vegetables", "Fruits", "Nuts", "Tahini"
            ],
            "keto": [
                "Eggs", "Chicken", "Salmon", "Avocados", "Cheese",
                "Spinach", "Broccoli", "Cauliflower", "Nuts", "Olive oil"
            ],
            "general": [
                "Chicken breast", "Fish", "Eggs", "Greek yogurt", "Quinoa",
                "Brown rice", "Mixed vegetables", "Fruits", "Nuts", "Olive oil"
            ]
        }
        return shopping_lists.get(dietary_type, shopping_lists["general"])
    
    def _get_prep_tips(self, dietary_type: str) -> List[str]:
        """Get meal prep tips"""
        return [
            "Prepare grains and proteins in bulk on Sunday",
            "Wash and chop vegetables at the beginning of the week",
            "Keep healthy snacks portioned and ready",
            "Cook larger batches and freeze portions",
            "Use a meal planning app to track your meals"
        ]
    
    def get_meal_plan_summary(self, context: UserSessionContext) -> str:
        """Generate a summary of the current meal plan"""
        if not context.meal_plan:
            return "No meal plan created yet."
        
        summary = f"Meal Plan Summary ({context.diet_preferences or 'General'}):\n"
        summary += f"Total days planned: {len(context.meal_plan)}\n"
        
        for i, day in enumerate(context.meal_plan[:3]):  # Show first 3 days
            summary += f"Day {i+1}: {day}\n"
        
        if len(context.meal_plan) > 3:
            summary += f"... and {len(context.meal_plan) - 3} more days\n"
        
        return summary

# Simple test function
async def test_meal_planner():
    """Test the meal planner tool"""
    tool = MealPlannerTool()
    context = UserSessionContext()
    
    # Test cases
    dietary_preferences = [
        "I'm vegetarian",
        "I follow a keto diet",
        "I'm vegan",
        None  # General diet
    ]
    
    for pref in dietary_preferences:
        print(f"\n🧪 Testing: {pref}")
        result = await tool.create_meal_plan(context, pref)
        print(f"Success: {result['success']}")
        if result['success']:
            print(f"Dietary type: {result['dietary_type']}")
            print(f"Days planned: {len(result['meal_plan']['days'])}")

if __name__ == "__main__":
    # Run test if file is executed directly
    asyncio.run(test_meal_planner())