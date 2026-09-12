import os
import json
import urllib.request

def send_seatalk_reminder():
    # Retrieve the secure webhook URL from GitHub Secrets
    webhook_url = os.environ.get("SEATALK_WEBHOOK_URL")
    if not webhook_url:
        print("Error: SEATALK_WEBHOOK_URL environment variable is missing.")
        return

    # Construct the JSON text message payload required by SeaTalk
    payload = {
        "tag": "text",
        "text": {
            "content": "⏰ Daily Reminder: Please update your task status boards and submit your daily logs! @all",
            "at_all": True  # Pings everyone in the group chat
        }
    }
    
    # Convert payload dictionary to encoded bytes
    data = json.dumps(payload).encode('utf-8')
    
    # Set headers and submit the POST request
    req = urllib.request.Request(
        webhook_url, 
        data=data, 
        headers={'Content-Type': 'application/json'}
    )
    
    try:
        with urllib.request.urlopen(req) as response:
            status = response.getcode()
            if status == 200:
                print("Reminder pushed successfully to SeaTalk!")
            else:
                print(f"Failed to send. Server responded with status: {status}")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    send_seatalk_reminder()
