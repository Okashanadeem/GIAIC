"""
User Session Context for Health & Wellness Planner
This file defines the data structure that holds all user information throughout the conversation.
"""

from pydantic import BaseModel
from typing import Optional, List, Dict, Any
from datetime import datetime

class UserSessionContext(BaseModel):
    """
    This class stores all user information during their session.
    It's shared across all tools and agents to maintain conversation context.
    """
    # Basic user information
    name: str = "User"
    uid: int = 1
    
    # Health goals and preferences
    goal: Optional[Dict[str, Any]] = None
    diet_preferences: Optional[str] = None
    workout_plan: Optional[Dict[str, Any]] = None
    meal_plan: Optional[List[str]] = None
    injury_notes: Optional[str] = None
    
    # Session tracking
    handoff_logs: List[str] = []
    progress_logs: List[Dict[str, str]] = []
    conversation_history: List[Dict[str, str]] = []
    
    # Timestamps
    created_at: datetime = datetime.now()
    last_updated: datetime = datetime.now()
    
    def add_conversation(self, role: str, message: str):
        """Add a message to conversation history"""
        self.conversation_history.append({
            "role": role,
            "message": message,
            "timestamp": datetime.now().isoformat()
        })
        self.last_updated = datetime.now()
    
    def add_handoff_log(self, agent_name: str, reason: str):
        """Log when we handoff to another agent"""
        log_entry = f"{datetime.now().isoformat()}: Handoff to {agent_name} - {reason}"
        self.handoff_logs.append(log_entry)
        self.last_updated = datetime.now()
    
    def add_progress_log(self, activity: str, details: str):
        """Log user progress"""
        self.progress_logs.append({
            "timestamp": datetime.now().isoformat(),
            "activity": activity,
            "details": details
        })
        self.last_updated = datetime.now()
    
    def get_summary(self) -> str:
        """Get a summary of the user's current state"""
        summary = f"User: {self.name}\n"
        
        if self.goal:
            summary += f"Goal: {self.goal}\n"
        
        if self.diet_preferences:
            summary += f"Diet: {self.diet_preferences}\n"
        
        if self.injury_notes:
            summary += f"Injuries: {self.injury_notes}\n"
        
        if self.workout_plan:
            summary += f"Workout Plan: {self.workout_plan.get('type', 'Custom')}\n"
        
        if self.meal_plan:
            summary += f"Meal Plan: {len(self.meal_plan)} days planned\n"
        
        return summary