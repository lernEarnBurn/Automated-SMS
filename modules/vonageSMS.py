import vonage
from dotenv import load_dotenv
import os

load_dotenv()

def mockSend(message, phoneNumber):
   return 'sent ' + message + ' to ' + phoneNumber

def sendMessage(message, phoneNumber):
   client = vonage.Client(os.getenv('vonageApiKey'), secret=os.getenv('vonageApiSecret'))
   sms = vonage.Sms(client)

   responseData = sms.send_message(
      {
         "from": "userPhoneNumber",
         "to": phoneNumber,
         "text": message,
      }
   )

   if responseData["messages"][0]["status"] == "0":
      return f"{message} sent successfully to {phoneNumber}"
   else:
      return f"failed to send message to {phoneNumber}"

def formatPhoneNum(num):
   return