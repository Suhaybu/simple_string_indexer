"""
This file contains most of the logical operations and calculations
"""

import os

from colorama import Fore

from . import interface


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
def get_index(input_string, word, delimiter):
	print(interface.splitter('return index'))
	# Splits the user input string into separate words stored in a list
	words = input_string.split(delimiter)
	try:
		# Converts integer inputs to string
		if isinstance(word, str):
			return words.index(word)
		elif isinstance(word, int):
			return words.index(str(word))
	except ValueError:
		return 'Word not found'


# Takes user input and index to return word @ index
def get_word(input_string, index, delimiter):
	print(interface.splitter('return word'))
	# Splits the user input string into separate words stored in a list
	words = input_string.split(delimiter)
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


# Line length formatter to insure no line contains characters longer than 75
def length_formatter(input_string, delimiter):
	words = input_string.split(
		delimiter
	)  # Extracts the individual words from the string
	line_counter = 0

	for index in range(len(words)):
		line_counter += len(words[index]) + len(
			delimiter
		)  # Adds the word length plus delimiter
		if line_counter > 75:  # If line + delimiter is longer than 75
			check_counter = line_counter - len(
				delimiter
			)  # Check if without delimiter, it's still > 75
			if check_counter > 75:  # If it is still larger than 75 without delimiter
				words[index] = '\n' + words[index]  # Add '\n' to the current word
				line_counter = len(words[index]) + len(
					delimiter
				)  # Reset the line_counter
		elif line_counter == 75:
			words[index] += '\n' + words[index]  # Add '\n' to the current word

	return delimiter.join(words)  # Join the words back together with the delimiter


# │ Time to put down your phone and get back to work! Enter my room code:       │
