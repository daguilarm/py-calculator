from buttons import render_button, render_button_0


# Set the keyboard
def render_keyboard(data, frame):
    # Set the list of buttons
    buttons = ['AC', '+/-', '%', '/', '7', '8', '9', 'x', '4', '5', '6', '-', '1', '2', '3', '+', '0', ',', '=']

    # Init values for rows and columns
    row = 1
    column = 0
    max_columns = 3

    # Render all the buttons from the list
    for button in buttons:

        # Render 0 the button
        if button == '0':
            render_button_0(data, frame)
            # The 0 button use 2 columns so...
            column += 1

        # Render the button
        else:
            render_button(data, frame, button, row, column)

        # New column
        if column < max_columns:
            column += 1

        # Reset column and start a new row
        else:
            # Reset the column
            column = 0
            # And start the new row
            row += 1
