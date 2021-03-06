'''
THIS FILE OF CODE SERVES TO ACT AS A TESTING GROUND FOR GETTING THE GPIO READY
AND IN A FUNCTIONAL STATE.  IT IS NOT INCLUDED IN THE MAIN PART OF THE CODE
WHATSOEVER.  

THE METHODS USED HERE ARE NOT EXAMPLES OF WHAT THE GPIO IN THE CODE LOOKS
LIKE
'''

import RPi.GPIO as GPIO
from time import delay

def setupGPIO():
    coats = {"umbrella": 4, "raincoat": 25, "light coat": 24, "heavy coat": 5}
    leds = {"umbrella": 17, "raincoat": 16, "light coat": 13, "heavy coat": 12}

    GPIO.setmode(GPIO.BCM)
    # setup the GPIO for the limit switches
    GPIO.setup(coats["umbrella"], GPIO.IN, pull_up_down = GPIO.PUD_DOWN)
    GPIO.setup(coats["raincoat"], GPIO.IN, pull_up_down = GPIO.PUD_DOWN)
    GPIO.setup(coats["light coat"], GPIO.IN, pull_up_down = GPIO.PUD_DOWN)
    GPIO.setup(coats["heavy coat"], GPIO.IN, pull_up_down = GPIO.PUD_DOWN)
    # setup the GPIO for the LEDs
    GPIO.setup(leds["umbrella"], GPIO.OUT)
    GPIO.setup(leds["raincoat"], GPIO.OUT)
    GPIO.setup(leds["light coat"], GPIO.OUT)
    GPIO.setup(leds["heavy coat"], GPIO.OUT)

    return coats, leds

def blink(led):
    GPIO.output(led, GPIO.HIGH)
    delay(0.3)
    GPIO.output(led, GPIO.LOW)
    delay(0.3)

def recommend(coat):
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

# forever loop might be an issue
while True:
    if (GPIO.input(coats["umbrella"] == GPIO.HIGH):
        # do this if umbrella is on switch 1
        pass

    if (GPIO.input(coats["raincoat"] == GPIO.HIGH):
        # do this if umbrella is on switch 2
        pass

    if (GPIO.input(coats["light coat"] == GPIO.HIGH):
        # do this if umbrella is on switch 3
        pass

    if (GPIO.input(coats["heavy coat"] == GPIO.HIGH):
        # do this if umbrella is on switch 4
        pass
