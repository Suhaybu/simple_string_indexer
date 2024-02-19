"""
Handles all the questions that are asked
"""
from src import interface
from src.display import display


# Ask for delimiter
def get_delimiter() -> str:
	display(interface.splitter('select'))  # displays the splitter for select option
	display(interface.menu('delimiter'))  # displays delimiter menu
	# Catches invalid input
	while True:
		try:
			choice = int(
				input(interface.enter('choice'))
			)  # Prompts the user for choice
			if choice == 1:
				return ' '
			elif choice == 2:
				return input(interface.enter('delimiter'))
			else:
				display(interface.error('invalid choice'))
				display(interface.menu('delimiter'))
		except ValueError:
			display(interface.error('invalid choice'))
			display(interface.menu('delimiter'))


# Asks the user for input
def get_string():
	display(interface.splitter('user input'))
	return input(interface.enter('input'))


# Asks the user for other options
def other_options():
	display(interface.splitter('select'))  # displays the splitter for select option
	display(interface.menu('other options'))
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
				display(interface.error('invalid choice'))
				display(interface.menu('other options'))
		except ValueError:
			display(interface.error('invalid choice'))
			display(interface.menu('other options'))
