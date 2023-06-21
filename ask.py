# Imports
import interface

# Initializers


# Ask for delimiter
def get_delimiter():
    print(interface.split_select)
    print(interface.menu_delimiter)
    choice = int(input(interface.ask_option))
    if choice == 1:
        return ' '
    elif choice == 2:
        return input(interface.ask_delimiter)
    else:
        raise ValueError('Invalid Choice')


# Ask for input
def get_string():
    print(interface.split_input)
    return input(interface.ask_input)
