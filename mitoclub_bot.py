import telebot

access_token = '700467919:AAF5CYn06UHUGMoTTRsl0YSiriq-9l3GD0c'
bot = telebot.TeleBot(access_token)

SPREADSHEET_ID = '18c-03qAYD0RELLXv1b7G-dJkPgFQOCI2jP19CCh0a2U'
RANGE_NAME = 'Class Data!A1:E'

def get_content():
	store = file.Storage('token.json')
	creds = store.get()
    if not creds or creds.invalid:
        flow = client.flow_from_clientsecrets('credentials.json', SCOPES)
        creds = tools.run_flow(flow, store)
	service = build('sheets', 'v4', http=creds.authorize(Http()))

	result = service.spreadsheets().values().get(
    spreadsheetId=SPREADSHEET_ID, range="A1").execute()

	numRows = result.get('values') if result.get('values') is not None else "Wow, such empty!"
	text = "\n".join(["".join(i) for i in numRows])
	return text

everything = get_content()

@bot.message_handler(content_types=['text'])
def send_everything(message):
	updates = bot.get_updates()
	if updates.text == "everything":
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