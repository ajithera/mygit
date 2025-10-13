from google.adk.agents import LlmAgent

qa_agent = LlmAgent(
    name = "qa_agent",
    model = "gemini-2.5-flash",
    description= "QA Agent",
    instruction= """ 
    You are a helpful assistant that answers questions about user's preferences.
    Here are some information about user:
    Name: {user_name}
    Preference: {user_preference}
    """
)
