from google.adk.agents import LlmAgent
from pydantic import BaseModel,Field

# define output schema
class EmailContent(BaseModel):
    subject: str = Field(
        description="The subject line of the email. Should be concise and descriptive"
    )
    body: str = Field(
        description="The main content of the email. Should be well formatted with proper greeting, paragraphs, and signature"
    )

root_agent = LlmAgent(
    name = "email_agent",
    model = "gemini-2.5-flash",
    description= "Mail generation Agent",
    instruction= """ 
    You are email generation assistant.
    Your task is to generate email based on user's input.

    GUIDELINES:
    - Create an appropriate subject line (Concise and relevent)
    - Write a well-structured email body with:
        * Professional Greeting
        * Clear and concise main content
        * Appropriate closing
        * Your name as signature
    - Suggest relevent attachments if appicable (empty list if none needed)
    - Email tone should match the purpose (formal for business, friendly for colleagues)
    - Keep emails concise but complete

    IMPORTANT: Your response MUST be valid JSON matching this structure:
    {
        "subject": "Subject Line Here",
        "body": "Email body here with proper paragraphs and formatting",
    }

    DO NOT include any explanations or additional text outside the JSON  response.
    """,
    output_schema = EmailContent,
    output_key= "email"
    )
