# tools/workout_recommender.py

def get_workout_plan(goal_type):
    if goal_type == "weight_loss":
        return ["Cardio 30 min", "HIIT 20 min", "Jog 3km"]
    elif goal_type == "muscle_gain":
        return ["Weight Lifting", "Pushups", "Squats"]
    return ["Yoga", "Stretching", "Walk"]
