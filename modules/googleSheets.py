from googleapiclient.discovery import build
from google.oauth2 import service_account

from dotenv import load_dotenv
import os

load_dotenv()

def fetchData(firstRow, lastRow):
    SCOPES = ['https://www.googleapis.com/auth/spreadsheets.readonly']
    SERVICE_ACCOUNT_FILE = './joshCreds.json'

    credentials = None
    credentials = service_account.Credentials.from_service_account_file(
            SERVICE_ACCOUNT_FILE, scopes=SCOPES)

    SPREADSHEET_ID = os.getenv('dummyLeadsSpreadsheetId')

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
        #round to nearest 10,000 then cut in half

def getBusinessName():
        return
        #if business name has a / only use whats on the right of /

def equityNumber():
        return
        #if first cells number has a space after it then whichever
        #out of the next one that is over 50 gets it unless theyure both 50




#database features, gonna move ti a new file
def databaseSheet():
        SCOPES = ['https://www.googleapis.com/auth/spreadsheets']
        SERVICE_ACCOUNT_FILE = './joshCreds.json'

        credentials = None
        credentials = service_account.Credentials.from_service_account_file(
                SERVICE_ACCOUNT_FILE, scopes=SCOPES)

        service = build('sheets', 'v4', credentials=credentials)
        sheet = service.spreadsheets()
        return sheet


def readDatabase():
        SPREADSHEET_ID = os.getenv('databaseSpreadsheetId')
        result = databaseSheet().values().get(spreadsheetId=SPREADSHEET_ID,
                       range="sheet1!A1:C1").execute()

        values = result.get('values', [])
        return values[0]
        


def writeToDatabase(updatedMessage, updatedFirst, updatedLast):
        SPREADSHEET_ID = os.getenv('databaseSpreadsheetId')
        updatedData = [[updatedMessage, updatedFirst, updatedLast]]

        request = databaseSheet().values().update(spreadsheetId=SPREADSHEET_ID, range="sheet1!A1:C1", valueInputOption="USER_ENTERED", body={"values": updatedData}).execute()