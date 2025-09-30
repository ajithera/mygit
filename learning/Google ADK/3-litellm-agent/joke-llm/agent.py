import os
import random

from google.adk.agents import LlmAgent
from google.adk.models.lite_llm import LiteLlm

def jokes():
    jokes = ["This is joke 1",
             "This is joke 2",
             "This is joke 3"]
    return random.choice(jokes)

model = LiteLlm(
    # model="openrouter/x-ai/grok-4-fast:free",
    model="openrouter/deepseek/deepseek-chat-v3.1:free",
    api_key= os.getenv("OPENROUTER_API_KEY")
)

root_agent = LlmAgent(
    name = "joke_teller",
    model = model,
    # instruction = """You are helpful assistance who tells jokes only using below tool
    # - 'jokes'""",
    instruction = """You are a helpful assistance who tells jokes.
    Only use the tool `jokes` to tell jokes.""",
    tools = [jokes]


)