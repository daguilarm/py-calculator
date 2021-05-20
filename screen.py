from tkinter import Entry


# Render the calculator screen
def render_screen(data, frame):

    # Screen generation
    screen = Entry(frame, textvariable=data)
    screen.grid(row=0, column=0, columnspan=4)
    screen.config(background="black", fg="orange", justify="right")

    return screen
