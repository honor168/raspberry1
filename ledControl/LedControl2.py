#!/usr/bin/python3.7

'''
控制Led
'''

from gpiozero import LED
from time import sleep
from tkinter import *


class App:
    def __init__(self,window):
        #建立gpiozero led
        self.red = LED(25)
        print("init")

        #建立window and Layout
        mainFrame = Frame(window, borderwidth=2, relief=GROOVE)
        self.button = Button(mainFrame,text="開燈",command=self.callback)
        self.button.pack(expand=YES, fill=BOTH, padx=40, pady=25)
        mainFrame.pack(expand=YES,fill=BOTH, padx=5, pady=20)

    def callback(self):
        print("Click!")


if __name__ == '__main__':
    window = Tk()
    window.title('LED Control')
    window.geometry("300x200")
    window.option_add("*Font",('verdana', 18))
    app = App(window)
    window.mainloop()