import sys
import json
from slack_sdk import WebClient

json_path = sys.argv[1]

with open(json_path) as file:
    json_data = json.load(file)

bot_token = json_data["bot_token"]
client = WebClient(token=bot_token)

for channel in json_data["channels"]:
    channel_name = channel["channel"]
    message = channel["text"]
    result = client.chat_postMessage(channel=channel_name, text=message)
    print(f"Sending message \'{message}\' to channel {channel_name}\n")
