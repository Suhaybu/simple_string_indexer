# This files purpose is to handle the more technical stuff

import os


# Indexing method
def index_string(input_string, delimiter):
    # Splitting the string and adding index
    modified_list = [f'[{index}]{word}' for index, word in enumerate(input_string.split(delimiter))]
    # Joining words into one string again
    output = delimiter.join(modified_list)
    return output


# Search methods
def find_index(input_string, word):
    return input_string.index(word)


def find_word(input_string, index):
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


# Line length formatter to insure no line contains characters longer than 75
def length_formatter():
    ...
