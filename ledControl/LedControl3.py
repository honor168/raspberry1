#!/usr/bin/python3.7

'''
控制Led
'''

from gpiozero import LED
from time import sleep
from tkinter import *
from firebase_admin import db

import firebase_admin
from firebase_admin import credentials

class App:
    def __init__(self,window):
        #建立gpiozero led
        self.red = LED(25)


        #建立window and Layout
        self.buttonName = StringVar()
        mainFrame = Frame(window, borderwidth=2, relief=GROOVE)
        Button(mainFrame,textvariable=self.buttonName,command=self.callback).pack(expand=YES, fill=BOTH, padx=40, pady=25)
        #self.buttonName.set("開燈")
        mainFrame.pack(expand=YES,fill=BOTH, padx=5, pady=20)
        
        #firebase
        # Fetch the service account key JSON file contents
        cred = credentials.Certificate("/home/pi/Documents/iotProject/eric-firebase-test-firebase-adminsdk-4bs2b-9871f102be.json")
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
            


    def callback(self):
        print("Click!")
        try:
            if self.buttonName.get() == '開燈':
                #self.buttonName.set('關燈')
                #self.red.on()
                self.ledNote.set(True)
            else:
                #self.buttonName.set('開燈')
                self.red.off()
                self.ledNote.set(False)
        except:
            print("firebase Error")

    def valueChangeLister(self,event):
        '''
        print(event)
        print(event.data)
        print(event.path)
        print(event.event_type)
        print(self.ledNote.get())
        '''
        if event.data:
            self.red.on()
            self.buttonName.set("關燈")
        else:
            self.red.off()
            self.buttonName.set("開燈")





if __name__ == '__main__':
    window = Tk()
    window.title('LED Control')
    window.geometry("300x200")
    window.option_add("*Font",('verdana', 18))
    app = App(window)
    window.mainloop()