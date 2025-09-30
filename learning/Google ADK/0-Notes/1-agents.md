23/09/2025
# Google ADK

## Agents:
`Agent` or `Llmagent`.

It is a core concept of LLM. 

It will call the actual llm models in the framework.

Example:
```
from google.adk.agents import llmAgent

capital_agent = LlmAgent(
    model="gemini-2.0-flash",
    name="capital_agent",
    description="Answers user questions about the capital city of a given country.",
    instruction="""You are an agent that provides the capital city of a country.
When a user asks for the capital of a country:
1. Identify the country name from the user's query.
2. Use the `get_capital_city` tool to find the capital.
3. Respond clearly to the user, stating the capital city.
Example Query: "What's the capital of {country}?"
Example Response: "The capital of France is Paris."
"""
)
```
## Tools:
