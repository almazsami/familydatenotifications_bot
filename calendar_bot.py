import requests
from datetime import datetime

import os
BOT_TOKEN = os.environ["BOT_TOKEN"]

CHAT_ID = -1003809412436
THREAD_ID = 5

BASE_URL = f"https://api.telegram.org/bot{BOT_TOKEN}"

def get_updates():
    return requests.get(f"{BASE_URL}/getUpdates").json()

def reply(message_id):
    requests.post(
        f"{BASE_URL}/sendMessage",
        json={
            "chat_id": CHAT_ID,
            "message_thread_id": THREAD_ID,
            "reply_to_message_id": message_id,
            "text": "@almazsami @dinara.qwq"
        }
    )

today = datetime.utcnow().strftime("%d.%m.%Y")

updates = get_updates()

for u in updates.get("result", []):
    msg = u.get("message")
    if not msg:
        continue

    if msg.get("message_thread_id") != THREAD_ID:
        continue

    text = msg.get("text", "")
    if text.startswith(today):
        reply(msg["message_id"])
