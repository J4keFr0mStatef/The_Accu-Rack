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

#VVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVV
#Immensely important that this file is correctly located on the machine. Otherwise the API will fail.
#^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
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
    if not events:
        reminders = "No events found."

    else:
        for event in events:
            start = event['start'].get('dateTime', event['start'].get('date'))
            reminders.append(str(event['summary']))
        reminders = "\n".join(reminders)

    return reminders

#Main call for the reminder variable. This is the variable that should be used for the GUI. 
reminders = getReminder()



############################### KEYBOARD GUI #################################

import tkinter as tk
from tkinter import ttk
import requests

keyboard = tk.Tk()  # key window name
keyboard.title('Keyboard')  # title Name

exp = " "   # global variable 

#Showing all data in display 
def press(num):
    global exp
    exp=exp + str(num)
    CITY.set(exp)

#Function clear button

def clear():
    global exp
    exp = " "
    CITY.set(exp)

# Enter Button Function

def action():
    exp = ""
    ###########CHECK FOR CORRECT CITY FOR WEATHER API#############
    # base URL
    BASE_URL = "https://api.openweathermap.org/data/2.5/forecast?"

    # API key for open weather
    API_KEY = "c6fac2b39ddd7e66e83a0be39bd11f52"
    # updating the URL
    URL = BASE_URL + "q=" + CITY.get() + "&units=imperial" + "&appid=" + API_KEY
    # HTTP request
    response = requests.get(URL)
    # checking the status code of the request
    if response.status_code == 200: 
        keyboard.destroy()
    else:
        CITY.set("COULD NOT FIND CITY")

# Size window 

keyboard.geometry('740x250')

#Window color
keyboard.configure(bg = 'blue')   

# Entry box and setup for CITY variable used for API and GUI.
CITY = tk.StringVar()
Dis_entry = ttk.Entry(keyboard,state= 'readonly',textvariable = CITY)
Dis_entry.grid(rowspan= 1 , columnspan = 100, ipadx = 999 , ipady = 20)

# First Line Buttons

q = ttk.Button(keyboard,text = 'Q' , width = 6, command = lambda : press('Q'))
q.grid(row = 1 , column = 0, ipadx = 6 , ipady = 10)

w = ttk.Button(keyboard,text = 'W' , width = 6, command = lambda : press('W'))
w.grid(row = 1 , column = 1, ipadx = 6 , ipady = 10)

E = ttk.Button(keyboard,text = 'E' , width = 6, command = lambda : press('E'))
E.grid(row = 1 , column = 2, ipadx = 6 , ipady = 10)

R = ttk.Button(keyboard,text = 'R' , width = 6, command = lambda : press('R'))
R.grid(row = 1 , column = 3, ipadx = 6 , ipady = 10)

T = ttk.Button(keyboard,text = 'T' , width = 6, command = lambda : press('T'))
T.grid(row = 1 , column = 4, ipadx = 6 , ipady = 10)

Y = ttk.Button(keyboard,text = 'Y' , width = 6, command = lambda : press('Y'))
Y.grid(row = 1 , column = 5, ipadx = 6 , ipady = 10)

U = ttk.Button(keyboard,text = 'U' , width = 6, command = lambda : press('U'))
U.grid(row = 1 , column = 6, ipadx = 6 , ipady = 10)

I = ttk.Button(keyboard,text = 'I' , width = 6, command = lambda : press('I'))
I.grid(row = 1 , column = 7, ipadx = 6 , ipady = 10)

O = ttk.Button(keyboard,text = 'O' , width = 6, command = lambda : press('O'))
O.grid(row = 1 , column = 8, ipadx = 6 , ipady = 10)

P = ttk.Button(keyboard,text = 'P' , width = 6, command = lambda : press('P'))
P.grid(row = 1 , column = 9, ipadx = 6 , ipady = 10)

clear = ttk.Button(keyboard,text = 'Clear' , width = 6, command = clear)
clear.grid(row = 2 , column = 9, ipadx = 6 , ipady = 10)

# Second Line Buttons

A = ttk.Button(keyboard,text = 'A' , width = 6, command = lambda : press('A'))
A.grid(row = 2 , column = 0, ipadx = 6 , ipady = 10)

S = ttk.Button(keyboard,text = 'S' , width = 6, command = lambda : press('S'))
S.grid(row = 2 , column = 1, ipadx = 6 , ipady = 10)

D = ttk.Button(keyboard,text = 'D' , width = 6, command = lambda : press('D'))
D.grid(row = 2 , column = 2, ipadx = 6 , ipady = 10)

F = ttk.Button(keyboard,text = 'F' , width = 6, command = lambda : press('F'))
F.grid(row = 2 , column = 3, ipadx = 6 , ipady = 10)


G = ttk.Button(keyboard,text = 'G' , width = 6, command = lambda : press('G'))
G.grid(row = 2 , column = 4, ipadx = 6 , ipady = 10)


H = ttk.Button(keyboard,text = 'H' , width = 6, command = lambda : press('H'))
H.grid(row = 2 , column = 5, ipadx = 6 , ipady = 10)


