"""
Workout Recommender Tool
Suggests workout plan based on parsed goals and experience level
"""

import asyncio
from typing import Dict, Any, List
from context import UserSessionContext
from guardrails import ToolOutputGuardrail

class WorkoutRecommenderTool:
    """
    This tool creates personalized workout plans based on user goals and fitness level
    """
    
    def __init__(self):
        self.name = "workout_recommender"
        self.description = "Creates personalized workout plans based on goals and fitness level"
        
        # Workout database organized by goal type and experience level
        self.workout_database = {
            "weight_loss": {
                "beginner": {
                    "frequency": "3-4 times per week",
                    "duration": "30-45 minutes",
                    "exercises": [
                        {"name": "Walking", "sets": "1", "reps": "30 minutes", "rest": "N/A"},
                        {"name": "Bodyweight Squats", "sets": "3", "reps": "10-15", "rest": "60s"},
                        {"name": "Push-ups (modified)", "sets": "3", "reps": "5-10", "rest": "60s"},
                        {"name": "Plank", "sets": "3", "reps": "20-30 seconds", "rest": "60s"},
                        {"name": "Mountain Climbers", "sets": "3", "reps": "20", "rest": "60s"}
                    ],
                    "cardio": ["20 minutes brisk walking", "10 minutes cycling"]
                },
                "intermediate": {
                    "frequency": "4-5 times per week",
                    "duration": "45-60 minutes",
                    "exercises": [
                        {"name": "Jogging", "sets": "1", "reps": "25 minutes", "rest": "N/A"},
                        {"name": "Burpees", "sets": "3", "reps": "10-15", "rest": "45s"},
                        {"name": "Jump Squats", "sets": "3", "reps": "15-20", "rest": "45s"},
                        {"name": "Push-ups", "sets": "3", "reps": "15-20", "rest": "45s"},
                        {"name": "High Knees", "sets": "3", "reps": "30 seconds", "rest": "30s"}
                    ],
                    "cardio": ["30 minutes running", "20 minutes HIIT"]
                }
            },
            "muscle_gain": {
                "beginner": {
                    "frequency": "3 times per week",
                    "duration": "45-60 minutes",
                    "exercises": [
                        {"name": "Goblet Squats", "sets": "3", "reps": "8-12", "rest": "90s"},
                        {"name": "Push-ups", "sets": "3", "reps": "8-12", "rest": "90s"},
                        {"name": "Bent-over Rows", "sets": "3", "reps": "8-12", "rest": "90s"},
                        {"name": "Overhead Press", "sets": "3", "reps": "8-12", "rest": "90s"},
                        {"name": "Deadlifts (light)", "sets": "3", "reps": "8-10", "rest": "2 minutes"}
                    ],
                    "cardio": ["10 minutes light cardio warm-up"]
                },
                "intermediate": {
                    "frequency": "4-5 times per week",
                    "duration": "60-75 minutes",
                    "exercises": [
                        {"name": "Barbell Squats", "sets": "4", "reps": "8-10", "rest": "2-3 minutes"},
                        {"name": "Bench Press", "sets": "4", "reps": "8-10", "rest": "2-3 minutes"},
                        {"name": "Deadlifts", "sets": "3", "reps": "5-8", "rest": "3 minutes"},
                        {"name": "Pull-ups", "sets": "3", "reps": "8-12", "rest": "2 minutes"},
                        {"name": "Dips", "sets": "3", "reps": "10-15", "rest": "90s"}
                    ],
                    "cardio": ["15 minutes light cardio"]
                }
            },
            "general_fitness": {
                "beginner": {
                    "frequency": "3-4 times per week",
                    "duration": "30-45 minutes",
                    "exercises": [
                        {"name": "Bodyweight Squats", "sets": "3", "reps": "12-15", "rest": "60s"},
                        {"name": "Push-ups", "sets": "3", "reps": "8-12", "rest": "60s"},
                        {"name": "Lunges", "sets": "3", "reps": "10 each leg", "rest": "60s"},
                        {"name": "Plank", "sets": "3", "reps": "30-45 seconds", "rest": "60s"},
                        {"name": "Jumping Jacks", "sets": "3", "reps": "20", "rest": "60s"}
                    ],
                    "cardio": ["20 minutes moderate cardio"]
                },
                "intermediate": {
                    "frequency": "4-5 times per week",
                    "duration": "45-60 minutes",
                    "exercises": [
                        {"name": "Squats with weights", "sets": "3", "reps": "12-15", "rest": "90s"},
                        {"name": "Push-ups variations", "sets": "3", "reps": "15-20", "rest": "60s"},
                        {"name": "Single-leg deadlifts", "sets": "3", "reps": "8-10 each", "rest": "90s"},
                        {"name": "Pull-ups/Chin-ups", "sets": "3", "reps": "5-10", "rest": "2 minutes"},
                        {"name": "Burpees", "sets": "3", "reps": "10-15", "rest": "90s"}
                    ],
                    "cardio": ["30 minutes varied cardio"]
                }
            }
        }
    
    async def recommend_workout(self, context: UserSessionContext, experience_level: str = "beginner") -> Dict[str, Any]:
        """
        Create a personalized workout plan based on user goals and experience
        """
        print(f"💪 Workout Recommender: Creating workout plan...")
        
        # Step 1: Determine goal type from context
        if not context.goal:
            return {
                "success": False,
                "error": "No goal found",
                "message": "Please set your fitness goal first before creating a workout plan."
            }
        
        goal_type = context.goal.get("goal_type", "general_fitness")
        print(f"🎯 Goal type: {goal_type}")
        print(f"📊 Experience level: {experience_level}")
        
        # Step 2: Generate workout plan
        workout_plan = await self._generate_workout_plan(goal_type, experience_level, context)
        
        # Step 3: Add injury considerations
        if context.injury_notes:
            workout_plan = self._modify_for_injuries(workout_plan, context.injury_notes)
        
        # Step 4: Validate output
        output_validator = ToolOutputGuardrail(
            tool_name=self.name,
            output_data=workout_plan
        )
        
        if not output_validator.validate_output():
            return {
                "success": False,
                "error": "Workout plan generation failed validation",
                "details": output_validator.validation_errors
            }
        
        # Step 5: Update context
        context.workout_plan = workout_plan
        context.add_conversation("system", f"Created {goal_type} workout plan for {experience_level}")
        
        print(f"✅ Workout Recommender: Successfully created workout plan")
        
        return {
            "success": True,
            "workout_plan": workout_plan,
            "goal_type": goal_type,
            "experience_level": experience_level,
            "message": f"I've created a personalized {goal_type.replace('_', ' ')} workout plan for your {experience_level} level!"
        }
    
    async def _generate_workout_plan(self, goal_type: str, experience_level: str, context: UserSessionContext) -> Dict[str, Any]:
        """
        Generate a workout plan based on goal and experience level
        """
        # Simulate async operation
        await asyncio.sleep(0.1)
        
        # Get workout template
        workout_template = self.workout_database.get(goal_type, self.workout_database["general_fitness"])
        plan_data = workout_template.get(experience_level, workout_template["beginner"])
        
        # Create weekly schedule
        weekly_schedule = self._create_weekly_schedule(plan_data, goal_type)
        
        # Add progression plan
        progression = self._create_progression_plan(goal_type, experience_level)
        
        workout_plan = {
            "goal_type": goal_type,
            "experience_level": experience_level,
            "frequency": plan_data["frequency"],
            "duration": plan_data["duration"],
            "exercises": plan_data["exercises"],
            "cardio": plan_data["cardio"],
            "weekly_schedule": weekly_schedule,
            "progression": progression,
            "safety_tips": self._get_safety_tips(),
            "equipment_needed": self._get_equipment_list(plan_data["exercises"]),
            "warm_up": self._get_warm_up_routine(),
            "cool_down": self._get_cool_down_routine()
        }
        
        return workout_plan
    
    def _create_weekly_schedule(self, plan_data: Dict[str, Any], goal_type: str) -> Dict[str, Any]:
        """Create a weekly workout schedule"""
        if goal_type == "weight_loss":
            return {
                "Monday": "Full body strength + 20 min cardio",
                "Tuesday": "30 min cardio",
                "Wednesday": "Full body strength + 15 min cardio",
                "Thursday": "Active recovery (walking)",
                "Friday": "Full body strength + 20 min cardio",
                "Saturday": "Long cardio session",
                "Sunday": "Rest or light stretching"
            }
        elif goal_type == "muscle_gain":
            return {
                "Monday": "Upper body strength",
                "Tuesday": "Lower body strength",
                "Wednesday": "Rest or light cardio",
                "Thursday": "Upper body strength",
                "Friday": "Lower body strength",
                "Saturday": "Full body or weak points",
                "Sunday": "Rest"
            }
        else:  # general_fitness
            return {
                "Monday": "Full body workout",
                "Tuesday": "Cardio + core",
                "Wednesday": "Rest or yoga",
                "Thursday": "Full body workout",
                "Friday": "Cardio + flexibility",
                "Saturday": "Active recovery",
                "Sunday": "Rest"
            }
    
    def _create_progression_plan(self, goal_type: str, experience_level: str) -> List[str]:
        """Create a progression plan for the workout"""
        base_progressions = [
            "Week 1-2: Focus on form and technique",
            "Week 3-4: Increase reps by 2-3 per exercise",
            "Week 5-6: Add weight or increase difficulty",
            "Week 7-8: Increase sets or add new exercises"
        ]
        
        if goal_type == "muscle_gain":
            base_progressions.extend([
                "Week 9-10: Focus on heavier weights, lower reps",
                "Week 11-12: Deload week, then reassess"
            ])
        
        return base_progressions
    
    def _get_safety_tips(self) -> List[str]:
        """Get safety tips for working out"""
        return [
            "Always warm up before starting your workout",
            "Focus on proper form over heavy weights",
            "Listen to your body and rest when needed",
            "Stay hydrated throughout your workout",
            "Cool down and stretch after exercising",
            "Progress gradually to avoid injury"
        ]
    
    def _get_equipment_list(self, exercises: List[Dict[str, str]]) -> List[str]:
        """Generate equipment list based on exercises"""
        equipment = set()
        
        for exercise in exercises:
            name = exercise["name"].lower()
            if "barbell" in name:
                equipment.add("Barbell and weights")
            elif "dumbbell" in name or "weight" in name:
                equipment.add("Dumbbells")
            elif "pull-up" in name or "chin-up" in name:
                equipment.add("Pull-up bar")
            elif "bench" in name:
                equipment.add("Bench")
        
        # Add basic equipment
        equipment.add("Exercise mat")
        equipment.add("Water bottle")
        
        return list(equipment)
    
    def _get_warm_up_routine(self) -> List[str]:
        """Get warm-up routine"""
        return [
            "5 minutes light cardio (marching in place)",
            "Arm circles (10 each direction)",
            "Leg swings (10 each leg)",
            "Hip circles (10 each direction)",
            "Bodyweight squats (10 reps)",
            "Push-up to downward dog (5 reps)"
        ]
    
    def _get_cool_down_routine(self) -> List[str]:
        """Get cool-down routine"""
        return [
            "5 minutes walking to lower heart rate",
            "Hamstring stretch (hold 30 seconds each)",
            "Quad stretch (hold 30 seconds each)",
            "Shoulder stretch (hold 30 seconds each)",
            "Chest stretch (hold 30 seconds)",
            "Deep breathing exercises (2 minutes)"
        ]
    
    def _modify_for_injuries(self, workout_plan: Dict[str, Any], injury_notes: str) -> Dict[str, Any]:
        """Modify workout plan based on injury notes"""
        injury_notes_lower = injury_notes.lower()
        
        # Create modified exercises list
        modified_exercises = []
        
        for exercise in workout_plan["exercises"]:
            exercise_name = exercise["name"].lower()
            
            # Skip or modify exercises based on common injuries
            if "knee" in injury_notes_lower and ("squat" in exercise_name or "lunge" in exercise_name):
                modified_exercises.append({
                    "name": "Seated leg extensions (light)",
                    "sets": exercise["sets"],
                    "reps": exercise["reps"],
                    "rest": exercise["rest"],
                    "note": "Modified for knee injury"
                })
            elif "shoulder" in injury_notes_lower and ("press" in exercise_name or "push" in exercise_name):
                modified_exercises.append({
                    "name": "Isometric exercises",
                    "sets": exercise["sets"],
                    "reps": "Hold 10-15 seconds",
                    "rest": exercise["rest"],
                    "note": "Modified for shoulder injury"
                })
            elif "back" in injury_notes_lower and ("deadlift" in exercise_name or "row" in exercise_name):
                modified_exercises.append({
                    "name": "Gentle core exercises",
                    "sets": exercise["sets"],
                    "reps": exercise["reps"],
                    "rest": exercise["rest"],
                    "note": "Modified for back injury"
                })
            else:
                modified_exercises.append(exercise)
        
        workout_plan["exercises"] = modified_exercises
        workout_plan["injury_modifications"] = f"Plan modified for: {injury_notes}"
        
        return workout_plan
    
    def get_workout_summary(self, context: UserSessionContext) -> str:
        """Generate a summary of the current workout plan"""
        if not context.workout_plan:
            return "No workout plan created yet."
        
        plan = context.workout_plan
        summary = f"Workout Plan Summary:\n"
        summary += f"Goal: {plan['goal_type'].replace('_', ' ').title()}\n"
        summary += f"Level: {plan['experience_level'].title()}\n"
        summary += f"Frequency: {plan['frequency']}\n"
        summary += f"Duration: {plan['duration']}\n"
        summary += f"Exercises: {len(plan['exercises'])} exercises\n"
        
        if plan.get("injury_modifications"):
            summary += f"Modifications: {plan['injury_modifications']}\n"
        
        return summary

# Simple test function
async def test_workout_recommender():
    """Test the workout recommender tool"""
    tool = WorkoutRecommenderTool()
    context = UserSessionContext()
    
    # Set a goal first
    context.goal = {"goal_type": "weight_loss", "quantity": 5, "metric": "kg"}
    
    # Test different experience levels
    experience_levels = ["beginner", "intermediate"]
    
    for level in experience_levels:
        print(f"\n🧪 Testing: {level} level")
        result = await tool.recommend_workout(context, level)
        print(f"Success: {result['success']}")
        if result['success']:
            print(f"Goal type: {result['goal_type']}")
            print(f"Frequency: {result['workout_plan']['frequency']}")

if __name__ == "__main__":
    # Run test if file is executed directly
    asyncio.run(test_workout_recommender())