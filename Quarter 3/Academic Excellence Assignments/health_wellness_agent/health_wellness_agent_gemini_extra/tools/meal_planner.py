# tools/meal_planner.py

def get_meal_plan(preference="none"):
    if "vegetarian" in preference:
        return ["Veggie Stir Fry", "Lentil Soup", "Grilled Tofu"]
    elif "diabetic" in preference:
        return ["Low-GI salad", "Quinoa bowl", "Steamed fish"]
    return ["Omelet", "Chicken Wrap", "Fruit Smoothie"]
