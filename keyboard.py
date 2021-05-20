from buttons import render_button


# Set the keyboard
def render_keyboard(calculator, data):

    # Set the list of buttons
    buttons = ['AC', '+/-', '%', '/', '7', '8', '9', 'x', '4', '5', '6', '-', '1', '2', '3', '+', '0', ',', '=']

    # Init values for rows and columns
    row = 2
    column = 1
    max_columns = 4

    # Render all the buttons from the list
    for button in buttons:

        # Render the button
        render_button(calculator, button, row, column, data)

        # New column
        if column < max_columns:
            column = column + 1

        # Reset column and start a new row
        else:
            # Reset the column
            column = 1
            # And start the new row
            row = row + 1