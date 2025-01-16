from crewai.tools import tool
import json
import requests

@tool
def slack_notifier(notification_endpoint: str,payload: dict) -> dict:
    """
    Fetch and process content from a web URL.
    
    Args:
        url (str): The web URL to fetch content from.
        
    Returns:
        str: The title and metadata of the webpage.
    """
    try:
        response = requests.post(
            notification_endpoint,
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
        return e
    return "Failed to send message."        