# This files purpose is to handle the more technical stuff

import interface
import os
from colorama import Fore


# Indexing method
def index_string(input_string, delimiter):
    # Splitting the string and adding index
    modified_list = [
        f'{Fore.LIGHTBLACK_EX}[{Fore.LIGHTBLUE_EX}{index}{Fore.LIGHTBLACK_EX}]{Fore.RESET}{word}'
        for index, word in enumerate(input_string.split(delimiter))
    ]
    # Joining words into one string again
    output = delimiter.join(modified_list)
    return output


# Search methods
def find_index(input_string, word):
    print(interface.splitter('return index'))
    try:
        # Converts integer inputs to string
        if isinstance(word, str):
            return input_string.index(word)
        elif isinstance(word, int):
            return input_string.index(str(word))
    except ValueError:
        return 'Word not found'


def find_word(input_string, index):
    print(interface.splitter('return word'))
    if index < len(input_string):
        return input_string[index]
    else:
        return 'Index out of range'


# Clear terminal screen
def clear_terminal():
    # Need to identify OS
    if os.name == 'nt':  # Windows
        os.system('cls')
    else:  # Unix/Linux/MacOS
        os.system('clear')


# TODO Line length formatter to insure no line contains characters longer than 75
def length_formatter():
    ...
