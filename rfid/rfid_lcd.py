from LCD.lcd_display import lcd
import RPi.GPIO as GPIO
import mfrc522 as MFRC522
from tkinter import *
import sys


def on_closing():
    print("ctrl+c captured, ending read.")
    GPIO.cleanup()
    sys.exit(0)


class App():
    def __init__(self, window):

        # init lcd
        self.my_lcd = lcd()

        # init Rfid
        self.MIFAREReader = MFRC522.MFRC522()
        self.rfidHandler()

    def rfidHandler(self):
        (status, TagType) = self.MIFAREReader.MFRC522_Request(self.MIFAREReader.PICC_REQIDL)
        if status == self.MIFAREReader.MI_OK:
            print("status success")
            self.my_lcd.display_string("status success", 1)
            self.my_lcd.display_string("..........", 2)
        else:
            self.my_lcd.display_string("Put On Card", 1)
            self.my_lcd.display_string("..........", 2)


if __name__ == "__main__":
    GPIO.setwarnings(False);
    root = Tk()
    root.title("RFID_LCD")
    root.protocol("WM_DELETE_WINDOW", on_closing)
    app = App(root);
    root.mainloop();