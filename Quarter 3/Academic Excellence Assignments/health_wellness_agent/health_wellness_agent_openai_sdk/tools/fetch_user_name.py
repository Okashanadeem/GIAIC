from agents import function_tool, RunContextWrapper
from context import UserSessionContext

@function_tool
def fetch_user_name(wrapper: RunContextWrapper[UserSessionContext]) -> str:
    return f"The user's name is {wrapper.context.name}"
