from gpiozero import Button,RGBLED

button = Button(18)
rgbLed = RGBLED(17,27,22)
rgbLed.color = (1, 0, 0)
while True:
    if button.is_pressed:
        print("Button is pressed")
        rgbLed.color = (1, 0, 0)
    else:
        print("Button is not pressed")
        rgbLed.color = (0, 1, 0)
