"""
Check-in Scheduler Tool
Schedules recurring weekly progress checks and reminders
"""

import asyncio
from datetime import datetime, timedelta
from typing import Dict, Any, List
from context import UserSessionContext

class CheckinSchedulerTool:
    """
    This tool schedules and manages progress check-ins and reminders
    """
    
    def __init__(self):
        self.name = "checkin_scheduler"
        self.description = "Schedules recurring weekly progress checks and reminders"
    
    async def schedule_checkins(self, context: UserSessionContext, checkin_frequency: str = "weekly") -> Dict[str, Any]:
        """
        Schedule progress check-ins based on user preferences
        """
        print(f"📅 Scheduler: Setting up {checkin_frequency} check-ins...")

        # Step 1: Create check-in schedule
        schedule = await self._create_checkin_schedule(checkin_frequency, context)

        # Step 2: Set up reminders
        reminders = self._create_reminders(schedule)

        # Step 3: Update context
        context.add_conversation("system", f"Scheduled {checkin_frequency} progress check-ins")

        print(f"✅ Scheduler: Successfully scheduled {len(schedule['sessions'])} check-in sessions")

        return {
            "success": True,
            "schedule": schedule,
            "reminders": reminders,
            "message": f"I've scheduled {checkin_frequency} progress check-ins for you!"
        }

    async def _create_checkin_schedule(self, frequency: str, context: UserSessionContext) -> Dict[str, Any]:
        """
        Create a schedule for check-ins
        """
        await asyncio.sleep(0.1)
        now = datetime.now()
        sessions = []

        if frequency == "weekly":
            for week in range(1, 9):
                checkin_date = now + timedelta(weeks=week)
                session = {
                    "week": week,
                    "date": checkin_date.strftime("%Y-%m-%d"),
                    "day_of_week": checkin_date.strftime("%A"),
                    "type": "Progress Check-in",
                    "focus_areas": self._get_weekly_focus_areas(week, context),
                    "questions": self._get_checkin_questions(week, context),
                    "time_slot": "Morning (9-11 AM)",
                    "duration": "15-20 minutes"
                }
                sessions.append(session)

        elif frequency == "bi-weekly":
            for session_num in range(1, 9):
                checkin_date = now + timedelta(weeks=session_num * 2)
                session = {
                    "session": session_num,
                    "date": checkin_date.strftime("%Y-%m-%d"),
                    "day_of_week": checkin_date.strftime("%A"),
                    "type": "Bi-weekly Review",
                    "focus_areas": self._get_biweekly_focus_areas(session_num, context),
                    "questions": self._get_checkin_questions(session_num * 2, context),
                    "time_slot": "Morning (9-11 AM)",
                    "duration": "20-30 minutes"
                }
                sessions.append(session)

        return {
            "frequency": frequency,
            "total_sessions": len(sessions),
            "start_date": now.strftime("%Y-%m-%d"),
            "sessions": sessions,
            "timezone": "Local Time"
        }

    def _get_weekly_focus_areas(self, week: int, context: UserSessionContext) -> List[str]:
        """Get focus areas for each week"""
        goal_type = context.goal.get("goal_type", "general_fitness") if context.goal else "general_fitness"

        focus_mapping = {
            1: ["Initial progress assessment", "Habit formation", "Routine establishment"],
            2: ["Exercise consistency", "Meal plan adherence", "Energy levels"],
            3: ["Physical measurements", "Strength improvements", "Dietary adjustments"],
            4: ["Mid-point evaluation", "Goal reassessment", "Plan modifications"],
            5: ["Motivation check", "Obstacle identification", "Support systems"],
            6: ["Progress acceleration", "Advanced techniques", "Challenge level"],
            7: ["Final push strategies", "Habit reinforcement", "Sustainability planning"],
            8: ["Goal achievement review", "Next phase planning", "Celebration and reflection"]
        }

        base_focus = focus_mapping.get(week, ["General progress", "Consistency", "Well-being"])

        if goal_type == "weight_loss":
            base_focus += ["Weight tracking", "Body composition"]
        elif goal_type == "muscle_gain":
            base_focus += ["Strength gains", "Muscle measurements"]

        return base_focus

    def _get_biweekly_focus_areas(self, session_num: int, context: UserSessionContext) -> List[str]:
        """Bi-weekly specific focus areas (simplified)"""
        return [f"Session {session_num} reflection", "Habits review", "Adjustments if needed"]

    def _get_checkin_questions(self, week: int, context: UserSessionContext) -> List[str]:
        """Questions to ask user during check-in"""
        questions = [
            "How are you feeling physically and mentally?",
            "Were you able to stick to your workout and meal plan?",
            "Any challenges or obstacles you faced this week?",
            "Is there anything you’d like to change or improve?"
        ]
        if context.goal:
            goal_type = context.goal.get("goal_type", "")
            if goal_type == "weight_loss":
                questions.append("Did you see any weight change this week?")
            elif goal_type == "muscle_gain":
                questions.append("Do you feel stronger or see muscle gain?")

        return questions

    def _create_reminders(self, schedule: Dict[str, Any]) -> List[str]:
        """Create reminder messages"""
        reminders = []
        for session in schedule["sessions"]:
            reminders.append(f"Reminder: {session['type']} on {session['date']} at {session['time_slot']}")
        return reminders
