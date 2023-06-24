# Imports
from discord import option
import interface


# Ask for delimiter
def get_delimiter() -> str:
    print(interface.splitter('select'))  # Prints the splitter for select option
    print(interface.menu('delimiter'))  # Prints delimiter menu
    # Catches invalid input
    while True:
        try:
            choice = int(input(interface.enter('choice')))  # Prompts the user for choice
            if choice == 1:
                return ' '
            elif choice == 2:
                return input(interface.enter('delimiter'))
            else:
                print(interface.error('invalid choice'))
                print(interface.menu('delimiter'))
        except ValueError:
            print(interface.error('invalid choice'))
            print(interface.menu('delimiter'))


# Asks the user for input
def get_string():
    print(interface.splitter('user input'))
    return input(interface.enter('input'))


# Asks the user for other options
def other_options():
    print(interface.splitter('select'))  # Prints the splitter for select option
    print(interface.menu('other options'))
    while True:
        try:
            choice = int(input(interface.enter('choice')))
            if 1 <= choice <= 4:
                if choice == 1:
                    return 'find index'
                elif choice == 2:
                    return 'find word'
                elif choice == 3:
                    return 'input'
                # TODO
                elif choice == 4:
                    return 'exit'
            else:
                print(interface.error('invalid choice'))
                print(interface.menu('other options'))
        except ValueError:
            print(interface.error('invalid choice'))
            print(interface.menu('other options'))
