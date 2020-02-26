#!/usr/bin/python3.7

'''
控制Led
'''

from gpiozero import LED
from time import sleep
from tkinter import *
red = LED(25)

if __name__ == '__main__':
    window = Tk()
    window.title('LED Control')
    window.geometry("300x200")
    window.option_add("*Font",('verdana', 18, 'bold'))
    window.mainloop()