from tkinter import Tk
from tkinter import Label
import time
import sys

# Create UI
master = Tk()
master.title("DigitalClock")

# Define function to get time in correct format and refresh clocks every 200ms
def get_time():
    timeVar = time.strftime("%I:%M:%S")
    clock.config(text=timeVar)
    clock.after(200,get_time)

# Create clock object with font and colors
clock = Label(master, font=("Arial",90),bg="black",fg="white")
clock.pack()

# Call get_time
get_time()

# Start UI
master.mainloop()
