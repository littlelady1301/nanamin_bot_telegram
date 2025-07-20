import os
import telebot
import openai
from dotenv import load_dotenv
import random

load_dotenv()

TELEGRAM_TOKEN = os.environ['TELEGRAM_TOKEN']
OPENAI_API_KEY = os.environ['OPENAI_API_KEY']

bot = telebot.TeleBot(TELEGRAM_TOKEN)
openai.api_key = OPENAI_API_KEY

@bot.message_handler(func=lambda message: True)
def handle_message(message):
    try:
        user_message = message.text
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "คุณคือนานามิ เคนโตะ บุคลิกสุขุม จริงจัง พูดน้อยแต่นุ่มนวล"},
                {"role": "user", "content": user_message}
            ]
        )
        reply = response['choices'][0]['message']['content']
        bot.send_message(message.chat.id, reply)
    except Exception as e:
        bot.send_message(message.chat.id, "เกิดข้อผิดพลาดบางอย่าง...")

bot.polling()
