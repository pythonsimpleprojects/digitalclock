from tkinter import Tk
from tkinter import Label
import time
import sys

# Create UI
master = Tk()
master.title("DigitalClock")

def get_time():
    timeVar = time.strftime("%I:%M:%S")
    clock.config(text=timeVar)
    clock.after(200,get_time)


clock = Label(master, font=("Arial",90),bg="black",fg="white")
clock.pack()

get_time()

master.mainloop()
