from agents import function_tool, RunContextWrapper
from context import UserSessionContext

@function_tool
def track_progress(wrapper: RunContextWrapper[UserSessionContext], note: str) -> str:
    wrapper.context.progress_logs.append({"update": note})
    return f"Progress noted: {note}"