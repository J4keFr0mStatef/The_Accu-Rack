from weather_class import *

from gpiozero import LED, Button
from time import sleep as delay

coats = {"umbrella": 4, "raincoat": 25, "light coat": 24, "heavy coat": 5}
leds = {"umbrella": 17, "raincoat": 16, "light coat": 13, "heavy coat": 12}


button1 = Button(coats["umbrella"])
button2 = Button(coats["raincoat"])
button3 = Button(coats["light coat"])
button4 = Button(coats["heavy coat"])

led1 = LED(leds["umbrella"])
led2 = LED(leds["raincoat"])
led3 = LED(leds["light coat"])
led4 = LED(leds["heavy coat"])

def blink(led):
    
    delay(0.3)
    led.on()
    delay(0.3)

def recommend(x=None):
    weatherData = Weather("Auburn")
    if (True):
        weatherData.ping()
        if (weatherData.getRainChance() >= 0.75) and (weatherData.getTemp() >= 32):
            # RAINCOAT & UMBRELLA
            blink(led2)
            blink(led1)
        elif (weatherData.getRainChance() >= 0.6) and (weatherData.getTemp() >= 32):
            # "RAINCOAT"
            blink(led2)
        elif (weatherData.getRainChance() >= 0.3) and (weatherData.getTemp() >= 32):
            # "UMBRELLA"
            blink(led2)
        elif (weatherData.getTemp() <= 35):
            # "HEAVY COAT"
            blink(led4)
        elif (weatherData.getTemp() <= 60):
            # "LIGHT COAT"
            blink(led3)

def letThereBeLight():
    # check to see if coats are on the rack
    if button1.is_pressed:
        led1.on()
        
    if button2.is_pressed:
        led2.on()
        
    if button4.is_pressed:
        led4.on()
        
    if button3.is_pressed:
        led3.on()
    

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
    letThereBeLight()
        
    recommend()
    print(button4.is_pressed)


if __name__ == "__main__":
    main()
