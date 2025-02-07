import threading
import keyboard


# Function to be called when the timer expires
def timer_expired():
    print("Timer expired!")


# Function to reset the timerr
def reset_timer():
    global timer
    if timer is not None:
        timer.cancel()
    timer = threading.Timer(5.0, timer_expired)  # Set timer for 5 seconds

    timer.start()
    # print("Timer reset!")


# Initialize the timer
timer = None

reset_timer()

# Set up the key press event listener
keyboard.on_press(lambda _: reset_timer())

# Keep the script running
keyboard.wait('esc')  # Press 'esc' to exit the script
from tkinter import *
def keyup(e):
    print( 'up', e.char)
def keydown(e):
    print( 'down', e.char)

root = Tk()
frame = Frame(root, width=100, height=100)
frame.bind("<KeyPress>", keydown)
frame.bind("<KeyRelease>", keyup)
frame.pack()
frame.focus_set()
root.mainloop()