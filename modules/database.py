from googleapiclient.discovery import build
from google.oauth2 import service_account

from dotenv import load_dotenv
import os

load_dotenv()

def databaseSheet():
        SCOPES = ['https://www.googleapis.com/auth/spreadsheets']
        SERVICE_ACCOUNT_FILE = 'credentials.json'

        credentials = None
        credentials = service_account.Credentials.from_service_account_file(
                SERVICE_ACCOUNT_FILE, scopes=SCOPES)

        service = build('sheets', 'v4', credentials=credentials)
        sheet = service.spreadsheets()
        return sheet


def readDatabase():
        SPREADSHEET_ID = 'SPREADSHEET_ID'
        result = databaseSheet().values().get(spreadsheetId=SPREADSHEET_ID,
                       range="sheet1!A1:C1").execute()

        values = result.get('values', [])
        return values[0]
        


def writeToDatabase(updatedMessage, updatedFirst, updatedLast):
        SPREADSHEET_ID = 'SPREADSHEET_ID'
        updatedData = [[updatedMessage, updatedFirst, updatedLast]]

        databaseSheet().values().update(spreadsheetId=SPREADSHEET_ID, range="sheet1!A1:C1", valueInputOption="USER_ENTERED", body={"values": updatedData}).execute()