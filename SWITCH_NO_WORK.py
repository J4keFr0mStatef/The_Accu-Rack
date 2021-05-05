from gpiozero import LED, Button
from time import sleep

switch = Button(4)

while True:
    if switch.is_pressed:
        print("pressed")
    else:
        print("not pressed")

