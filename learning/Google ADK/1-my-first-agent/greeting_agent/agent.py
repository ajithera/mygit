from google.adk.agents import LlmAgent

root_agent = LlmAgent(
    name = "greeting_agent",
    model = "gemini-2.5-flash",
    description= "Greeting Agent",
    instruction= """ you are helpful assistant that greets the user.
    Ask for the users name and greet them by name."""
)