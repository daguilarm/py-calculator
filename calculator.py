from tkinter import *
from keyboard import render as render_keyboard
from screen import render as render_screen

# Window
root = Tk()
root.title("Mac calculator app with Python")

# Frame
calculator = Frame(root)
calculator.configure(background='black')
calculator.pack()

# Screen
# Default data to be show in the screen
data = StringVar()
# Render the screen with the default data
screen = render_screen(data, calculator)

# Buttons
buttons = render_keyboard(data, calculator)

# Infinity loop for the window
root.mainloop()