J = ttk.Button(keyboard,text = 'J' , width = 6, command = lambda : press('J'))
J.grid(row = 2 , column = 6, ipadx = 6 , ipady = 10)


K = ttk.Button(keyboard,text = 'K' , width = 6, command = lambda : press('K'))
K.grid(row = 2 , column = 7, ipadx = 6 , ipady = 10)

L = ttk.Button(keyboard,text = 'L' , width = 6, command = lambda : press('L'))
L.grid(row = 2 , column = 8, ipadx = 6 , ipady = 10)



#Third line Buttons

Z = ttk.Button(keyboard,text = 'Z' , width = 6, command = lambda : press('Z'))
Z.grid(row = 3 , column = 1, ipadx = 6 , ipady = 10)


X = ttk.Button(keyboard,text = 'X' , width = 6, command = lambda : press('X'))
X.grid(row = 3 , column = 2, ipadx = 6 , ipady = 10)


C = ttk.Button(keyboard,text = 'C' , width = 6, command = lambda : press('C'))
C.grid(row = 3 , column = 3, ipadx = 6 , ipady = 10)


V = ttk.Button(keyboard,text = 'V' , width = 6, command = lambda : press('V'))
V.grid(row = 3 , column = 4, ipadx = 6 , ipady = 10)

B = ttk.Button(keyboard, text= 'B' , width = 6 , command = lambda : press('B'))
B.grid(row = 3 , column = 5, ipadx = 6 ,ipady = 10)


N = ttk.Button(keyboard,text = 'N' , width = 6, command = lambda : press('N'))
N.grid(row = 3 , column = 6, ipadx = 6 , ipady = 10)


M = ttk.Button(keyboard,text = 'M' , width = 6, command = lambda : press('M'))
M.grid(row = 3 , column = 7, ipadx = 6 , ipady = 10)


#Fourth Line Buttons

space = ttk.Button(keyboard,text = 'Space' , width = 6, command = lambda : press(' '))
space.grid(row = 4 , columnspan = 10 , ipadx = 116.5, ipady = 10)

enter = ttk.Button(keyboard,text = 'Enter' , width = 6, command = action)
enter.grid(row = 4, column = 9, ipadx = 6 , ipady = 10)


keyboard.mainloop() 

################################## MAIN GUI ########################################
from tkinter import *
class Application(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.grid()
        self.master.title("Grid Manager")

        for r in range(6):
            self.master.rowconfigure(r, weight=1)    
        for c in range(5):
            self.master.columnconfigure(c, weight=1)
            Button(master, text="Button {0}".format(c)).grid(row=6,column=c,sticky=E+W)

        Frame1 = Frame(master, bg="darkturquoise")
        Frame1.grid(row = 0, column = 0, rowspan = 3, columnspan = 2, sticky = W+E+N+S) 

        Label1A = Label(Frame1, text = "{}".format(CITY.get()), bg = "darkturquoise")
        Label1A.pack()

        Label1B = Label(Frame1, text = "Temperature and weather status here", bg = "darkturquoise")
        Label1B.place(relx = 0.5, rely = 0.5, anchor = CENTER)


        Frame2 = Frame(master, bg="SlateBlue2")
        Frame2.grid(row = 3, column = 0, rowspan = 3, columnspan = 2, sticky = W+E+N+S)

        Label2A = Label(Frame2, text = "Coat recommendation", bg = "SlateBlue2")
        Label2A.pack()

        Label2B = Label(Frame2, text = "Which coat here", bg = "SlateBlue2")
        Label2B.place(relx = 0.5, rely = 0.5, anchor = CENTER)


        Frame3 = Frame(master, bg="aquamarine")
        Frame3.grid(row = 0, column = 2, rowspan = 6, columnspan = 3, sticky = W+E+N+S)


        Label3A = Label(Frame3, text = "Reminders", bg = "aquamarine")
        Label3A.pack()

        Label3B = Label(Frame3, text = "{}".format(reminders), bg = "aquamarine")
        Label3B.place(relx = 0.5, rely = 0.5, anchor = CENTER)
        
        

Tk = Tk()
Tk.geometry("750x250")
app = Application(master=Tk)
app.mainloop()




########## WEATHER API INTEGRATION AND DATA GET ############
#TODO: BUGGED OUT CODE :( FIX IT 


# if response.status_code == 200:

#     # getting data in the json format
#     data = response.json()
#     # getting the main dict block
#     print(data)
#     main = data["main"]
#     # getting temperature
#     temperature = main['temp']
#     # getting the humidity
#     humidity = main['humidity']
#     # getting the pressure
#     pressure = main['pressure']
#     # getting the probability of precipitation
#     chance_rain = info['pop']
#     # weather report
#     report = info['weather']
#     print(f"{CITY:-^30}")
#     print(f"Temperature: {temperature}")
#     print(f"Humidity: {humidity}")
#     print(f"Pressure: {pressure}")
#     print(f"Weather Report: {report[0]['description']}")
#     print(f"Chance of Rain: {str(chance_rain * 100) + '%'}")
# else:
#     # showing the error message
#     print("Could not find city.")