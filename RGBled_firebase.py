from gpiozero import Button,RGBLED
import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

def rgbListener(event):
    print(event.data)

    if event.path == "/":
        print('rgb')
    elif event.path == "/R":
        print('r change')
    elif event.path == "/G":
        print("g change")
    elif event.path == "/B":
        print("b change")

if __name__ == "__main__":
    cred = credentials.Certificate("/home/pi/Documents/iotProject/eric-firebase-test-firebase-adminsdk-4bs2b-9871f102be.json")
    firebase_admin.initialize_app(cred,{'databaseURL':'https://eric-firebase-test.firebaseio.com/'})
    rgb = db.reference('iot20191126/RGBLed')
    rgb.listen(rgbListener)
    button = Button(18)
    rgbLed = RGBLED(17,27,22)

    while True:
        if button.is_pressed:
            rgbLed.color = (1, 0, 0)

        else:
            rgbLed.color = (0, 1, 0)