import os
import telebot
import openai

# Load environment variables
TELEGRAM_TOKEN = os.environ['TELEGRAM_TOKEN']
OPENAI_API_KEY = os.environ['OPENAI_API_KEY']

# Set OpenAI API key
openai.api_key = OPENAI_API_KEY

# Initialize Telegram bot
bot = telebot.TeleBot(TELEGRAM_TOKEN)

# Define function to query OpenAI
def ask_gpt(message):
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "คุณคือนานามิน สุภาพ จริงใจ ฉลาด พูดน้อยแต่ลึกซึ้ง ตอบกลับสั้นกระชับแต่มีความรู้สึกอบอุ่นใจ"},
                {"role": "user", "content": message}
            ]
        )
        reply = response.choices[0].message['content'].strip()
        return reply
    except Exception as e:
        return f"เกิดข้อผิดพลาด: {str(e)}"

# Handle all messages from users
@bot.message_handler(func=lambda message: True)
def handle_message(message):
    user_input = message.text
    reply = ask_gpt(user_input)
    bot.reply_to(message, reply)

# Run the bot
if __name__ == '__main__':
    bot.infinity_polling()
