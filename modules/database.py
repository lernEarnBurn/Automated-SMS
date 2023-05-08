from googleapiclient.discovery import build
from google.oauth2 import service_account






def databaseSheet():
        SCOPES = ['https://www.googleapis.com/auth/spreadsheets']
        SERVICE_ACCOUNT_FILE = './judaCreds.json'

        credentials = None
        credentials = service_account.Credentials.from_service_account_file(
                SERVICE_ACCOUNT_FILE, scopes=SCOPES)

        service = build('sheets', 'v4', credentials=credentials)
        sheet = service.spreadsheets()
        return sheet


def readDatabase():
        SPREADSHEET_ID = 'sadknskjdbakjbdksbadbasdbashd'
        result = databaseSheet().values().get(spreadsheetId=SPREADSHEET_ID,
                       range="sheet1!A1:E1").execute()

        values = result.get('values', [])
        return values[0]
        


def writeToDatabase(updatedMessage, updatedFirst, updatedLast):
        SPREADSHEET_ID = '1Kfy0zCpGXGasdasdadasda_cvTKgm74DdP7JrC2YaZKYsf2AWiKM4BU'
        updatedData = [[updatedMessage, updatedFirst, updatedLast]]

        databaseSheet().values().update(spreadsheetId=SPREADSHEET_ID, range="sheet1!A1:C1", valueInputOption="USER_ENTERED", body={"values": updatedData}).execute()


def readPrevResponses():
        SPREADSHEET_ID = '1KfG_cvTKgm74DdadsadasdadsP7JrC2YaZKYsf2AWiKM4BU'
        result = databaseSheet().values().get(spreadsheetId=SPREADSHEET_ID,
                       range="sheet1!E1").execute()

        values = result.get('values', [])
        try:
                return values[0]
        except:
                return [""]

def writeCurrentResponses(responseNumbers):
        SPREADSHEET_ID = '1Kfy0zCpGXG_csdabkdbskjdbakbdaskdYaZKYasdadadU'

        updatedData = [[" ".join(responseNumbers)]]

        databaseSheet().values().update(spreadsheetId=SPREADSHEET_ID, range="sheet1!E1", valueInputOption="RAW", body={"values": updatedData}).execute()


