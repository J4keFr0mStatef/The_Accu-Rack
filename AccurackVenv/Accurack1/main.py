######################################################################################################
#THE ACCURACK MAIN CODE
#LOUISIANA TECH UNIVERSITY CSC 132 PROJECT
#MEMBERS: GREGORY WHITEHURST, TRAVIS KNIPPERS, JOHN DOHERTY
#COMPLETION DATE: 5/11/2021 
######################################################################################################

# import our written libraries
from weather_class import *
from Google_Calendar_API import *
# import external libraries
import RPi.GPIO as GPIO
import requests
from tkinter import *
from tkinter import ttk
from time import sleep as delay
import threading

#create variable to contain the weather data from the weather API. 
weatherData = None

#Boolean to turn off and on fullscreen for debugging
FULLSCREEN = True

# the Coathook class encompasses the entire GUI
# it is a class so that it has self-sustained
# variables.
class Coathook:
    # dictionary that matches every LED pin and limit switch
    # input pin to a specific coat
    coats = {"umbrella": 4, "raincoat": 25, "light coat": 24, "heavy coat": 5}
    leds = {"umbrella": 17, "raincoat": 16, "light coat": 13, "heavy coat": 12}

    def __init__(self):
        self.setupGPIO()

    # create all the GPIO pins and initialise them
    def setupGPIO(self):
        GPIO.setmode(GPIO.BCM)
        GPIO.setwarnings(False)
       
        # setup the GPIO for the limit switches
        for coat in self.coats:
            GPIO.setup(self.coats[coat], GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
        # setup the GPIO for the LEDs
        for led in self.leds:
            GPIO.setup(self.leds[led], GPIO.OUT)
        # event listener module allows detection for
        # limit switch input pins so the LEDs can update
        # every time one is pressed
        for coat in self.coats:
            GPIO.add_event_detect(self.coats[coat], GPIO.BOTH, callback=self.letThereBeLight)

    # func used to blink an LED for a recommended coat
    def blink(self, led):
        while (GPIO.input(led) == 1):
            check = coathanger.recommend()
            GPIO.output(led, GPIO.LOW)
            delay(0.5)
            GPIO.output(led, GPIO.HIGH)
            delay(0.5)
            if (check != led):
                break

    # this func controls the logic for which coat is recommended
    # it is logically identitcal to the GUI's recommend function
    def recommend(self):
        recommendation = None

        temperature, humidity, rainPOP = weatherData.giveInfo()
        
        # recommendation logic for Fahrenheit
        if (weatherData.unit == "imperial"):
            if (rainPOP >= 0.7) and (temperature >= 32):
                # RAINCOAT & UMBRELLA
                recommendation = self.leds["raincoat"]
                recommendation = self.leds["umbrella"]
            elif (rainPOP >= 0.55) and (temperature >= 32):
                # "RAINCOAT"
                recommendation = self.leds["raincoat"]
            elif (rainPOP >= 0.3) and (temperature >= 32):
                # "UMBRELLA"
                recommendation = self.leds["umbrella"]
            elif (temperature <= 45):
                # "HEAVY COAT"
                recommendation = self.leds["heavy coat"]
            elif (temperature <= 65):
                # "LIGHT COAT"
                recommendation = self.leds["light coat"]
            
        # recommendation logic for Celsius
        else:
            if (rainPOP >= 0.7) and (temperature >= 0):
                # RAINCOAT & UMBRELLA
                recommendation = self.leds["raincoat"]
                recommendation = self.leds["umbrella"]
            elif (rainPOP >= 0.55) and (temperature >= 0):
                # "RAINCOAT"
                recommendation = self.leds["raincoat"]
            elif (rainPOP >= 0.3) and (temperature >= 0):
                # "UMBRELLA"
                recommendation = self.leds["umbrella"]
            elif (temperature <= 8):
                # "HEAVY COAT"
                recommendation = self.leds["heavy coat"]
            elif (temperature <= 16):
                # "LIGHT COAT"
                recommendation = self.leds["light coat"]

        return recommendation

    # the most fundamental function to the coatrack's switches
    # this function updates all the switches' current states
    def letThereBeLight(self, _=None):
        # check to see if coats are on the rack
        rec = self.recommend()
        for coat in self.coats:
            #if the coat is not there, turn the light off
            if (GPIO.input(self.coats[coat]) == 1):
                GPIO.output(self.leds[coat], GPIO.LOW)
            else:
                GPIO.output(self.leds[coat], GPIO.HIGH)

        try:
            # find the coat tied to the led pin that was recommended
            ledsKeyList = list(self.leds.keys())
            ledsValList = list(self.leds.values())
            position = ledsKeyList[ledsValList.index(rec)]
            # blink the led of the recommended
            if GPIO.input(self.coats[position]) == 0:
                test = threading.Thread(target=self.blink, args=(rec,), daemon=True)
                test.start()
        except:
            pass
            

# keyboard class allows for user input of a city
class keyboardGUI:
    #constructor
    def __init__(self):
        self.setupKeys()
    
    #Function to append each key press on the keyboard into the entry box. 
    def press(self,num):
        if str(CITY.get()) == "TYPE IN YOUR CITY":
            self.exp = " "
            CITY.set(self.exp)
        self.exp = self.exp + str(num)
        CITY.set(self.exp)

    #Clear button function
    def clear(self):
        self.exp = " "
        CITY.set(self.exp)

    # Enter Button Function
    def action(self):
        self.exp = " "
        #API Check for correct city

        # base URL
        BASE_URL = "https://api.openweathermap.org/data/2.5/forecast?"

        # API key for open weather
        API_KEY = "c6fac2b39ddd7e66e83a0be39bd11f52"

        # updating the URL
        URL = BASE_URL + "q=" + CITY.get() + "&units=imperial" + "&appid=" + API_KEY

        # HTTP request
        response = requests.get(URL)

        # check if the city input is valid
        if response.status_code == 200:
            global weatherData 
            weatherData = Weather("{}".format(CITY.get())) #Pull weather data from the API
            GUI() #run GUI
            self.keyboard.destroy()
            keyboardGUI()
        
        else:
            #if city is invalid
            CITY.set("COULD NOT FIND CITY")

    def setupKeys(self):
        self.keyboard = Tk()  # key window name
        self.keyboard.title('Keyboard')  # title name
        self.keyboard.attributes("-fullscreen", FULLSCREEN) #fullscreen attribute
        self.keyboard.config(cursor = "none") #removes cursor
        self.exp = " "   # variable for the text box 
    
        # Size window 
        self.keyboard.geometry('800x480')

        #Window color
        self.keyboard.configure(bg = 'blue')

        # Entry box and setup for CITY variable used for API and GUI.
        global CITY
        CITY = StringVar()
        CITY.set("TYPE IN YOUR CITY")
        self.Dis_entry = ttk.Entry(self.keyboard,state= 'readonly',textvariable = CITY)
        self.Dis_entry.grid(rowspan = 1, columnspan = 330, ipadx = 330, ipady = 40)

        #Create keyboard buttons:

        # First Line Buttons    
        Q = ttk.Button(self.keyboard,text = 'Q' , width = 7, command = lambda : self.press('Q'))
        Q.grid(row = 1 , column = 0, ipadx = 7 , ipady = 20)

        W = ttk.Button(self.keyboard,text = 'W' , width = 7, command = lambda : self.press('W'))
        W.grid(row = 1 , column = 1, ipadx = 7 , ipady = 20)

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

        clear = ttk.Button(self.keyboard,text = 'Clear' , width = 7, command = self.clear)
        clear.grid(row = 2 , column = 9, ipadx = 7 , ipady = 20)

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
    #constructor
    def __init__(self):
        GPIO.cleanup()
        global coathanger
        coathanger = Coathook()
        self.setUpGUI()
    
    def setUpGUI(self):
        self.GUI = Tk()  # key window name
        self.GUI.title('The Accurack')  # title Name
        self.GUI.geometry("800x480") #sizing the window out of fullscreen
        self.GUI.attributes("-fullscreen", FULLSCREEN) #fullscreen attribute

        #create grid for GUI
        for r in range(6):
            self.GUI.rowconfigure(r, weight=1)    
        for c in range(5):
            self.GUI.columnconfigure(c, weight=1)
        
        #Change city button
        self.Button1 = Button(self.GUI, text="Change city", command = lambda : self.changeCity(), font = "times 19 bold", highlightthickness = 2, highlightbackground = "black")
        self.Button1.grid(row = 6, column = 0, columnspan = 2, sticky = N + S +E + W)

        #°F/°C button
        self.Button2 = Button(self.GUI, text = "°F/°C", command = lambda: self.changeTemp(), font = "times 19 bold", highlightthickness = 2, highlightbackground = "black")
        self.Button2.grid(row = 6, column = 2, columnspan = 2, sticky = N + S + E + W)

        #Refresh button
        self.Button3 = Button(self.GUI, text = "Refresh", command = lambda : self.refresh(), font = "times 19 bold", highlightthickness = 2, highlightbackground = "black")
        self.Button3.grid(row = 6, column = 4, columnspan = 2, sticky = N + S + E + W)

        #background frame for the weather data
        self.Frame1 = Frame(self.GUI, bg="firebrick2", highlightthickness = 2, highlightbackground = "black")
        self.Frame1.grid(row = 0, column = 0, rowspan = 3, columnspan = 2, sticky = W+E+N+S) 

        #City label
        self.Label1A = Label(self.Frame1, text = "{}".format(CITY.get()), font = "times 20 bold", bg = "firebrick2")
        self.Label1A.pack()

        #weather data display
        self.Label1B = Label(self.Frame1, text = "{}".format(weatherData),font = "times 18", bg = "firebrick2")
        self.Label1B.place(relx = 0.5, rely = 0.5, anchor = CENTER)

        #background frame for the coat recommendation
        self.Frame2 = Frame(self.GUI, bg="firebrick2", highlightthickness = 2, highlightbackground = "black")
        self.Frame2.grid(row = 3, column = 0, rowspan = 3, columnspan = 2, sticky = W+E+N+S)

        #coat label
        self.Label2A = Label(self.Frame2, text = "Coat Recommendation:", font = "times 20 bold", bg = "firebrick2")
        self.Label2A.pack()

        #coat recommmendation display
        self.Label2B = Label(self.Frame2, text = self.recommendCoat(), font = "times 19", bg = "firebrick2")
        self.Label2B.place(relx = 0.5, rely = 0.5, anchor = CENTER)

        #background frame for the google calendar reminders
        self.Frame3 = Frame(self.GUI, bg="royal blue", highlightthickness = 2, highlightbackground = "black")
        self.Frame3.grid(row = 0, column = 2, rowspan = 6, columnspan = 3, sticky = W+E+N+S)

        #reminders + date label
        self.Label3A = Label(self.Frame3, text = "Reminders {}".format(datetime.datetime.now().today().strftime("%A %B %d")), font = "times 20 bold", bg = "royal blue")
        self.Label3A.pack()

        #reminders display 
        reminders = getReminder()
        self.Label3B = Label(self.Frame3, text = "{}".format(reminders), font = "times 19",bg = "royal blue")
        self.Label3B.place(relx = 0.5, rely = 0.5, anchor = CENTER)
        
        self.GUI.config(cursor = "none") #disable the user's cursor
        self.GUI.mainloop() #loop GUI

        coathanger.letThereBeLight()
        
    # function to recommend coats on-screen
    # this function handles the logic and returns a string
    # that recommends the coat
    def recommendCoat(self):
        # refresh LEDs
        coathanger.letThereBeLight()
        
        temperature, humidity, rainPOP = weatherData.giveInfo()
        
        s = "I recommend you take a(n)\n"
        # logic for Fahrenheit
        if (weatherData.unit == "imperial"):
            if (rainPOP >= 0.7) and (temperature >= 32):
                s = "I recommend both an\nUMBRELLA and a RAIN COAT"
            elif (rainPOP >= 0.55) and (temperature >= 32):
                s += "RAINCOAT"
            elif (rainPOP >= 0.3) and (temperature >= 32):
                s += "UMBRELLA"
            elif (temperature <= 45):
                s += "HEAVY COAT"
            elif (temperature <= 65):
                s += "LIGHT COAT"
            else:
                s = "It looks like you're good\nto go today!\nHave a great day!"

        # logic for celsius
        else:
            if (rainPOP >= 0.7) and (temperature >= 0):
                s = "I recommend both an\nUMBRELLA and a RAIN COAT"
            elif (rainPOP >= 0.55) and (temperature >= 0):
                s += "RAINCOAT"
            elif (rainPOP >= 0.3) and (temperature >= 0):
                s += "UMBRELLA"
            elif (temperature <= 8):
                s += "HEAVY COAT"
            elif (temperature <= 16):
                s += "LIGHT COAT"
            else:
                s = "It looks like you're good\nto go today!\nHave a great day!"
        return s
    
    # change city function
    def changeCity(self):
        coathanger.letThereBeLight()
        self.GUI.destroy()
        
    # refreshes all the weather data
    def refresh(self):
        global weatherData
        unit = weatherData.unit
        weatherData = Weather("{}".format(CITY.get()), unit)
        coathanger.letThereBeLight()

        self.Label1A.config(text = "{}".format(CITY.get()))
        self.Label1B.config(text = "{}".format(weatherData))

        self.Label2B.config(text = self.recommendCoat())

        self.Label3A.config(text = "Reminders {}".format(datetime.datetime.now().today().strftime("%A %B %d")))
        
        reminders = getReminder()
        self.Label3B.config(text = "{}".format(reminders))

    # °F/°C change function
    def changeTemp(self):
        global weatherData
        coathanger.letThereBeLight()
        if weatherData.unit == "imperial":
            weatherData = Weather("{}".format(CITY.get()), "metric")
            self.Label1B.config(text = "{}".format(weatherData))
        else:
            weatherData = Weather("{}".format(CITY.get()), "imperial")
            self.Label1B.config(text = "{}".format(weatherData))
            
        self.refresh()
    

######### MAIN CODE ##########
def main():
    keyboardGUI()

if __name__ == "__main__":
    main()
