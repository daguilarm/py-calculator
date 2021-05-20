from tkinter import Button, W


# Render the buttons
def render_button(data, frame, text, row, column):

    button = Button(
        frame,
        text=text,
        width=3,
        command=lambda: enter_data(data, text)
    )

    button.grid(row=row, column=column)

    return button


def render_button_0(data, frame):

    button = Button(
        frame,
        text='0',
        width=10,
        command=lambda: enter_data(data, '0'),
    )

    button.grid(row=5, column=0, columnspan=2, sticky=W)

    return button

# Enter data
def enter_data(data, value):
    initial_data = data.get()
    data.set(initial_data + value)
