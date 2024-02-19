"""
Display introduces logic enabling logging to be bundled with print statements
"""
from colorama import Fore, Style  # noqa: F401

history = ''


def display(new_data: str):
	global history

	if new_data is not None:
		print(new_data)
		history += new_data + '\n'

		return history
	else:
		raise ValueError('The parameter is invalid. Make sure they exist.')


# # Testing
# display(interface.splitter('user input'))
# # display(interface.splitter())
# print('First History')
# print(history)

# display(interface.splitter('user input'))
# display(interface.splitter('user input'))
# print('Second History')
# print(history)
