import telebot
import time
from googleapiclient.discovery import build
from httplib2 import Http
from oauth2client import file, client, tools

#SPREADSHEET_ID = '18c-03qAYD0RELLXv1b7G-dJkPgFQOCI2jP19CCh0a2U'
#RANGE_NAME = '!A1:E'

# Delete old
# Insert new
# Remind every week

#creds = google.oauth2.credentials.Credentials(access_token,refresh_token = refresh_token, token_uri = 'https://accounts.google.com/o/oauth2/token', client_id = "453055321365-hlivcj5qd7tb95krkv2tvep3iong4piq.apps.googleusercontent.com", client_secret = "3FjTSFTNFcbltahUvx2l4Hdn")

#store = file.Storage('token.json')
#service = build('sheets', 'v4', http=creds.authorize(Http()))
#result = service.spreadsheets().values().get(spreadsheetId=SPREADSHEET_ID, range=RANGE_NAME).execute()
#numRows = result.get('values') if result.get('values') is not None else "Wow, such empty!"
#everything = "\n".join(["".join(i) for i in numRows])
everything = "Wow, such empty!"

access_token = '700467919:AAF5CYn06UHUGMoTTRsl0YSiriq-9l3GD0c'
bot = telebot.TeleBot(access_token)


while 1:
    time.sleep(5)
    try:
        @bot.message_handler(commands=['start'])
        def send_welcome(message):
            text = "Hello, I am the Mitoclub TeleBot! I am responsible for keeping a list of upcoming meetings as well as keeping you posted about the deadlines. Here's a list of commands I can handle:\n\n/start display the welcome message again\n/everything print all of the upcoming meetings"
            bot.send_message(message.chat.id, text)

        @bot.message_handler(commands=['everything'])
        def echo(message):
            bot.send_message(message.chat.id, everything)

        if __name__ == '__main__':
            bot.polling(none_stop=False, interval=0, timeout=20)
    except:
        time.sleep(5)
        continue