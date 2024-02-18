"""
Display introduces logic enabling logging to be bundled with print statements
"""
import interface
from colorama import Fore, Style  # noqa: F401
from interface import (  # noqa: F401
	enter,
	error,
	fancy_input,
	greeting,
	menu,
	splitter,
)


def display(parameter: str):
	if parameter is not None:
		print(parameter)
	else:
		raise ValueError('The parameter is invalid. Make sure they exist.')


# Testing
display(interface.splitter('user input'))
display(interface.splitter())
