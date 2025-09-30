from dotenv import load_dotenv
from google.adk.runners import Runner
from google.adk.sessions import InMemorySessionService
from google.genai import types
from qa_agent import qa_agent

load_dotenv()

initial_state = {
    "user_name": "Ajith",
    "user_preference": """
        I like to play football, ps5 and running.
        My favorite food is Biriyani.
        My Favorite TV show is GoT.
        Loves it when people like and subscribe to his YouTube Channel.""",
}