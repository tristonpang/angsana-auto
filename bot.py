import telegram
from telegram.ext import Updater, MessageHandler, Filters
from telegram.ext import CommandHandler
import os
from webserver import welcome

telegram_bot_token = '5675610376:AAE8O3RbO2ViRpFyOya_HHT3Zb-TNrYr8Tc'

updater = Updater(token=telegram_bot_token, use_context=True)
dispatcher = updater.dispatcher


# set up the introductory statement for the bot when the /start command is invoked
def start(update, context):
    chat_id = update.effective_chat.id
    context.bot.send_message(chat_id=chat_id, text="Hello there. This bot serves to automate publishing posts and promotional material to all related Angsana Network channels and social media platforms.")


# obtain the information of the word provided and format before presenting.
def test(update, context):
    msg = welcome(update.message.text)

    update.message.reply_text(msg)

# run the start function when the user invokes the /start command 
dispatcher.add_handler(CommandHandler("start", start))

# invoke the get_word_info function when the user sends a message 
# that is not a command.
dispatcher.add_handler(MessageHandler(Filters.text, test))
updater.start_webhook(listen="0.0.0.0",
                      port=int(os.environ.get('PORT', 5000)),
                      url_path=telegram_bot_token,
                      webhook_url=  + telegram_bot_token
                      )