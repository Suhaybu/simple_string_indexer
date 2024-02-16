"""
Display class introduces logic enabling logging to be bundled with print statements
"""
from src.interface import (  # noqa: F401
	enter,
	error,
	fancy_input,
	greeting,
	menu,
	splitter,
)


def display(type: str, component: str, state=None):
	if type not in ['input', 'output']:
		raise ValueError('Type specified must be input or output')

	if callable(component):
		print(component(state))
	else:
		raise TypeError('Component must be callable.')


display('input', '')
