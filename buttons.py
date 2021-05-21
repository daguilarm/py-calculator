from tkinter import Button, W


# Default variables
operation = ''
isInputNumeric = False


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

    global operation, isInputNumeric

    # Update the operation
    operation += value

    # For results
    if value == '=':

        data.set(eval(operation[:-1]))
        operation = data.get()

    # For numeric values
    elif value.isnumeric():

        # If the previous value was number
        if isInputNumeric:
            data.set(data.get() + value)

        # If the previous value was a symbol
        else:
            data.set(value)

        # Set the value as numeric
        isInputNumeric = True

    # For operation values, show the current result
    else:
        data.set(eval(operation[:-1]))

        # Set the value as symbol
        isInputNumeric = False