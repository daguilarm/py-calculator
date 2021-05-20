from tkinter import Button, W


# Default variables
operation = ''
results = 0


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

    global operation, results

    # For numeric values
    if value.isnumeric():

        # If there is an on going operation
        if operation != '':
            data.set(value)
            operation = ''

        # There is no on going operation
        else:
            data.set(data.get() + value)

    # For operation values
    else:
        # Just doing this for not empty variable
        operation = 'on-going-operation'

        # Sum operation
        if value == '+':
            # Add value to chain of values
            results += int(data.get())

        # Show values on screen
        data.set(results)