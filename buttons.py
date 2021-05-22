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
    operation += value.replace('x', '*').replace('+/-', '*(-1)')

    # Return the results
    if value == '=':

        resolve_operation(data)
        operation = data.get()

    # Reset the results
    elif value == 'AC':

        operation = ''
        data.set('0')
        isInputNumeric = False

    # Change positive or negative
    elif value == '+/-':
        # Avoid operation to resolve the string *(-1)
        # when reset the value with AC
        if not operation == '*(-1)':
            data.set(eval(operation))

        else:
            operation = ''

    # Float number
    elif value == '.':
        # If there is no number to float...
        if data.get().count('.') <= 0:
            data.set(data.get() + value)

        # If the number is already float, delete the point
        if operation.count('.') > 1:
            operation = operation[:-1]

    # Percent
    elif value == '%':

        # Removed % symbol and divide the value
        percent = operation[:-1].split('*')

        # Calculate full percent
        if len(percent) == 2:
            operation = '100 * {} / {}'.format(percent[0], percent[1])

        # Calculate partial percent
        else:
            operation = '{} / 100'.format(percent[0])

        data.set(eval(operation))

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
        # Fixed number with left 0
        new_value = (data.get() + value).lstrip('0')
        # Set the value
        data.set(new_value)

    # If the previous value is a symbol / operation
    else:
        data.set(value)

    # Set the value as numeric
    isInputNumeric = True


# Resolve operation
def resolve_operation(data):
    global operation

    filter_operation = operation[:-1]

    # Get the value
    if len(filter_operation) > 0:
        value = eval(filter_operation)
    else:
        value = 0

    # Resolve the operation value in memory
    data.set(value);
