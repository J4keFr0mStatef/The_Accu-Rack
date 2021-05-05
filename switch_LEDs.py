from weather_class import *

import RPi.GPIO as GPIO
from time import sleep as delay

coats = {"umbrella": 4, "raincoat": 25, "light coat": 24, "heavy coat": 5}
leds = {"umbrella": 17, "raincoat": 16, "light coat": 13, "heavy coat": 12}

def setupGPIO():
    global coats, leds

    GPIO.setmode(GPIO.BCM)
    GPIO.setwarnings(False)
    # setup the GPIO for the limit switches
    for coat in coats:
        GPIO.setup(coats[coat], GPIO.IN, pull_up_down = GPIO.PUD_DOWN)
    # setup the GPIO for the LEDs
    for led in leds:
        GPIO.setup(leds[led], GPIO.OUT)
    
    letThereBeLight()

def blink(led):
    GPIO.output(led, GPIO.LOW)
    delay(0.3)
    GPIO.output(led, GPIO.HIGH)
    delay(0.3)

def recommend(x=None):
    weatherData = Weather("Auburn")
    if (True):
        weatherData.ping()
        if (weatherData.getRainChance() >= 0.75) and (weatherData.getTemp() >= 32):
            # RAINCOAT & UMBRELLA
            blink(leds["raincoat"])
            blink(leds["umbrella"])
        elif (weatherData.getRainChance() >= 0.6) and (weatherData.getTemp() >= 32):
            # "RAINCOAT"
            blink(leds["raincoat"])
        elif (weatherData.getRainChance() >= 0.3) and (weatherData.getTemp() >= 32):
            # "UMBRELLA"
            blink(leds["umbrella"])
        elif (weatherData.getTemp() <= 35):
            # "HEAVY COAT"
            blink(leds["heavy coat"])
        elif (weatherData.getTemp() <= 60):
            # "LIGHT COAT"
            blink(leds["light coat"])

def letThereBeLight():
    # check to see if coats are on the rack
    if (GPIO.input(coats["umbrella"]) == GPIO.HIGH):
        GPIO.output(leds["umbrella"], GPIO.HIGH)
        
    if (GPIO.input(coats["raincoat"]) == GPIO.HIGH):
        GPIO.output(leds["raincoat"], GPIO.HIGH)
        
    if (GPIO.input(coats["heavy coat"]) == GPIO.HIGH):
        GPIO.output(leds["heavy coat"], GPIO.HIGH)
        
    if (GPIO.input(coats["light coat"]) == GPIO.HIGH):
        GPIO.output(leds["light coat"], GPIO.HIGH)
    

### forever loop might be an issue
##while True:
##    if (GPIO.input(coats["umbrella"] == GPIO.HIGH):
##        # do this if umbrella is on switch 1
##        pass
##
##    if (GPIO.input(coats["raincoat"] == GPIO.HIGH):
##        # do this if umbrella is on switch 2
##        pass
##
##    if (GPIO.input(coats["light coat"] == GPIO.HIGH):
##        # do this if umbrella is on switch 3
##        pass
##
##    if (GPIO.input(coats["heavy coat"] == GPIO.HIGH):
##        # do this if umbrella is on switch 4
##        pass

def main():
    setupGPIO()
    letThereBeLight()
        
    recommend()

    print(GPIO.input(coats["heavy coat"]))
    
    GPIO.add_event_detect(coats["umbrella"], GPIO.FALLING, callback=recommend)
    GPIO.add_event_detect(coats["raincoat"], GPIO.FALLING, callback=recommend)
    GPIO.add_event_detect(coats["light coat"], GPIO.FALLING, callback=recommend)
    GPIO.add_event_detect(coats["heavy coat"], GPIO.FALLING, callback=recommend)

##    GPIO.add_event_callback(coats["umbrella"], recommend(leds, True))
##    GPIO.add_event_callback(coats["raincoat"], recommend(leds, True))
##    GPIO.add_event_callback(coats["light coat"], recommend(leds, True))
##    GPIO.add_event_callback(coats["heavy coat"], recommend(leds, True))


if __name__ == "__main__":
    main()
