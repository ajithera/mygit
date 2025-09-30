from google.adk.agents import LlmAgent
from google.adk.tools import google_search

root_agent = LlmAgent(
    name= "tool_agent",
    description = "It is a tool agent",
    model = "gemini-2.5-flash",
    instruction = """You are an helpful agent that can use following tools
    - google_search""",
    tools = [google_search]
)