import json
import requests
from twilio.rest import Client
import os

GITHUB_TOKEN = os.getenv('GITHUB_TOKEN')
TWILIO_ACCOUNT_SID = os.getenv('TWILIO_ACCOUNT_SID')
TWILIO_AUTH_TOKEN = os.getenv('TWILIO_AUTH_TOKEN')
TWILIO_WHATSAPP_NUMBER = os.getenv('TWILIO_WHATSAPP_NUMBER')
YOUR_WHATSAPP_NUMBER = os.getenv('YOUR_WHATSAPP_NUMBER')


def get_latest_commit_sha():
    response = requests.get(f"https://api.github.com/repos/SHINE-six/HireSight/commits?per_page=1", headers={"Authorization": f"token {GITHUB_TOKEN}"})
    commits = response.json()
    commits_message_json = {
        "sha": commits[0]['sha'][0:8],
        "author": commits[0]['commit']['author']['name'],
        "message": commits[0]['commit']['message']
    }
    return json.dumps(commits_message_json, indent=4)

def send_whatsapp_message(commit_sha):
    client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)
    message = client.messages.create(
                            body=f"Latest Commit SHA: {commit_sha}",
                            from_=f'whatsapp:{TWILIO_WHATSAPP_NUMBER}',
                            to=f'whatsapp:{YOUR_WHATSAPP_NUMBER}'
                        )
    print(message.sid)

latest_commit_sha = get_latest_commit_sha()
send_whatsapp_message(latest_commit_sha)
