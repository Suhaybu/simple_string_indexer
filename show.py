from magic import clear_terminal, index_string
import interface
from interface import menu_delimiter
from colorama import Style

input_string = ''


# Print method
def get_output(input_string, delimiter):
    # Prepares the terminal for new output interface
    print(interface.split_result)
    print(index_string(input_string, delimiter))


# Selector styler
selected_choice = 1
if selected_choice == 1:
    menu_delimiter = menu_delimiter.replace(f'{selected_choice}.', f'{Style.BRIGHT}{selected_choice}.')
    menu_delimiter = menu_delimiter.replace(f'{selected_choice+1}.', f'{Style.DIM}{selected_choice}.')
elif selected_choice == 2:
    menu_delimiter = menu_delimiter.replace(f'{selected_choice}.', f'{Style.BRIGHT}{selected_choice}.')
    menu_delimiter = menu_delimiter.replace(f'{selected_choice+1}.', f'{Style.DIM}{selected_choice}.')
else:
    print('Error!')
