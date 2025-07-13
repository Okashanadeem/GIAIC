from pydantic import BaseModel, ConfigDict
from typing import Optional, List
from guardrails import WorkoutWeekPlan

class UserSessionContext(BaseModel):
    model_config = ConfigDict(extra="forbid")

    name: str
    uid: int
    goal: Optional[dict] = None
    diet_preferences: Optional[str] = None
    workout_plan: Optional[WorkoutWeekPlan] = None
    meal_plan: Optional[List[str]] = None
    injury_notes: Optional[str] = None
    handoff_logs: List[str] = []
    progress_logs: List[dict] = []