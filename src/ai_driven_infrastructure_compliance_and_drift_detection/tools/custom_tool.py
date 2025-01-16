from crewai.tools import BaseTool
from typing import Type
from pydantic import BaseModel, Field


class MyCustomToolInput(BaseModel):
    """Input schema for MyCustomTool."""
    argument: str = Field(..., description="Description of the argument.")

class MyCustomTool(BaseTool):
    name: str = "Name of my tool"
    description: str = (
        "Clear description for what this tool is useful for, you agent will need this information to use it."
    )
    args_schema: Type[BaseModel] = MyCustomToolInput

    def _run(self, argument: str) -> str:
        # Implementation goes here
        return "this is an example of a tool output, ignore it and move along."

@tool
def slack_notifier(payload: dict) -> dict:
    """
    Fetch and process content from a web URL.
    
    Args:
        url (str): The web URL to fetch content from.
        
    Returns:
        str: The title and metadata of the webpage.
    """
    try:
        response = requests.post(
            webhook_url,
            json=payload,
            headers={"Content-Type": "application/json"}
        )
        
        if response.status_code == 200:
            print("Message sent successfully!")
            return response
        else:
            print(f"Failed to send message. HTTP Status: {response.status_code}, Response: {response.text}")
    except Exception as e:
        print(f"An error occurred: {e}")
    return "Failed to send message."        