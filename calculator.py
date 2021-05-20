from tkinter import *
from screen import render_screen
from keyboard import render_keyboard


# Window
root = Tk()
root.title("Mac calculator app with Python")

# Frame
calculator = Frame(root)
calculator.pack()

# Screen
data = StringVar()
screen = render_screen(data, calculator)

# Buttons
buttons = render_keyboard(data, calculator)

# Infinity loop
root.mainloop()
