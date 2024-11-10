from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup, WebAppInfo
from telegram.ext import Updater, CommandHandler, CallbackContext
from dotenv import load_dotenv
import os

# Загрузка переменных окружения из файла .env
load_dotenv()

TELEGRAM_BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
WEB_APP_URL = os.getenv("WEB_APP_URL")

def start(update: Update, context: CallbackContext):
    keyboard = [
        [InlineKeyboardButton("Open Web App", web_app=WebAppInfo(url=WEB_APP_URL))]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    update.message.reply_text("Нажмите 'Open Web App' для запуска игры", reply_markup=reply_markup)

def main():
    updater = Updater(TELEGRAM_BOT_TOKEN)
    dp = updater.dispatcher
    dp.add_handler(CommandHandler("start", start))

    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
