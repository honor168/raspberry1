from LCD.lcd_display import lcd
import RPi.GPIO as GPIO
import mfrc522 as MFRC522
from tkinter import *
import sys

my_lcd = lcd()
my_lcd.display_string("Raspberry Pi", 1)
my_lcd.display_string("Hello", 2)


class App():
    def __init__(self, window):
        print('app init')


def on_closing():
    print("ctrl+c captured, ending read.")
    GPIO.cleanup()
    sys.exit(0)


if __name__ == "__main__":
    GPIO.setwarnings(False);
    root = Tk()
    root.title("RFID_LCD")
    root.protocol("WM_DELETE_WINDOW", on_closing)
    app = App(root);
    root.mainloop();