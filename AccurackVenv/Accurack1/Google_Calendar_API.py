######## REQUIRED LIBRARIES FOR GOOGLE CALENDAR API ########

import datetime 
import pickle
import os.path
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request

################ GOOGLE CALENDAR API GET #######################

#Authorization for different portions of the google calendar API.
SCOPES = ['https://www.googleapis.com/auth/calendar']

#vvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvv#
#Immensely important that this file is correctly located on the machine. Otherwise the API will fail.#
#^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^#
CREDENTIALS_FILE = 'C:\google calendar api\credentials.json'

#Function will verify and allow access to google calendar
def get_calendar_service():
    creds = None
    # The file token.pickle stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
    if os.path.exists('token.pickle'):
        with open('token.pickle', 'rb') as token:
            creds = pickle.load(token)
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(CREDENTIALS_FILE, SCOPES)
            creds = flow.run_local_server(port=0)

        # Save the credentials for the next run
        with open('token.pickle', 'wb') as token:
            pickle.dump(creds, token)

    service = build('calendar', 'v3', credentials=creds)
    return service

#Function that pulls events from google calendar and returns them as a variable.
def getReminder():
    service = get_calendar_service()
    # Call the Calendar API
    now = datetime.datetime.utcnow().isoformat() + 'Z' # 'Z' indicates UTC tim
    events_result = service.events().list(
        calendarId='primary', timeMin=now,
        maxResults=10, singleEvents=True,
        orderBy='startTime').execute()
    events = events_result.get('items', [])
    reminders = []
    #check if there are events listed
    
    for event in events:
        #Pull the start time from the API for the event
        time1 = str(event['start']['dateTime'])
        #convert into a datetime from ISO format so we can use it
        dt = datetime.datetime.fromisoformat(time1)
        #convert date time into HOUR:MINUTE AM/PM format
        time2 = dt.strftime("%I:%M %p")
        #pull current time
        now = datetime.datetime.now()
        if dt.strftime("%m%d%Y") == now.strftime("%m%d%Y"): #check if the event falls on the current date
            #append event to todays reminders
            reminders.append(str(event['summary'])+" @ "+str(time2))
    #list all reminders seperated by a line in string format
    if reminders == []:
        reminders = "No events found."
    else:
        reminders = "\n".join(reminders)

    return reminders
#Main call for the reminder variable. This is the variable that should be used for the GUI. 
reminders = getReminder()

