from tkinter import Entry


# Render the calculator screen
def render(data, frame):
    # Screen generation
    screen = Entry(frame, textvariable=data, highlightbackground="black", highlightthickness=2, bd=0)
    screen.grid(row=0, column=0, columnspan=4, ipady=10)
    screen.config(background="black", fg="orange", justify="right", font=("Verdana", 18))

    return screen
