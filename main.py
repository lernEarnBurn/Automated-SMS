from googleapiclient.discovery import build
from google.oauth2 import service_account
from dotenv import load_dotenv
import os

#need to make service account then need to be shared to the sheet
SCOPES = ['https://www.googleapis.com/auth/spreadsheets.readonly']
SERVICE_ACCOUNT_FILE = './sheetsApiKey.json'



credentials = None
credentials = service_account.Credentials.from_service_account_file(
        SERVICE_ACCOUNT_FILE, scopes=SCOPES)

SPREADSHEET_ID = '1UOLEry4RzgeSHqH69q6wN9SSlHclnp5oDkFNmZivKQg'

service = build('sheets', 'v4', credentials=credentials)


sheet = service.spreadsheets()
result = sheet.values().get(spreadsheetId=SPREADSHEET_ID,
                            range="sheet1!A1:D6").execute()

values = result.get('values', [])



for value in values:
    print(f'hey {value[0]} this is Moshe Lerner\n calling to let u know u got approved for ${value[3]}\n\n')

