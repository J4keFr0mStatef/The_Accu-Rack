
############################### KEYBOARD GUI #################################

import tkinter as tk
from tkinter import ttk
import requests

key = tk.Tk()  # key window name
key.title('Keyboard')  # title Name

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
        key.destroy()
    else:
        CITY.set("COULD NOT FIND CITY")

# Size window size

key.geometry('1010x250')         # normal size
key.maxsize(width=1010, height=250)      # maximum size
key.minsize(width= 1010 , height = 250)     # minimum size
# end window size

key.configure(bg = 'blue')    #  add background color

# Entry box and setup for CITY variable used for API and GUI.
CITY = tk.StringVar()
Dis_entry = ttk.Entry(key,state= 'readonly',textvariable = CITY)
Dis_entry.grid(rowspan= 1 , columnspan = 100, ipadx = 999 , ipady = 20)

# First Line Buttons

q = ttk.Button(key,text = 'Q' , width = 6, command = lambda : press('Q'))
q.grid(row = 1 , column = 0, ipadx = 6 , ipady = 10)

w = ttk.Button(key,text = 'W' , width = 6, command = lambda : press('W'))
w.grid(row = 1 , column = 1, ipadx = 6 , ipady = 10)

E = ttk.Button(key,text = 'E' , width = 6, command = lambda : press('E'))
E.grid(row = 1 , column = 2, ipadx = 6 , ipady = 10)

R = ttk.Button(key,text = 'R' , width = 6, command = lambda : press('R'))
R.grid(row = 1 , column = 3, ipadx = 6 , ipady = 10)

T = ttk.Button(key,text = 'T' , width = 6, command = lambda : press('T'))
T.grid(row = 1 , column = 4, ipadx = 6 , ipady = 10)

Y = ttk.Button(key,text = 'Y' , width = 6, command = lambda : press('Y'))
Y.grid(row = 1 , column = 5, ipadx = 6 , ipady = 10)

U = ttk.Button(key,text = 'U' , width = 6, command = lambda : press('U'))
U.grid(row = 1 , column = 6, ipadx = 6 , ipady = 10)

I = ttk.Button(key,text = 'I' , width = 6, command = lambda : press('I'))
I.grid(row = 1 , column = 7, ipadx = 6 , ipady = 10)

O = ttk.Button(key,text = 'O' , width = 6, command = lambda : press('O'))
O.grid(row = 1 , column = 8, ipadx = 6 , ipady = 10)

P = ttk.Button(key,text = 'P' , width = 6, command = lambda : press('P'))
P.grid(row = 1 , column = 9, ipadx = 6 , ipady = 10)

clear = ttk.Button(key,text = 'Clear' , width = 6, command = clear)
clear.grid(row = 1 , column = 13, ipadx = 20 , ipady = 10)

# Second Line Buttons

A = ttk.Button(key,text = 'A' , width = 6, command = lambda : press('A'))
A.grid(row = 2 , column = 0, ipadx = 6 , ipady = 10)

S = ttk.Button(key,text = 'S' , width = 6, command = lambda : press('S'))
S.grid(row = 2 , column = 1, ipadx = 6 , ipady = 10)

D = ttk.Button(key,text = 'D' , width = 6, command = lambda : press('D'))
D.grid(row = 2 , column = 2, ipadx = 6 , ipady = 10)

F = ttk.Button(key,text = 'F' , width = 6, command = lambda : press('F'))
F.grid(row = 2 , column = 3, ipadx = 6 , ipady = 10)


G = ttk.Button(key,text = 'G' , width = 6, command = lambda : press('G'))
G.grid(row = 2 , column = 4, ipadx = 6 , ipady = 10)


H = ttk.Button(key,text = 'H' , width = 6, command = lambda : press('H'))
H.grid(row = 2 , column = 5, ipadx = 6 , ipady = 10)


J = ttk.Button(key,text = 'J' , width = 6, command = lambda : press('J'))
J.grid(row = 2 , column = 6, ipadx = 6 , ipady = 10)


K = ttk.Button(key,text = 'K' , width = 6, command = lambda : press('K'))
K.grid(row = 2 , column = 7, ipadx = 6 , ipady = 10)

L = ttk.Button(key,text = 'L' , width = 6, command = lambda : press('L'))
L.grid(row = 2 , column = 8, ipadx = 6 , ipady = 10)

enter = ttk.Button(key,text = 'Enter' , width = 6, command = action)
enter.grid(row = 2 , column = 13, ipadx = 20 , ipady = 10)

#Third line Buttons

Z = ttk.Button(key,text = 'Z' , width = 6, command = lambda : press('Z'))
Z.grid(row = 3 , column = 0, ipadx = 6 , ipady = 10)


X = ttk.Button(key,text = 'X' , width = 6, command = lambda : press('X'))
X.grid(row = 3 , column = 1, ipadx = 6 , ipady = 10)


C = ttk.Button(key,text = 'C' , width = 6, command = lambda : press('C'))
C.grid(row = 3 , column = 2, ipadx = 6 , ipady = 10)


V = ttk.Button(key,text = 'V' , width = 6, command = lambda : press('V'))
V.grid(row = 3 , column = 3, ipadx = 6 , ipady = 10)

B = ttk.Button(key, text= 'B' , width = 6 , command = lambda : press('B'))
B.grid(row = 3 , column = 4 , ipadx = 6 ,ipady = 10)


N = ttk.Button(key,text = 'N' , width = 6, command = lambda : press('N'))
N.grid(row = 3 , column = 5, ipadx = 6 , ipady = 10)


M = ttk.Button(key,text = 'M' , width = 6, command = lambda : press('M'))
M.grid(row = 3 , column = 6, ipadx = 6 , ipady = 10)


shift = ttk.Button(key,text = 'Shift' , width = 6, command = lambda : press('Shift'))
shift.grid(row = 3 , column = 13, ipadx = 20 , ipady = 10)


#Fourth Line Buttons

space = ttk.Button(key,text = 'Space' , width = 6, command = lambda : press(' '))
space.grid(row = 4 , columnspan = 10 , ipadx = 120, ipady = 10)



key.mainloop()  # loop GUI

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

        Label3B = Label(Frame3, text = "reminder", bg = "aquamarine")
        Label3B.place(relx = 0.5, rely = 0.5, anchor = CENTER)
        
        

Tk = Tk()
Tk.geometry("400x200+200+200")
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