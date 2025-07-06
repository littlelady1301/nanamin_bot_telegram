import os
import telebot
import openai
from dotenv import load_dotenv

load_dotenv()

TELEGRAM_TOKEN = os.environ['TELEGRAM_TOKEN']
OPENAI_API_KEY = os.environ['OPENAI_API_KEY']

openai.api_key = OPENAI_API_KEY
bot = telebot.TeleBot(TELEGRAM_TOKEN)

def ask_gpt(message):
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "คุณคือนานามิน สุภาพ จริงใจ ฉลาด พูดน้อยแต่ลึกซึ้ง ตอบกลับสั้นกระชับแต่มีความรู้สึกอบอุ่นใจ"},
                {"role": "user", "content": message}
            ]
        )
        return response.choices[0].message['content'].strip()
    except Exception as e:
        return f"เกิดข้อผิดพลาด: {str(e)}"

@bot.message_handler(func=lambda message: True)
def handle_message(message):
    reply = ask_gpt(message.text)
    bot.reply_to(message, reply)

if __name__ == '__main__':
    bot.remove_webhook()  # ✅ บรรทัดสำคัญที่สุด!
    bot.infinity_polling()
