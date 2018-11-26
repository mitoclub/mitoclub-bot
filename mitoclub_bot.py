import telebot
import time
import response
from config import bot_access_token
from sheet_interaction import *


# TODO
# new command for certain dates?
# Remind every week
# Delete old
# Insert new
# next week month

everything = get_everything()
everything = "Here are all the upcoming meetings listed by deadline order:\n\n" + everything
bot = telebot.TeleBot(bot_access_token)

while 1:
    time.sleep(5)
    try:
        @bot.message_handler(commands=['start'])
        def send_welcome(message):
            bot.send_message(message.chat.id, response.welcome)

        @bot.message_handler(commands=['help'])
        def send_welcome(message):
            bot.send_message(message.chat.id, response.help_message)

        @bot.message_handler(commands=['everything'])
        def send_everything(message):
            bot.send_message(message.chat.id, everything)
        # Reaction to text
        @bot.message_handler(content_types=['text'])
        def send_welcome(message):
            bot.send_message(message.chat.id, response.text)

        if __name__ == '__main__':
            bot.polling(none_stop=False, interval=0, timeout=20)
    except:
        time.sleep(5)
        continue