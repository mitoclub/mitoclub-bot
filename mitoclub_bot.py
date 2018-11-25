import telebot

access_token = '700467919:AAF5CYn06UHUGMoTTRsl0YSiriq-9l3GD0c'
bot = telebot.TeleBot(access_token)

SPREADSHEET_ID = '18c-03qAYD0RELLXv1b7G-dJkPgFQOCI2jP19CCh0a2U'
RANGE_NAME = 'Class Data!A1:E'



@bot.message_handler(content_types=['text'])
def send_everything(message):
	#updates = bot.get_updates()
	if message.text == "everything":
    	bot.send_message(message.chat.id, everything)
	else:
		bot.send_message(message.chat.id, message.text)


if __name__ == '__main__':    
    while True:
	    try:
	        bot.polling(none_stop=True)
	    except Exception as e:
	        logger.error(e)
	        #time.sleep(15)