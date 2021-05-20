from tkinter import *
from screen import render_screen
from buttons import render_button


# Init window
root = Tk()
root.title("Mac calculator app with Python")

# Frame
calculator = Frame(root)
calculator.pack()

# Screen
data = StringVar()
screen = render_screen(data, calculator)

# Buttons from first line
buttonAc = render_button(calculator, 'AC', 2, 1, data)
buttonPlusMinus = render_button(calculator, '+/-', 2, 2, data)
buttonPercent = render_button(calculator, '%', 2, 3, data)
buttonDivide = render_button(calculator, '/', 2, 4, data)

# Buttons from second line
button7 = render_button(calculator, '7', 3, 1, data)
button8 = render_button(calculator, '8', 3, 2, data)
button9 = render_button(calculator, '9', 3, 3, data)
buttonMultiple = render_button(calculator, 'x', 3, 4, data)

# Buttons from third line
button4 = render_button(calculator, '4', 4, 1, data)
button5 = render_button(calculator, '5', 4, 2, data)
button6 = render_button(calculator, '6', 4, 3, data)
buttonMinus = render_button(calculator, '-', 4, 4, data)

# Buttons from fourth line
button1 = render_button(calculator, '4', 4, 1, data)
button2 = render_button(calculator, '5', 4, 2, data)
button3 = render_button(calculator, '6', 4, 3, data)
buttonPlus = render_button(calculator, '+', 4, 4, data)

# Buttons from fifth line
button0 = render_button(calculator, '0', 5, 1, data)
buttonComma = render_button(calculator, ',', 5, 2, data)
buttonEqual = render_button(calculator, '=', 5, 3, data)

# Infinity loop
root.mainloop()
