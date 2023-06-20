# This files purpose is to handle the more technical stuff

import os


# Indexing method
def index_string(input_string):
    # Splitting the string and adding index
    modified_list = [f'[{index}]{word}' for index, word in enumerate(input_string.split())]
    # Joining words into one string again
    output = ' '.join(modified_list)
    return output


# Clear terminal screen
def clear_terminal():
    # Need to identify OS
    if os.name == 'nt':  # Windows
        os.system('cls')
    else:  # Unix/Linux/MacOS
        os.system('clear')


# Line length formatter to insure no line contains characters longer than 75
def length_formatter():
    ...
