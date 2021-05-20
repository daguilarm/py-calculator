from tkinter import Button


# Render the buttons
def render_button(frame, text, row, column, data):
    button = Button(
        frame,
        text=text,
        width=3,
        command=lambda: enter_data(data, text)
    )

    button.grid(row=row, column=column)

    return button


# Enter data
def enter_data(data, value):
    initial_data = data.get()
    data.set(initial_data + value)
