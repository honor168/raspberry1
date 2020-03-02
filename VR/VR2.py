#!/usr/bin/python3.7
'''
MCP3008 ,可變電阻
'''

from gpiozero import MCP3008
from tkinter import *
from threading import Timer
from gpiozero import PWMLED


channel0 = MCP3008(0)
led = PWMLED(25)

class App():
    def __init__(self,win):
        #tkinter
        self.displayValue = IntVar()
        mainFrame = Frame(win,borderwidth=2,relief=GROOVE)
        displayBar = Scale(mainFrame, from_=0, to=100, orient=HORIZONTAL, variable=self.displayValue,state=DISABLED,length=300)
        displayBar.pack()
        mainFrame.pack()
        self.displayValue.set(50)
        self.auotUpdate()

    def auotUpdate(self):
        print('update')
        outputValue = int(channel0.value * 100)
        led.value = channel0.value
        self.displayValue.set(outputValue)
        try:
            Timer(0.2,self.auotUpdate).start()
        except:
            print("error")
            Timer(0.2, self.auotUpdate).start()

if __name__ == '__main__':
    window = Tk()
    window.title("MCP3008_可變電阻")
    window.option_add("*font",('verdana',18,'bold'))
    window.option_add('*background','#333333')
    window.option_add('*foreground','#ffffff')
    app = App(window)
    window.mainloop()