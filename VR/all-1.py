#!/usr/bin/python3.7
'''
MCP3008 , 可變電阻, pwmLed
'''
from gpiozero import RGBLED
from gpiozero import MCP3008
from tkinter import *
from threading import Timer
from gpiozero import PWMLED, LED
import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
from gpiozero import Button as btn

channel0 = MCP3008(0)
led = PWMLED(25)
ledGreen = LED(20)
rgbLed = RGBLED (17,27,22)
button = btn(18)

class App():
    def __init__(self,win):
        #firebase realtimedataBase_PWM
        self.master = win
        self.job = None
        self.outputValue = 0
        cred = credentials.Certificate('/home/pi/Documents/iotProject/eric-firebase-test-firebase-adminsdk-4bs2b-9871f102be.json')
        firebase_admin.initialize_app(cred, {
            'databaseURL': 'https://eric-firebase-test.firebaseio.com/'
        })
        self.ledNote = db.reference('/iot20191126/ledState')
        #print(self.ledNote.get())
        #register listen self.ledNote changeEvent
        try:
            self.ledNote.listen(self.valueChangeLister)
        except  FirebaseError:
            print("listen Error")
        rgb = db.reference('/iot20191126/RGBLed')
        
        rgb.listen(self.rgbListener)    
        self.pwmRef = db.reference('/iot20191126/PWM')
        print(self.pwmRef)
        #tkinter
        self.displayValue = IntVar()
        mainFrame = Frame(win,borderwidth=2,relief=GROOVE)
        displayBar = Scale(mainFrame, from_=0, to=100, orient=HORIZONTAL, variable=self.displayValue,length=300)
        displayBar.pack()
        mainFrame.pack()
        self.displayValue.set(50)
        self.auotUpdate()
        
    def valueChangeLister(self,event):
        '''
        print(event)
        print(event.data)
        print(event.path)
        print(event.event_type)
        print(self.ledNote.get())
        '''
        #print("valueChangeLister")
        if event.data:
            ledGreen.on()
            print("關燈")
        else:
            ledGreen.off()
            print("開燈")
            
            
            
    def rgbListener(self, event):
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
            

        
    def userCreateJob(self):
        print("userCreateJob")
        if self.job:
            self.master.after_cancel(self.job);        
        self.job = self.master.after(100,self.firebaseDoSomeThing)
    
    def firebaseDoSomeThing(self):
        print('doSomethine')
        self.pwmRef.update({'value':self.displayValue.get()})

    def auotUpdate(self):
        #print('update')
        #
        if button.is_pressed:
            if (self.ledNote.get() == TRUE):
                self.ledNote.set(False)
            else:
                self.ledNote.set(True)
        
            
        outputValue = int(channel0.value * 100)
        if self.outputValue != outputValue:
            self.outputValue = outputValue
            self.userCreateJob()
            
        led.value = channel0.value
        self.displayValue.set(outputValue)
        try:
            Timer(0.2,self.auotUpdate).start()
            #self.pwmRef.update({'value':outputValue})       
            
        except:
            print("error")
            Timer(1, self.auotUpdate).start()

if __name__ == '__main__':
    window = Tk()
    window.title("MCP3008_可變電阻")
    window.option_add("*font",('verdana',18,'bold'))
    window.option_add('*background','#333333')
    window.option_add('*foreground','#ffffff')
    app = App(window)
    window.mainloop()