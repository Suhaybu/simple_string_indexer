# This file's purpose is to handle the more technical backend stuff

import interface
import os
from colorama import Fore


# Indexing method:
def index_string(input_string, delimiter):
    # Splitting the string and adding index and coloring it
    modified_list = [
        f'{Fore.LIGHTBLACK_EX}[{Fore.LIGHTBLUE_EX}{index}{Fore.LIGHTBLACK_EX}]{Fore.RESET}{word}'
        for index, word in enumerate(input_string.split(delimiter))
    ]
    # Joining words into one string again
    output = delimiter.join(modified_list)
    return output


# Search methods:
# Takes user input and word to return index of word
def get_index(input_string, word):
    print(interface.splitter('return index'))
    try:
        # Converts integer inputs to string
        if isinstance(word, str):
            return input_string.index(word)
        elif isinstance(word, int):
            return input_string.index(str(word))
    except ValueError:
        return 'Word not found'


# Takes user input and index to return word @ index
def get_word(input_string, index):
    print(interface.splitter('return word'))
    # Splits the user input string into seperate words stored in a list
    words = input_string.split()
    # Ensures input index is int
    index = int(index)
    # Ensures index is within range
    if 0 <= index < len(words):
        return words[index]
    else:
        return 'Index out of range'


# Clears terminal screen with respect to OS
def clear_terminal():
    # Need to identify OS
    if os.name == 'nt':  # Windows
        os.system('cls')
    else:  # Unix/Linux/MacOS
        os.system('clear')


# TODO Line length formatter to insure no line contains characters longer than 75
def length_formatter():
    ...
