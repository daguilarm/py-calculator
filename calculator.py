from tkinter import *
from keyboard import render as render_keyboard

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
screen = Entry(calculator, textvariable=data, highlightbackground="#333333", highlightthickness=2, bd=0)
screen.grid(row=0, column=0, columnspan=4, ipady=14)
screen.config(background='#333333', fg='#ececec', justify='right', font=('Verdana', 18))
screen.insert(0, '0')

# Buttons
buttons = render_keyboard(data, calculator)

# Infinity loop for the window
root.mainloop()