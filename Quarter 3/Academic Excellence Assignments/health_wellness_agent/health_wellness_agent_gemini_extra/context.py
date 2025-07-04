# context.py

from typing import Optional, List, Dict
from pydantic import BaseModel

class UserSessionContext(BaseModel):
    name: Optional[str] = None
    uid: Optional[int] = 1
    goal: Optional[dict] = None
    diet_preferences: Optional[str] = None
    workout_plan: Optional[dict] = None
    meal_plan: Optional[List[str]] = None
    injury_notes: Optional[str] = None
    handoff_logs: List[str] = []
    progress_logs: List[Dict[str, str]] = []
