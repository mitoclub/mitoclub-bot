import telebot
import time
from googleapiclient.discovery import build
from httplib2 import Http
from oauth2client import file, client, tools
import response

# TODO
# new command for certain dates?
# Remind every week
# Delete old
# Insert new

SPREADSHEET_ID = '18c-03qAYD0RELLXv1b7G-dJkPgFQOCI2jP19CCh0a2U'
RANGE_NAME = '!A1:E'

store = file.Storage('token.json')
creds = store.get()
store = file.Storage('token.json')
service = build('sheets', 'v4', http=creds.authorize(Http()))
result = service.spreadsheets().values().get(spreadsheetId=SPREADSHEET_ID, range=RANGE_NAME).execute()
numRows = result.get('values') if result.get('values') is not None else "Wow, such empty!"
everything = "\n".join(["\t".join(i) for i in numRows])

access_token = '700467919:AAF5CYn06UHUGMoTTRsl0YSiriq-9l3GD0c'
bot = telebot.TeleBot(access_token)


while 1:
    time.sleep(5)
    try:
        @bot.message_handler(commands=['start'])
        def send_welcome(message):
            bot.send_message(message.chat.id, response.welcome)

        @bot.message_handler(commands=['everything'])
        def send_everything(message):
            bot.send_message(message.chat.id, everything)

        if __name__ == '__main__':
            bot.polling(none_stop=False, interval=0, timeout=20)
    except:
        time.sleep(5)
        continue