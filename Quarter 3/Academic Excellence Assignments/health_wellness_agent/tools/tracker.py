"""
Progress Tracker Tool
Logs and summarizes user wellness progress over time
"""

from typing import Dict, Any, List
from datetime import datetime
from context import UserSessionContext

class ProgressTrackerTool:
    """
    Tracks and logs weekly progress including workouts, meals, mindset, and results
    """

    def __init__(self):
        self.name = "progress_tracker"
        self.description = "Tracks and summarizes user wellness progress"

    def track_progress(self, context: UserSessionContext, update: Dict[str, str]) -> Dict[str, Any]:
        """
        Record user progress entry
        """
        print("📊 Progress Tracker: Logging new progress...")

        # Add timestamp to the update
        timestamped_update = {
            "date": datetime.now().strftime("%Y-%m-%d"),
            "data": update
        }

        # Save to context
        context.progress_logs.append(timestamped_update)
        context.add_conversation("system", "Logged weekly progress update.")

        print(f"✅ Tracker: Progress updated for {timestamped_update['date']}")

        # Return success message with last 3 summaries
        summary = self._summarize_progress(context)

        return {
            "success": True,
            "message": "Your progress has been successfully recorded!",
            "summary": summary,
            "total_logs": len(context.progress_logs)
        }

    def _summarize_progress(self, context: UserSessionContext) -> str:
        """
        Summarize the latest progress entries
        """
        if not context.progress_logs:
            return "No progress has been logged yet."

        summary_lines = [f"📆 Progress Summary ({len(context.progress_logs)} entries)"]

        # Show last 3 logs only
        for entry in context.progress_logs[-3:]:
            date = entry["date"]
            data = entry["data"]
            summary = f"🗓️ {date}: " + ", ".join([f"{k}: {v}" for k, v in data.items()])
            summary_lines.append(summary)

        return "\n".join(summary_lines)

# Simple test block
if __name__ == "__main__":
    from context import UserSessionContext

    tracker = ProgressTrackerTool()
    context = UserSessionContext(name="TestUser", uid=101)

    updates = [
        {"workout": "3 sessions", "diet": "mostly followed", "mood": "energized"},
        {"workout": "2 sessions", "diet": "cheated twice", "mood": "low"},
        {"workout": "4 sessions", "diet": "perfect", "mood": "motivated"},
    ]

    for update in updates:
        result = tracker.track_progress(context, update)
        print(result["message"])
        print(result["summary"])
        print(f"Total logs: {result['total_logs']}\n")
        print("-" * 40)
        print("End of test\n")

