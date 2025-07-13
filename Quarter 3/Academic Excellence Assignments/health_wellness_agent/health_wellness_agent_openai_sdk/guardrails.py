from pydantic import BaseModel, Field, ConfigDict
from typing import Literal, Dict, List

class Goal(BaseModel):
    objective: Literal["lose", "gain", "maintain"]
    quantity: float = Field(..., gt=0)
    metric: Literal["kg", "lbs"]
    duration_months: int = Field(..., gt=0)

class GoalInput(BaseModel):
    model_config = ConfigDict(extra="forbid")
    goal: Goal


class MealPlanOutput(BaseModel):
    model_config = ConfigDict(extra="forbid")
    plan: List[str]

class WorkoutWeekPlan(BaseModel):
    model_config = ConfigDict(extra="forbid")
    week_1: List[str]
    week_2: List[str]

class WorkoutPlanOutput(BaseModel):
    model_config = ConfigDict(extra="forbid")
    plan: WorkoutWeekPlan