from telegram.ext import Updater, MessageHandler, Filters

# Replace 'YOUR_BOT_TOKEN' with your actual bot token obtained from BotFather
BOT_TOKEN = 'YOUR_BOT_TOKEN'

def start(update, context):
    context.bot.send_message(chat_id=update.message.chat_id, text="Hi! I'm your bot. Type 'hello'")

def response(update, context):
    # Check if user's response includes 'hello':
    if 'hello' in update.message.text.lower():
        context.bot.send_message(chat_id=update.message.chat_id, text="Hi!")

# Define function main() that sets up the Telegram bot and determines how bot should respond to different types of messages:
def main():
    # Create Updater object which initializes the bot wuth provided BOT_TOKEN
    # use_context=True parameter means that there will be a new context-based approach:
    updater = Updater(token=BOT_TOKEN, use_context=True)

    # Create a dispatcher that is responsible for handling updates:
    dispatcher = updater.dispatcher

    # Add a command handler for the text messages and not commands:
    dispatcher.add_handler(MessageHandler(Filters.text & ~Filters.command, response))

    # Start the method start_polling() that actively listens to messages and updates:
    updater.start_polling()
    # Keep the program running until the user interupts:
    updater.idle()

# Ensure that function main() is executed only when the scrpt is run directly, not when imported as a module:    
if __name__ == '__main__':
    main()