from googleapiclient.discovery import build
from google.oauth2 import service_account

from dotenv import load_dotenv
import os

load_dotenv()

def fetchData(firstRow, lastRow):
    SCOPES = ['https://www.googleapis.com/auth/spreadsheets.readonly']
    SERVICE_ACCOUNT_FILE = './judaCreds.json'

    credentials = None
    credentials = service_account.Credentials.from_service_account_file(
            SERVICE_ACCOUNT_FILE, scopes=SCOPES)

    SPREADSHEET_ID = '123'

    service = build('sheets', 'v4', credentials=credentials)


    sheet = service.spreadsheets()
    result = sheet.values().get(spreadsheetId=SPREADSHEET_ID,
                                range=f"'JUDA''S PIPELINE'!B{firstRow}:N{lastRow}").execute()

    values = result.get('values', [])

    return values


def formatFirstName(name):
    return name[0] + name[1:].lower()


def roundApproval(num):
    num = float(num.replace(',', ''))
    if num % 5000 == 0:
        num = "{:.2f}".format(num)
        return  "$" + addCommas(num)
    else:
        num = ((round(num / 10000) * 10000) / 2)
        num = "{:.2f}".format(num)
        return "$" + addCommas(num)
    

def addCommas(num):
    num = str(num)
    parts = num.split(".")
    integer_part = parts[0]
    length = len(integer_part)
    result = ""
    for i in range(length):
        if (i + 1) % 3 == 0 and i != length - 1:
            result = "," + integer_part[length - i - 1] + result
        else:
            result = integer_part[length - i - 1] + result
    if len(parts) > 1:
        result += "." + parts[1]
    return result


def formatBusinessName(businessName):
    for i in range(len(businessName)):
        if businessName[i] == '/':
            return capitalize_words(businessName[i + 2:])
            #make sure it gets properly capped for each word
            #also cut out inc llc llp or corp
    return capitalize_words(businessName)

def capitalize_words(text):
    words = text.split()
    if len(words) == 0:
        return ""
    last_word = words[-1].lower()
    if last_word in {"llc", "llp", "inc", "corp"}:
        words = words[:-1]
    capitalized_words = [word.capitalize() for word in words]
    return " ".join(capitalized_words)

def whichColumn(value):
    if len(value) < 10:
        return 7
    elif "(" in value or ")" in value:
        return 6
    else:
        return 7

#implement this at the end once you map out how everything else is gonna work
def equityNumber(value): #data[i][1]
    if value[3] == ' ':
        if int(value[:3]) >= 50:
            print('majority owner')
            print('skip next')
        else:
            print('skip this')
        

def formatNumber(number):
    return '1' + ''.join(filter(str.isdigit, number))


