# Automated-SMS (python)
## What it does
+ Uses Google Sheets API to persolize each text by grabbing name and company and other info from google sheet.
+ It then takes message and phone number and accesses the messaging platform via a headless browser and sends messages.
+ Then it repeats for whatever rows specified on initial request.
+ It then goes back to the google sheet and marks down all of those that it sent to.


## Link
 Intended to be run locally

## Technologies 
python with either PyQt or customTkinter (customTkinter is 1000% nicer looking) depending on what version, wrapped up with pyinstaller.
Uses Google Sheets as Database (that is what they wanted.)


## Introduction
A payed freelance contract for a money lending company.


## Accomplishments
+ That I succesfully developed and delivered a valuable software product to a customer.

## Instructions 
+ Adjust message as needed, refrain from interfering with bracketed values
+ Put the starting and ending row you wish to read in the marked inputs
+ Hit run and watch the magic happen



# Automated-SMS
Uses Google Sheets API to personalize text and grab numbers to Text Blast (uses a bot to automate interaction with escape sms platform). After messages sent it scrapes the responses and marks them with time stamps to allow for 
data collection.
