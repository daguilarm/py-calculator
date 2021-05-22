from tkinter import Button, W, StringVar

# Default variables
operation: str = ''
isInputNumeric: bool = False


# Render numeric  buttons
def render_button(data, frame, text, row, column):

    button = Button(
        frame,
        text=text,
        width=3,
        height=3,
        command=lambda: enter_data(data, text)
    )

    button.grid(row=row, column=column, padx=0, pady=0)

    return button


# Render de 0 button. Because has double size
def render_button_zero(data, frame):

    button = Button(
        frame,
        text='0',
        width=10,
        height=3,
        command=lambda: enter_data(data, '0'),
    )

    button.grid(row=5, column=0, columnspan=2, sticky=W, padx=0, pady=0)

    return button


# Enter data
def enter_data(data, value):

    global operation, isInputNumeric

    # Update the operation
    operation += value.replace('x', '*')

    # Return the results
    if value == '=':

        resolve_operation(data)
        operation = data.get()

    # Return the results
    elif value == 'AC':

        operation = ''
        data.set('0')

    # For numeric values
    elif value.isnumeric():

        # Resolve for numeric values
        resolve_numeric(data, value)

    # For operation values, show the current result
    else:
        resolve_operation(data)

        # Set the value as symbol
        isInputNumeric = False


# Resolve numeric
def resolve_numeric(data, value):

    global isInputNumeric

    # If the previous value is a number
    if isInputNumeric:
        data.set(data.get() + value)

    # If the previous value is a symbol / operation
    else:
        data.set(value)

    # Set the value as numeric
    isInputNumeric = True


# Resolve operation
def resolve_operation(data):
    global operation

    # Get the value
    value = eval(operation[:-1])

    # Resolve the operation value in memory
    data.set(value);