from dotenv import load_dotenv
from google.adk.runners import Runner
from google.adk.sessions import InMemorySessionService
from google.genai import types
from qa_agent import qa_agent

import uuid

load_dotenv()

# InMemorySessionService - once the session closes all the data will be vanished.
session_memory = InMemorySessionService()

initial_state = {
    "user_name": "Ajith",
    "user_preference": """
        I like to play football, ps5 and running.
        My favorite food is Biriyani.
        My Favorite TV show is GoT.
        Loves it when people like and subscribe to his YouTube Channel.""",
}

# create new session
APP_NAME = "Ajith Bot"
USER_ID = "ajithera"
SESSION_ID = str(uuid.uuid4())

stateful_session = session_memory.create_session(
    app_name = APP_NAME,
    user_id = USER_ID,
    session_id = SESSION_ID,
    state = initial_state # state is nothing but a dictionary with key and values.
)
print("New session created: ", SESSION_ID)

runner = Runner(
    agent = qa_agent,
    app_name = APP_NAME,
    session_service = session_memory
)

print("step 1 done")

new_message = types.Content(
    role="user", parts=[types.Part(text="What is Ajith's favorite TV show?")]
)

print("step 2 done")

for event in runner.run(
    user_id=USER_ID,
    session_id=SESSION_ID,
    new_message=new_message,
):
    if event.is_final_response():
        if event.content and event.content.parts:
            print(f"Final Response: {event.content.parts[0].text}")

print("==== Session Event Exploration ====")
session = session_memory.get_session(
    app_name=APP_NAME, user_id=USER_ID, session_id=SESSION_ID
)

# Log final Session state
print("=== Final Session State ===")
for key, value in session.state.items():
    print(f"{key}: {value}")