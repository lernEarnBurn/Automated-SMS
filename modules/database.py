from googleapiclient.discovery import build
from google.oauth2 import service_account

from dotenv import load_dotenv
import os

load_dotenv()

def databaseSheet():
        SCOPES = ['https://www.googleapis.com/auth/spreadsheets']
        SERVICE_ACCOUNT_FILE = 'joshCreds.json'

        credentials = None
        credentials = service_account.Credentials.from_service_account_file(
                SERVICE_ACCOUNT_FILE, scopes=SCOPES)

        service = build('sheets', 'v4', credentials=credentials)
        sheet = service.spreadsheets()
        return sheet


def readDatabase():
        SPREADSHEET_ID = 'spreadsheet_id'
        result = databaseSheet().values().get(spreadsheetId=SPREADSHEET_ID,
                       range="sheet1!A1:E1").execute()

        values = result.get('values', [])
        return values[0]
        


def writeToDatabase(updatedMessage, updatedFirst, updatedLast):
        SPREADSHEET_ID = 'spreadsheet_id'
        updatedData = [[updatedMessage, updatedFirst, updatedLast]]

        databaseSheet().values().update(spreadsheetId=SPREADSHEET_ID, range="sheet1!A1:C1", valueInputOption="USER_ENTERED", body={"values": updatedData}).execute()


def readPrevResponses():
        SPREADSHEET_ID = 'spreadsheet_id'
        result = databaseSheet().values().get(spreadsheetId=SPREADSHEET_ID,
                       range="sheet1!E1").execute()

        values = result.get('values', [])
        try:
                return values[0]
        except:
                return [""]

def writeCurrentResponses(responseNumbers):
        SPREADSHEET_ID = 'spreadsheet_id'

        updatedData = [[" ".join(responseNumbers)]]

        databaseSheet().values().update(spreadsheetId=SPREADSHEET_ID, range="sheet1!E1", valueInputOption="RAW", body={"values": updatedData}).execute()


