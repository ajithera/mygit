from google.adk.agents import LlmAgent
from google.adk.tools import google_search
from datetime import datetime


def get_current_time() -> dict:
    """
    Returns the current time in a dictionary format with the key 'Current time:'.
    """

    # Get the current time as a formatted string
    current_time_str = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    # Return the time in a dictionary
    return {"Current time:": current_time_str}


root_agent = LlmAgent(
    name= "cur_time_agent",
    description = "It is a tool agent",
    model = "gemini-2.5-flash",
    instruction = """You are an helpful agent that can use following tools
    - get_current_time""",
    tools = [get_current_time]
)