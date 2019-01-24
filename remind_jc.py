import telebot
import response
from config import bot_access_token

"""
	JC_reminder task. Runs at 13:30 UTC every Thursday.
"""

bot = telebot.TeleBot(bot_access_token)
bot.send_message(211516424, response.reminder_jc)