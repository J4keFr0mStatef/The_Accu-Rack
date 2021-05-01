# GPIO event listener module
# https://sourceforge.net/p/raspberry-gpio-python/wiki/Inputs/

# import our written libraries
from weather_class import *
from Google_Calendar_API import *

# import external libraries
import requests
from tkinter import *
from tkinter import ttk
from time import sleep

FULLSCREEN = False

class keyboardGUI:
    def __init__(self):
        self.setupKeys()
    
    #Showing all data in display 
    def press(self,num):
        self.exp = self.exp + str(num)
        CITY.set(self.exp)

    #Clear button function

    def clear(self):
        self.exp = " "
        CITY.set(self.exp)

    # Enter Button Function

    def action(self):
        self.exp = ""

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
            global weatherData
            weatherData = Weather("{}".format(CITY.get())) 
            self.keyboard.destroy()
        else:
            CITY.set("COULD NOT FIND CITY")

    def setupKeys(self):
        self.keyboard = Tk()  # key window name
        self.keyboard.title('Keyboard')  # title Name
        self.keyboard.attributes("-fullscreen", FULLSCREEN)
        self.keyboard.config(cursor = "none")

        self.exp = " "   # global variable 

        # Size window 
        self.keyboard.geometry('800x480')

        #Window color
        self.keyboard.configure(bg = 'blue')

        # Entry box and setup for CITY variable used for API and GUI.
        global CITY
        CITY = StringVar()
        self.Dis_entry = ttk.Entry(self.keyboard,state= 'readonly',textvariable = CITY)
        self.Dis_entry.grid(rowspan = 1, columnspan = 330, ipadx = 330, ipady = 40)

        # First Line Buttons
        q = ttk.Button(self.keyboard,text = 'Q' , width = 7, command = lambda : self.press('Q'))
        q.grid(row = 1 , column = 0, ipadx = 7 , ipady = 20)

        w = ttk.Button(self.keyboard,text = 'W' , width = 7, command = lambda : self.press('W'))
        w.grid(row = 1 , column = 1, ipadx = 7 , ipady = 20)

        E = ttk.Button(self.keyboard,text = 'E' , width = 7, command = lambda : self.press('E'))
        E.grid(row = 1 , column = 2, ipadx = 7 , ipady = 20)

        R = ttk.Button(self.keyboard,text = 'R' , width = 7, command = lambda : self.press('R'))
        R.grid(row = 1 , column = 3, ipadx = 7 , ipady = 20)

        T = ttk.Button(self.keyboard,text = 'T' , width = 7, command = lambda : self.press('T'))
        T.grid(row = 1 , column = 4, ipadx = 7 , ipady = 20)
        
        Y = ttk.Button(self.keyboard,text = 'Y' , width = 7, command = lambda : self.press('Y'))
        Y.grid(row = 1 , column = 5, ipadx = 7 , ipady = 20)

        U = ttk.Button(self.keyboard,text = 'U' , width = 7, command = lambda : self.press('U'))
        U.grid(row = 1 , column = 6, ipadx = 7 , ipady = 20)

        I = ttk.Button(self.keyboard,text = 'I' , width = 7, command = lambda : self.press('I'))
        I.grid(row = 1 , column = 7, ipadx = 7 , ipady = 20)

        O = ttk.Button(self.keyboard,text = 'O' , width = 7, command = lambda : self.press('O'))
        O.grid(row = 1 , column = 8, ipadx = 7 , ipady = 20)

        P = ttk.Button(self.keyboard,text = 'P' , width = 7, command = lambda : self.press('P'))
        P.grid(row = 1 , column = 9, ipadx = 7 , ipady = 20)

        clear = ttk.Button(self.keyboard,text = 'Clear' , width = 7, command = self.clear)
        clear.grid(row = 2 , column = 9, ipadx = 7 , ipady = 20)

        # Second Line Buttons
        A = ttk.Button(self.keyboard,text = 'A' , width = 7, command = lambda : self.press('A'))
        A.grid(row = 2 , column = 0, ipadx = 7 , ipady = 20)

        S = ttk.Button(self.keyboard,text = 'S' , width = 7, command = lambda : self.press('S'))
        S.grid(row = 2 , column = 1, ipadx = 7 , ipady = 20)

        D = ttk.Button(self.keyboard,text = 'D' , width = 7, command = lambda : self.press('D'))
        D.grid(row = 2 , column = 2, ipadx = 7 , ipady = 20)

        F = ttk.Button(self.keyboard,text = 'F' , width = 7, command = lambda : self.press('F'))
        F.grid(row = 2 , column = 3, ipadx = 7 , ipady = 20)

        G = ttk.Button(self.keyboard,text = 'G' , width = 7, command = lambda : self.press('G'))
        G.grid(row = 2 , column = 4, ipadx = 7 , ipady = 20)

        H = ttk.Button(self.keyboard,text = 'H' , width = 7, command = lambda : self.press('H'))
        H.grid(row = 2 , column = 5, ipadx = 7 , ipady = 20)

        J = ttk.Button(self.keyboard,text = 'J' , width = 7, command = lambda : self.press('J'))
        J.grid(row = 2 , column = 6, ipadx = 7 , ipady = 20)

        K = ttk.Button(self.keyboard,text = 'K' , width = 7, command = lambda : self.press('K'))
        K.grid(row = 2 , column = 7, ipadx = 7 , ipady = 20)

        L = ttk.Button(self.keyboard,text = 'L' , width = 7, command = lambda : self.press('L'))
        L.grid(row = 2 , column = 8, ipadx = 7 , ipady = 20)

        #Third line Buttons
        Z = ttk.Button(self.keyboard,text = 'Z' , width = 7, command = lambda : self.press('Z'))
        Z.grid(row = 3 , column = 1, ipadx = 7 , ipady = 20)

        X = ttk.Button(self.keyboard,text = 'X' , width = 7, command = lambda : self.press('X'))
        X.grid(row = 3 , column = 2, ipadx = 7 , ipady = 20)

        C = ttk.Button(self.keyboard,text = 'C' , width = 7, command = lambda : self.press('C'))
        C.grid(row = 3 , column = 3, ipadx = 7 , ipady = 20)

        V = ttk.Button(self.keyboard,text = 'V' , width = 7, command = lambda : self.press('V'))
        V.grid(row = 3 , column = 4, ipadx = 7 , ipady = 20)

        B = ttk.Button(self.keyboard, text= 'B' , width = 7 , command = lambda : self.press('B'))
        B.grid(row = 3 , column = 5, ipadx = 7 ,ipady = 20)

        N = ttk.Button(self.keyboard,text = 'N' , width = 7, command = lambda : self.press('N'))
        N.grid(row = 3 , column = 6, ipadx = 7 , ipady = 20)

        M = ttk.Button(self.keyboard,text = 'M' , width = 7, command = lambda : self.press('M'))
        M.grid(row = 3 , column = 7, ipadx = 7 , ipady = 20)

        #Fourth Line Buttons
        space = ttk.Button(self.keyboard,text = 'Space' , width = 7, command = lambda : self.press(' '))
        space.grid(row = 4 , columnspan = 10 , ipadx = 116.5, ipady = 10)

        enter = ttk.Button(self.keyboard,text = 'Enter' , width = 7, command = self.action)
        enter.grid(row = 4, column = 9, ipadx = 6 , ipady = 20)

        self.keyboard.mainloop() 


