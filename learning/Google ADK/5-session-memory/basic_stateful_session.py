import asyncio
import uuid
from dotenv import load_dotenv
from google.adk.runners import Runner
from google.adk.sessions import InMemorySessionService
from google.genai import types
from qa_agent import qa_agent


async def main():
    load_dotenv()

    # In-memory session store (async API)
    session_memory = InMemorySessionService()

    initial_state = {
        "user_name": "Ajith",
        "user_preference": """
            I like to play football, ps5 and running.
            My favorite food is Biriyani.
            My Favorite TV show is GoT.
            Loves it when people like and subscribe to his YouTube Channel.""",
    }

    APP_NAME = "Ajith Bot"
    USER_ID = "ajithera"
    SESSION_ID = str(uuid.uuid4())

    # Create the session (must be awaited)
    await session_memory.create_session(
        app_name=APP_NAME,
        user_id=USER_ID,
        session_id=SESSION_ID,
        state=initial_state,
    )
    print("New session created: ", SESSION_ID)

    runner = Runner(
        agent=qa_agent,
        app_name=APP_NAME,
        session_service=session_memory,
    )

    print("step 1 done")

    new_message = types.Content(
        role="user", parts=[types.Part(text="What is Ajith's favorite TV show?")]
    )

    print("step 2 done")

    try:
        # Use the async runner to keep everything in one event loop
        async for event in runner.run_async(
            user_id=USER_ID,
            session_id=SESSION_ID,
            new_message=new_message,
        ):
            print("step 3 done")
            if event.is_final_response():
                if event.content and event.content.parts:
                    print(f"Final Response: {event.content.parts[0].text}")
    finally:
        # Clean up network resources to avoid "Unclosed client session/connector"
        if hasattr(runner, "aclose"):
            await runner.aclose()
        elif hasattr(runner, "close"):
            runner.close()

        # If your qa_agent constructs any client (e.g., google.genai client),
        # ensure it provides a teardown method or expose the client so we can close it here.
        if hasattr(qa_agent, "teardown"):
            maybe = qa_agent.teardown()
            if asyncio.iscoroutine(maybe):
                await maybe

        client = getattr(qa_agent, "client", None)
        if client:
            if hasattr(client, "aclose"):
                await client.aclose()
            elif hasattr(client, "close"):
                client.close()

    print("==== Session Event Exploration ====")

    # Read back the final session state (must be awaited)
    session = await session_memory.get_session(
        app_name=APP_NAME, user_id=USER_ID, session_id=SESSION_ID
    )

    print("=== Final Session State ===")
    for key, value in session.state.items():
        print(f"{key}: {value}")


if __name__ == "__main__":
    asyncio.run(main())
