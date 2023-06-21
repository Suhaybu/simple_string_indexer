# Imports
import interface

# Initializers


# Ask for delimiter
def get_delimiter() -> str:
    print(interface.split_option)
    print(interface.menu_delimiter)
    while True:
        try:
            choice = int(input(interface.ask_option))
            if choice == 1:
                return ' '
            elif choice == 2:
                return input(interface.ask_delimiter)
            else:
                print(interface.error_option)
        except ValueError:
            print(interface.error_option)


# Ask for input
def get_string():
    print(interface.split_input)
    return input(interface.ask_input)


def other_options():
    print(interface.split_option)
    print(interface.menu_other_options)
    while True:
        try:
            choice = int(input(interface.ask_option))
            if 1 <= choice <= 4:
                return choice
            else:
                print(interface.error_option)
        except ValueError:
            print(interface.error_option)
