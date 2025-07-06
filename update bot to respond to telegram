from flask import Flask, request
import requests
import os

app = Flask(__name__)
TOKEN = os.environ.get("TELEGRAM_TOKEN")  # ต้องตั้ง env var ใน Render ด้วย

@app.route("/", methods=["GET"])
def home():
    return "Hello, Nanamin Bot is alive."

@app.route("/webhook", methods=["POST"])
def webhook():
    data = request.get_json()
    if data and "message" in data:
        chat_id = data["message"]["chat"]["id"]
        user_text = data["message"].get("text", "")
        
        # ตอบข้อความ (จะตอบอะไรก็แก้ได้)
        reply_text = f"นานามินได้รับข้อความ: {user_text}"
        send_message(chat_id, reply_text)
    return "Webhook received", 200

def send_message(chat_id, text):
    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
    payload = {"chat_id": chat_id, "text": text}
    requests.post(url, json=payload)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))