################################## MAIN GUI ########################################
class Application(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.grid()
        self.master.title("The Accurack")
        self.setUpGUI()

    def setUpGUI(self):
        for r in range(6):
            self.master.rowconfigure(r, weight=1)    
        for c in range(5):
            self.master.columnconfigure(c, weight=1)
           
        Button1 = Button(self.master, text="Change city", command = self.destroy())
        Button1.grid(row=6,column=0,sticky=E+W)

        Frame1 = Frame(self.master, bg="red2")
        Frame1.grid(row = 0, column = 0, rowspan = 3, columnspan = 2, sticky = W+E+N+S) 

        Label1A = Label(Frame1, text = "{}".format(CITY.get()), font = "times 20 bold", bg = "red2")
        Label1A.pack()

        Label1B = Label(Frame1, text = "{}".format(weatherData),font = "times 20", bg = "red2")
        Label1B.place(relx = 0.5, rely = 0.5, anchor = CENTER)

        Frame2 = Frame(self.master, bg="red2")
        Frame2.grid(row = 3, column = 0, rowspan = 3, columnspan = 2, sticky = W+E+N+S)

        Label2A = Label(Frame2, text = "Coat Recommendation:", font = "times 20 bold", bg = "red2")
        Label2A.pack()

        Label2B = Label(Frame2, text = self.recommendCoat(), font = "times 20", bg = "red2")
        Label2B.place(relx = 0.5, rely = 0.5, anchor = CENTER)

        Frame3 = Frame(self.master, bg="blue2")
        Frame3.grid(row = 0, column = 2, rowspan = 6, columnspan = 3, sticky = W+E+N+S)

        Label3A = Label(Frame3, text = "Reminders {}".format(datetime.datetime.now().today().strftime("%A %B %d")), font = "times 20 bold", bg = "blue2")
        Label3A.pack()

        reminders = getReminder()
        Label3B = Label(Frame3, text = "{}".format(reminders), font = "times 20",bg = "blue2")
        Label3B.place(relx = 0.5, rely = 0.5, anchor = CENTER)
    
    def changeCity(self):
        self.destroy()
    

    # rain chance >= 60, RAINCOAT
    # rain chance >= 30, UMBRELLA
    # rain chance >= 75, BOTH
    # temp < 60 and rain chance <30, LIGHT COAT
    # temp < 35, HEAVY COAT
    def recommendCoat(self):
        weatherData.ping()
        s = "I recommend you take a(n)\n"
        if (weatherData.getRainChance() >= 0.75) and (weatherData.getTemp() >= 32):
            s = "I recommend both an\nUMBRELLA and a RAIN COAT"
        elif (weatherData.getRainChance() >= 0.6) and (weatherData.getTemp() >= 32):
            s += "RAINCOAT"
        elif (weatherData.getRainChance() >= 0.3) and (weatherData.getTemp() >= 32):
            s += "UMBRELLA"
        elif (weatherData.getTemp() <= 35):
            s += "HEAVY COAT"
        elif (weatherData.getTemp() <= 60):
            s += "LIGHT COAT"
        else:
            s = "It looks like you're good\nto go today!\nHave a great day!"

        return s



###### MAIN CODE #######
keyboardGUI()
GUI = Tk()
GUI.geometry("800x480")
GUI.config(cursor = "none")
app = Application(master=GUI)
GUI.attributes("-fullscreen", FULLSCREEN)
app.mainloop()
