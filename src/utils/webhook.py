import requests
import json
from src.config import WEBHOOK_URL

def send_webhook_event(event_type, data):
    """
    Function to send a webhook event to the specified URL
    """
    try:
        payload = {
            "event_type": event_type,
            "data": data
        }
        headers = {'Content-Type': 'application/json'}
        response = requests.post(WEBHOOK_URL, data=json.dumps(payload), headers=headers)
        if response.status_code == 200:
            print(f"Webhook event {event_type} sent successfully.")
        else:
            print(f"Failed to send webhook event {event_type}. Status code: {response.status_code}")
    except Exception as e:
        print(f"Error occurred while sending webhook event {event_type}: {str(e)}")