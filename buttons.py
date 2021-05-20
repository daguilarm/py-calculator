from tkinter import Button, W
import operations


# Render  buttons
def render_button(data, frame, text, row, column):

    button = Button(
        frame,
        text=text,
        width=3,
        command=lambda: enter_data(data, text)
    )

    button.grid(row=row, column=column)

    return button


# Render de 0 button. Because has double size
def render_button_zero(data, frame):

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

    # For numeric values
    if value.isnumeric():
        # If there is an on going operation
        if operations.operation != '':
            data.set(value)
            operations.operation = ''

        # There is no on going operation
        else:
            data.set(data.get() + value)

    # For operation values
    else:
        if value == '+':
            operations.operation = 'sum'
