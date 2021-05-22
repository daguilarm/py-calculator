from tkinter import Entry


# Render the calculator screen
def render_screen(data, frame):
    # Main screen
    screen = Entry(frame, textvariable=data, highlightbackground="#333333", highlightthickness=2, bd=0)
    screen.grid(row=0, column=0, columnspan=4, ipady=14)
    screen.config(background="#333333", fg="#ececec", justify="right", font=("Verdana", 18))
    screen.insert(0, "0")

    return screen


# Render the calculator screen
def render_operations(operation, frame):
    # Main screen
    screen_operation = Entry(frame, textvariable=operation)
    screen_operation.grid(row=1, column=0, columnspan=4)
    screen_operation.config(background="#333333", fg="#ececec", justify="right", font=("Verdana", 12))

    return screen_operation
