from googleapiclient.discovery import build
from google.oauth2 import service_account

from dotenv import load_dotenv
import os

load_dotenv()

def readSpreadsheet(firstRow, lastRow):
    SCOPES = ['https://www.googleapis.com/auth/spreadsheets.readonly']
    SERVICE_ACCOUNT_FILE = './sheetsApiKey.json'

    credentials = None
    credentials = service_account.Credentials.from_service_account_file(
            SERVICE_ACCOUNT_FILE, scopes=SCOPES)

    SPREADSHEET_ID = os.getenv('testSpreadsheetId')

    service = build('sheets', 'v4', credentials=credentials)


    sheet = service.spreadsheets()
    result = sheet.values().get(spreadsheetId=SPREADSHEET_ID,
                                range="sheet1!A" + firstRow + ":E" + lastRow).execute()

    values = result.get('values', [])

    return values


def firstNameFormat(name):
        return


def roundValue(num):
        return