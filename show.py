import magic
import interface
from magic import clear_terminal
from interface import menu
from colorama import Style

input_string = ''


# Print method
def get_output(input_string, delimiter):
    # Prepares the terminal for new output interface
    print(interface.splitter('result'))
    print(magic.index_string(input_string, delimiter))


def get_other_option(input_string, choice, delimiter):
    # Replace choice number with appropriate string
    print(interface.splitter(choice))
    data = input(interface.enter(choice))
    if choice == 'find index':
        print(magic.get_index(input_string, data, delimiter))
    elif choice == 'find word':
        print(magic.get_word(input_string, data, delimiter))


# TODO: Selector styler
menu_delimiter = menu('delimiter')
selected_choice = 1
if selected_choice == 1:
    menu_delimiter = menu_delimiter.replace(f'{selected_choice}.', f'{Style.BRIGHT}{selected_choice}.')
    menu_delimiter = menu_delimiter.replace(f'{selected_choice+1}.', f'{Style.DIM}{selected_choice}.')
elif selected_choice == 2:
    menu_delimiter = menu_delimiter.replace(f'{selected_choice}.', f'{Style.BRIGHT}{selected_choice}.')
    menu_delimiter = menu_delimiter.replace(f'{selected_choice+1}.', f'{Style.DIM}{selected_choice}.')
else:
    print('Error!')
