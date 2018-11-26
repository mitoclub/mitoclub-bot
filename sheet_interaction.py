from googleapiclient.discovery import build
from httplib2 import Http
from oauth2client import file, client, tools
from config import SPREADSHEET_ID

def get_everything():
	RANGE_NAME = '!A1:E'
	store = file.Storage('token.json')
	creds = store.get()
	store = file.Storage('token.json')
	service = build('sheets', 'v4', http=creds.authorize(Http()))
	result = service.spreadsheets().values().get(spreadsheetId=SPREADSHEET_ID, range=RANGE_NAME).execute()
	numRows = result.get('values') if result.get('values') is not None else "Wow, such empty!"
	numRows = numRows[1:]
	everything = "\n".join(["\n".join(i) for i in numRows])
	everything += "\n\n"
	return everything