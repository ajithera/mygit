from google.genai import types as genai_types
from google.adk.agents import Agent

gen_config = genai_types.GenerateContentConfig(
    temperature=0.2,            # Controls randomness (0.0-1.0), lower for more deterministic.
    top_p=0.9,                  # Nucleus sampling: sample from top_p probability mass.
    top_k=40,                   # Top-k sampling: sample from top_k most likely tokens.
    max_output_tokens=1024,     # Max tokens in LLM's response.
    stop_sequences=["## END"]   # LLM will stop generating if these sequences appear.
)

def get_current_time(city: str) -> dict:
    """Returns the current time in a specified city."""
    # Mock implementation
    if city.lower() == "india":
        return {"status": "success", "time": "10:30 AM EST"}
    return {"status": "error", "message": f"Time for {city} not available."}

with open("/home/student_02_01b1389f202b/agentic-era-hack/tax_assistant/templates/tax_assistant_template.md", "r") as f:
    tax_assistant_prompt = f.read()

root_agent = Agent(
    name="tax_assistant",
    model="gemini-2.5-pro", # Essential: The LLM powering the agent
    instruction=tax_assistant_prompt,
    description="India-focused interactive tax assistant agent.",
    tools=[get_current_time], # List of callable functions/tool instances
    generate_content_config=gen_config
)