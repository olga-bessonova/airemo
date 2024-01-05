#First, you need to make sure that you have a telegram account. Telegram can be downloaded from the Google Play Store, Apple Store or telegram site.

#Next, you need to obtain a bot token. Open telegram, and in the search bar search for "BotFather". Type /newbot and follow instructions.

#Install the telegram bot by typing the following command in your terminal:

#pip install python-telegram-bot

#Next, create python script, for example, 'telegram_bot_hi.py':

# Import libraries:
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from telegram import Update
from telegram.ext.callbackcontext import CallbackContext

# Replace 'YOUR_BOT_TOKEN' with your actual bot token obtained from BotFather
updater = Updater("YOUR_BOT_TOKEN", use_context=True) 

# Welcome message:
def start(update: Update, context: CallbackContext): 
    update.message.reply_text("Hi") 
def handle_message(update: Update, context: CallbackContext):
    text = update.message.text.lower()
    if text == "hello":
        update.message.reply_text("Hi")

updater.dispatcher.add_handler(MessageHandler(Filters.text & (~Filters.command), handle_message))

updater.dispatcher.add_handler(CommandHandler('start', start))

# Run the bot:
updater.start_polling() 


#To execute python script, type in the terminal:

#python 'telegram_bot_hi.py'

