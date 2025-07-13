from agents import function_tool, RunContextWrapper
from context import UserSessionContext

@function_tool
def schedule_checkin(wrapper: RunContextWrapper[UserSessionContext], day: str) -> str:
    message = f"Check-in scheduled every {day}"
    wrapper.context.progress_logs.append({"scheduled": message})
    return message
