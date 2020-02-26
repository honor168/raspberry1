from gpiozero import Button,RGBLED
import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

def rgbListener(event):

    print(event.event_type)
    eventType = event.event_type;

    data = event.data
    if event.path == "/" and eventType == "put":
        r = data['R']
        g = data['G']
        b = data['B']
        rgbLed.color = (r/100, g/100, b/100)
    elif event.path == "/R" and eventType == "put":
        rgbLed.red = data/100
    elif event.path == "/G" and eventType == "put":
        rgbLed.green = data / 100
    elif event.path == "/B" and eventType == "put":
        rgbLed.blue = data/100

    elif event.path == "/" and eventType == "patch":
        #web change message
        print("patch")
        print(event.path)
        for key, value in data.items():
            if key == "R":
                rgbLed.red = value/100
            elif key == "G":
                rgbLed.green = value/100
            elif key == "B":
                rgbLed.blue = value/100




if __name__ == "__main__":
    cred = credentials.Certificate("/home/pi/Documents/iotProject/eric-firebase-test-firebase-adminsdk-4bs2b-9871f102be.json")
    firebase_admin.initialize_app(cred,{'databaseURL':'https://eric-firebase-test.firebaseio.com/'})
    rgb = db.reference('iot20191126/RGBLed')
    button = Button(18)
    rgbLed = RGBLED(17,27,22)
    rgb.listen(rgbListener)