import telebot
import time
import response
from config import bot_access_token
from sheet_interaction import *

# TODO
# Remind every week about journal club and lab meeting an hour before 
# Delete old
# Insert new

everything = get_everything()
everything = "Here are all the upcoming meetings listed by deadline order:\n\n" + everything
bot = telebot.TeleBot(bot_access_token)

while 1:
    time.sleep(5)
    try:
        @bot.message_handler(commands=['start'])
        def send_welcome(message):
            bot.send_message(message.chat.id, response.welcome)
            bot.send_message(211516424, message)

        @bot.message_handler(commands=['help'])
        def send_welcome(message):
            bot.send_message(message.chat.id, response.help_message)
            bot.send_message(211516424, message)

        @bot.message_handler(commands=['everything'])
        def send_everything(message):
            bot.send_message(message.chat.id, everything)
            bot.send_message(211516424, message)
        # Reaction to text
        @bot.message_handler(content_types=['text'])
        def send_welcome(message):
            bot.send_message(message.chat.id, response.text)
            bot.send_message(211516424, message)

        if __name__ == '__main__':
            bot.polling(none_stop=False, interval=0, timeout=20)
    except:
        time.sleep(5)
        continue