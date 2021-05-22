from tkinter import *
from keyboard import render as render_keyboard
from screens import render_screen

# Window
root = Tk()
root.title("Mac calculator app with Python")
root.config(background='red')

# Frame
calculator = Frame(root)
calculator.configure(background='#333333')
calculator.pack()

# Default data for the screen
data = StringVar()

# Screens
screen = render_screen(data, calculator)

# Buttons
buttons = render_keyboard(data, calculator)

# Infinity loop for the window
root.mainloop()