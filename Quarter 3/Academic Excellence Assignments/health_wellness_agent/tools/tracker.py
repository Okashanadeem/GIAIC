"""
Progress Tracker Tool for Health & Wellness Planner Agent
Tracks user progress and updates session context
"""

import asyncio
from datetime import datetime
from typing import Dict, List, Optional
from pydantic import BaseModel, Field
from openai_agents import Tool

from ..context import UserSessionContext
from ..guardrails import validate_progress_input, validate_progress_output


class ProgressUpdate(BaseModel):
    """Model for progress update input"""
    metric: str = Field(..., description="What metric to update (weight, workout_count, etc.)")
    value: str = Field(..., description="New value for the metric")
    notes: Optional[str] = Field(None, description="Optional notes about the progress")


class ProgressSummary(BaseModel):
    """Model for progress summary output"""
    total_updates: int = Field(..., description="Total number of progress updates")
    recent_updates: List[Dict[str, str]] = Field(..., description="List of recent progress entries")
    motivational_message: str = Field(..., description="Encouraging message based on progress")
    suggestions: List[str] = Field(..., description="Suggestions for continued progress")


class ProgressTrackerTool(Tool):
    """Tool for tracking user progress and updating context"""
    
    name = "progress_tracker"
    description = "Track user progress updates and provide motivational feedback"
    
    async def run(self, progress_update: ProgressUpdate, context) -> ProgressSummary:
        """
        Process progress updates and provide motivational feedback
        
        Args:
            progress_update: The progress update data
            context: User session context
            
        Returns:
            ProgressSummary with updates and motivational content
        """
        # Validate input
        validate_progress_input(progress_update.dict())
        
        # Get current timestamp
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        
        # Create progress entry
        progress_entry = {
            "timestamp": timestamp,
            "metric": progress_update.metric,
            "value": progress_update.value,
            "notes": progress_update.notes or ""
        }
        
        # Add to context progress logs
        if not hasattr(context, 'progress_logs'):
            context.progress_logs = []
        context.progress_logs.append(progress_entry)
        
        # Generate motivational message based on progress
        motivational_message = self._generate_motivational_message(
            progress_update.metric, 
            progress_update.value,
            len(context.progress_logs)
        )
        
        # Generate suggestions
        suggestions = self._generate_suggestions(progress_update.metric, context.progress_logs)
        
        # Get recent updates (last 5)
        recent_updates = context.progress_logs[-5:]
        
        # Create summary
        summary = ProgressSummary(
            total_updates=len(context.progress_logs),
            recent_updates=recent_updates,
            motivational_message=motivational_message,
            suggestions=suggestions
        )
        
        # Validate output
        validate_progress_output(summary.dict())
        
        # Add some async processing delay to simulate real tracking
        await asyncio.sleep(0.5)
        
        return summary
    
    def _generate_motivational_message(self, metric: str, value: str, total_updates: int) -> str:
        """Generate motivational message based on progress"""
        messages = {
            "weight": [
                f"Great progress! You're tracking your weight consistently. Current: {value}",
                f"Keep up the excellent work! Weight update recorded: {value}",
                f"Consistency is key! Your {total_updates} updates show real dedication."
            ],
            "workout_count": [
                f"Amazing! You've completed {value} workouts. Your consistency is inspiring!",
                f"You're crushing your fitness goals! {value} workouts logged.",
                f"Fantastic dedication! {value} workouts show your commitment to health."
            ],
            "steps": [
                f"Excellent daily activity! {value} steps is a great achievement.",
                f"You're staying active! {value} steps logged successfully.",
                f"Keep moving! {value} steps brings you closer to your goals."
            ]
        }
        
        metric_messages = messages.get(metric.lower(), [
            f"Great job tracking your {metric}! Current value: {value}",
            f"Consistency in tracking {metric} will help you reach your goals!",
            f"You're making progress! {metric} update: {value}"
        ])
        
        # Choose message based on number of updates
        message_index = min(total_updates % len(metric_messages), len(metric_messages) - 1)
        return metric_messages[message_index]
    
    def _generate_suggestions(self, metric: str, progress_logs: List[Dict]) -> List[str]:
        """Generate suggestions based on progress history"""
        base_suggestions = [
            "Keep maintaining your tracking consistency",
            "Consider setting weekly mini-goals",
            "Share your progress with a friend for accountability"
        ]
        
        metric_suggestions = {
            "weight": [
                "Remember that weight can fluctuate daily - focus on weekly trends",
                "Combine weight tracking with body measurements for better insights",
                "Stay hydrated and weigh yourself at the same time daily"
            ],
            "workout_count": [
                "Try to gradually increase workout intensity",
                "Mix different types of exercises to prevent boredom",
                "Rest days are just as important as workout days"
            ],
            "steps": [
                "Try taking stairs instead of elevators",
                "Park farther away or get off transit one stop early",
                "Set hourly reminders to take short walks"
            ]
        }
        
        suggestions = base_suggestions.copy()
        if metric.lower() in metric_suggestions:
            suggestions.extend(metric_suggestions[metric.lower()][:2])
        
        return suggestions[:4]  # Return max 4 suggestions


# Tool instance for export
progress_tracker_tool = ProgressTrackerTool()