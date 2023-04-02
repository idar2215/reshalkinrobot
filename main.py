import os
import logging
import telegram
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from dotenv import load_dotenv
from gpt import GPT
# Load environment variables
load_dotenv()
# Set up logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
# Set up Telegram API
bot = telegram.Bot(token=os.getenv('6237673020:AAFQb3mtOaHg0bv0iePthqo1UgfB3A5ZJgU'))
# Set up GPT model
gpt = GPT()
# Define start command handler
def start(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="Привет! Я бот для работы с токенами. Нажми на кнопку, чтобы узнать баланс токенов.")
# Define balance command handler
def balance(update, context):
    # Get balance from database or API
    balance = 100
    context.bot.send_message(chat_id=update.effective_chat.id, text=f"Баланс токенов: {balance}")
# Define secret code handler
def secret_code(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="Введите секретный код на бесконечные токены:")
# Define message handler
def message(update, context):
    # Check if message is a photo
    if update.message.photo:
        # Download photo
        file = bot.getFile(update.message.photo[-1].file_id)
        filename = file.download()
        # Extract text from photo using GPT
        text = gpt.extract_text_from_image(filename)
        # Answer question using GPT
        answer = gpt.answer_question(text)
        # Send answer to user
        context.bot.send_message(chat_id=update.effective_chat.id, text=answer)
# Define admin panel handler
def admin_panel(update, context):
    # Check if user is an admin
    if update.effective_user.id == int(os.getenv('6192875899')):
        # Show admin panel
        context.bot.send_message(chat_id=update.effective_chat.id, text="Админ-панель")
# Define main function
def main():
    # Create updater and dispatcher
    updater = Updater(token=os.getenv('6237673020:AAFQb3mtOaHg0bv0iePthqo1UgfB3A5ZJgU'), use_context=True)
    dispatcher = updater.dispatcher
    # Add handlers
    dispatcher.add_handler(CommandHandler('start', start))
    dispatcher.add_handler(CommandHandler('balance', balance))
    dispatcher.add_handler(CommandHandler('secret_code', secret_code))
    dispatcher.add_handler(MessageHandler(Filters.text, message))
    dispatcher.add_handler(CommandHandler('22157219', admin_panel))
    # Start polling
    updater.start_polling()
    # Run until Ctrl-C is pressed
    updater.idle()
if __name__ == '__main__':
    main()
