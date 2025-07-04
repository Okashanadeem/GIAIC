# tools/goal_analyzer.py

import re

def analyze_goal(text: str):
    match = re.search(r"(lose|gain) (\d+)\s*(kg|pounds|lbs) in (\d+) (weeks|months)", text.lower())
    if match:
        return {
            "type": "weight_loss" if "lose" in match.group(1) else "muscle_gain",
            "amount": f"{match.group(2)} {match.group(3)}",
            "duration": f"{match.group(4)} {match.group(5)}",
            "details": text
        }
    return {"type": "general", "details": text}
