# import our written libraries
from weather_class import *
from Google_Calendar_API import *

# import external libraries
import RPi.GPIO as GPIO
import requests
from tkinter import *
from tkinter import ttk
from time import sleep as delay


weatherData = None
FULLSCREEN = True

class Coathook:
    coats = {"umbrella": 4, "raincoat": 25, "light coat": 24, "heavy coat": 5}
    leds = {"umbrella": 17, "raincoat": 16, "light coat": 13, "heavy coat": 12}

    def __init__(self):
        self.setupGPIO()
        self.letThereBeLight()
    
    def setupGPIO(self):
        GPIO.setmode(GPIO.BCM)
        GPIO.setwarnings(False)
        
        # setup the GPIO for the limit switches
        for coat in self.coats:
            GPIO.setup(self.coats[coat], GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
        # setup the GPIO for the LEDs
        for led in self.leds:
            GPIO.setup(self.leds[led], GPIO.OUT)

        for coat in self.coats:
            GPIO.add_event_detect(self.coats[coat], GPIO.BOTH, callback=self.letThereBeLight)

    def blink(self, led):
        GPIO.output(led, GPIO.LOW)
        delay(0.3)
        GPIO.output(led, GPIO.HIGH)
        delay(0.3)

    def recommend(self):
        recommendation = None
        if (True):
            if (weatherData.getRainChance() >= 0.75) and (weatherData.getTemp() >= 32):
                # RAINCOAT & UMBRELLA
                recommendation = self.leds["raincoat"]
                recommendation = self.leds["umbrella"]
            elif (weatherData.getRainChance() >= 0.6) and (weatherData.getTemp() >= 32):
                # "RAINCOAT"
                recommendation = self.leds["raincoat"]
            elif (weatherData.getRainChance() >= 0.3) and (weatherData.getTemp() >= 32):
                # "UMBRELLA"
                recommendation = self.leds["umbrella"]
            elif (weatherData.getTemp() <= 35):
                # "HEAVY COAT"
                recommendation = self.leds["heavy coat"]
            elif (weatherData.getTemp() <= 60):
                # "LIGHT COAT"
                recommendation = self.leds["light coat"]
            return recommendation

    def letThereBeLight(self, _=None):
        # check to see if coats are on the rack
        rec = self.recommend()
        for coat in self.coats:
            #if the coat is not there, turn the light off
            if (GPIO.input(self.coats[coat]) == 1):
                GPIO.output(self.leds[coat], GPIO.LOW)
            else:
                if rec == self.leds[coat]:
                    while (GPIO.input(self.coats[coat]) == 0):
                        self.blink(self.leds[coat])
                else:
                    GPIO.output(self.leds[coat], GPIO.HIGH)


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
        self.exp = " "

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
            GUI()
            self.keyboard.destroy()
            keyboardGUI()
        
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
class GUI():

    def __init__(self):
        GPIO.cleanup()
        coathanger = Coathook()
        self.setUpGUI()
        
    def setUpGUI(self):
        self.GUI = Tk()  # key window name
        self.GUI.title('The Accurack')  # title Name
        self.GUI.geometry("800x480")
        self.GUI.attributes("-fullscreen", FULLSCREEN)

        for r in range(6):
            self.GUI.rowconfigure(r, weight=1)    
        for c in range(5):
            self.GUI.columnconfigure(c, weight=1)
        
        self.Button1 = Button(self.GUI, text="Change city", command = lambda : self.changeCity(), font = "times 19 bold", highlightthickness = 2, highlightbackground = "black")
        self.Button1.grid(row = 6, column = 0, columnspan = 2, sticky = N + S +E + W)

        self.Button2 = Button(self.GUI, text = "°F/°C", command = lambda: self.changeTemp(), font = "times 19 bold", highlightthickness = 2, highlightbackground = "black")
        self.Button2.grid(row = 6, column = 2, columnspan = 2, sticky = N + S + E + W)

        self.Button3 = Button(self.GUI, text = "Refresh", command = lambda : self.refresh(), font = "times 19 bold", highlightthickness = 2, highlightbackground = "black")
        self.Button3.grid(row = 6, column = 4, columnspan = 2, sticky = N + S + E + W)

        self.Frame1 = Frame(self.GUI, bg="firebrick2", highlightthickness = 2, highlightbackground = "black")
        self.Frame1.grid(row = 0, column = 0, rowspan = 3, columnspan = 2, sticky = W+E+N+S) 

        self.Label1A = Label(self.Frame1, text = "{}".format(CITY.get()), font = "times 20 bold", bg = "firebrick2")
        self.Label1A.pack()

        self.Label1B = Label(self.Frame1, text = "{}".format(weatherData),font = "times 18", bg = "firebrick2")
        self.Label1B.place(relx = 0.5, rely = 0.5, anchor = CENTER)

        self.Frame2 = Frame(self.GUI, bg="firebrick2", highlightthickness = 2, highlightbackground = "black")
        self.Frame2.grid(row = 3, column = 0, rowspan = 3, columnspan = 2, sticky = W+E+N+S)

        self.Label2A = Label(self.Frame2, text = "Coat Recommendation:", font = "times 20 bold", bg = "firebrick2")
        self.Label2A.pack()

        self.Label2B = Label(self.Frame2, text = self.recommendCoat(), font = "times 19", bg = "firebrick2")
        self.Label2B.place(relx = 0.5, rely = 0.5, anchor = CENTER)

        self.Frame3 = Frame(self.GUI, bg="royal blue", highlightthickness = 2, highlightbackground = "black")
        self.Frame3.grid(row = 0, column = 2, rowspan = 6, columnspan = 3, sticky = W+E+N+S)

        self.Label3A = Label(self.Frame3, text = "Reminders {}".format(datetime.datetime.now().today().strftime("%A %B %d")), font = "times 20 bold", bg = "royal blue")
        self.Label3A.pack()

        reminders = getReminder()
        self.Label3B = Label(self.Frame3, text = "{}".format(reminders), font = "times 19",bg = "royal blue")
        self.Label3B.place(relx = 0.5, rely = 0.5, anchor = CENTER)

        self.GUI.config(cursor = "none")
        self.GUI.mainloop()
        
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
    
    # change city function
    def changeCity(self):
        self.GUI.destroy()
        

    # refresh function
    # WIP still experimenting with this
    # temporary implementation of this addition
    def refresh(self):
        weatherData = Weather("{}".format(CITY.get()))

        self.Label1A.config(text = "{}".format(CITY.get()))
        self.Label1B.config(text = "{}".format(weatherData))

        self.Label2B.config(text = self.recommendCoat())

        self.Label3A.config(text = "Reminders {}".format(datetime.datetime.now().today().strftime("%A %B %d")))
        
        reminders = getReminder()
        self.Label3B.config(text = "{}".format(reminders))

    def changeTemp(self):
        global weatherData
        if weatherData.unit == "imperial":
            weatherData = Weather("{}".format(CITY.get()), "metric")
            self.Label1B.config(text = "{}".format(weatherData))
        else:
            weatherData = Weather("{}".format(CITY.get()), "imperial")
            self.Label1B.config(text = "{}".format(weatherData))
    

###### MAIN CODE #######
def main():
    keyboardGUI()

