from gpiozero import Button,RGBLED
import time

button = Button(18)
rgbLed = RGBLED(17,27,22)
rgbLed.color = (1, 0, 0)


ledState = 1

def changeLedState():
    global ledState
    ledState = ledState +1
    if (ledState ==0 ):
        rgbLed.color = (0, 0, 0)
    elif (ledState ==1 ):
        rgbLed.color = (1, 0, 0)
    elif (ledState ==2 ):
        rgbLed.color = (0, 1, 0)
    elif (ledState ==3 ):
        rgbLed.color = (0, 0, 1)
        ledState = 0
    else:
        rgbLed.color = (1, 1, 1)


while True:
    if button.is_pressed:
        print("Button is pressed")
        changeLedState()
        time.sleep (0.2)
        while button.is_pressed:
            pass
        
        #rgbLed.color = (1, 0, 0)
    else:
        print("Button is not pressed")
        #rgbLed.color = (0, 1, 0)
