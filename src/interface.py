"""
This file's purpose is storing all statements and designs that will be printed
"""
from colorama import Fore, Style

# Greeting
greeting = f"""
{Fore.LIGHTYELLOW_EX}┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
{Fore.LIGHTYELLOW_EX}┃ {Fore.RED}█▀ █ █▀▄▀█ █▀█ █░░ █▀▀   █▀ ▀█▀ █▀█ █ █▄░█ █▀▀   █ █▄░█ █▀▄ █▀▀ ▀▄▀ █▀▀ █▀█{Fore.LIGHTYELLOW_EX} ┃
{Fore.LIGHTYELLOW_EX}┃ {Fore.RED}▄█ █ █░▀░█ █▀▀ █▄▄ ██▄   ▄█ ░█░ █▀▄ █ █░▀█ █▄█   █ █░▀█ █▄▀ ██▄ █░█ ██▄ █▀▄{Fore.LIGHTYELLOW_EX} ┃
{Fore.LIGHTYELLOW_EX}┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛

{Fore.CYAN}:::::::::::::::::· {Fore.RESET}Welcome user to my simple Python program! {Fore.CYAN}·:::::::::::::::::
{Fore.CYAN}:::::::· {Fore.RESET}Coded & designed by suhaybu. ASCII text https://fsymbols.com/ {Fore.CYAN}·:::::::{Fore.RESET}"""


# Askers
def enter(state):
	if state == 'choice':
		return f'{Fore.CYAN}:: {Fore.YELLOW}Enter your choice{Fore.WHITE}: {Fore.RESET}'
	elif state == 'delimiter':
		return f'{Fore.CYAN}:: {Fore.YELLOW}Enter the delimiter of your choice{Fore.WHITE}: {Fore.RESET}'
	elif state == 'input':
		return f'{Fore.CYAN}:: {Fore.YELLOW}Enter the string you wish to index{Fore.WHITE}: {Fore.RESET}'
	elif state == 'find index':
		return f'{Fore.CYAN}:: {Fore.YELLOW}Enter the word to find its index{Fore.WHITE}: {Fore.RESET}'
	elif state == 'find word':
		return f'{Fore.CYAN}:: {Fore.YELLOW}Enter the index to return its word{Fore.WHITE}: {Fore.RESET}'


# Splitters
def splitter(type):
	if type == 'select':
		return f'\n{Fore.CYAN}:::::::::::::::::::::::::::::· {Fore.LIGHTYELLOW_EX}Select an option: {Fore.CYAN}·:::::::::::::::::::::::::::::{Fore.RESET}'
	elif type == 'user input':
		return f'{Fore.CYAN}::::::::::::::::::::::::::::::::· {Fore.LIGHTYELLOW_EX}Your input: {Fore.CYAN}·::::::::::::::::::::::::::::::::{Fore.RESET}'
	elif type == 'result':
		return f'\n{Fore.CYAN}::::::::::::::::::::::::::::::· {Fore.LIGHTYELLOW_EX}Indexed Result: {Fore.CYAN}·::::::::::::::::::::::::::::::{Fore.RESET}'
	elif type == 'input':
		return f'\n{Fore.CYAN}:::::::::::::::::::::::::::· {Fore.LIGHTYELLOW_EX}Input another String: {Fore.CYAN}·:::::::::::::::::::::::::::{Fore.RESET}'
	elif type == 'find word':
		return f'\n{Fore.CYAN}::::::::::::::::::::::::::::· {Fore.LIGHTYELLOW_EX}Find word at index: {Fore.CYAN}·::::::::::::::::::::::::::::{Fore.RESET}'
	elif type == 'find index':
		return f'\n{Fore.CYAN}:::::::::::::::::::::::::::· {Fore.LIGHTYELLOW_EX}Find index of a word: {Fore.CYAN}·:::::::::::::::::::::::::::{Fore.RESET}'
	elif type == 'return index':
		return f'\n{Fore.CYAN}::::::::::::::::::::::::::· {Fore.LIGHTYELLOW_EX}The index of your word: {Fore.CYAN}·::::::::::::::::::::::::::{Fore.RESET}'
	elif type == 'return word':
		return f'\n{Fore.CYAN}::::::::::::::::::::::::::· {Fore.LIGHTYELLOW_EX}The word at your index: {Fore.CYAN}·::::::::::::::::::::::::::{Fore.RESET}'


# MENUS


def menu(type):
	if type == 'delimiter':
		return f"""{Fore.LIGHTYELLOW_EX}╔═════════════════════════════════════════════════════════════════════════════╗
║ {Fore.WHITE}1. {Fore.LIGHTBLUE_EX}Default{Fore.WHITE}: {Fore.WHITE}Words in string are separated with single SPACE{Style.RESET_ALL}{Fore.LIGHTYELLOW_EX}                 ║
║ {Fore.WHITE}2. {Fore.LIGHTBLUE_EX}Custom{Fore.WHITE}: {Fore.WHITE}Provide a custom delimiter{Style.RESET_ALL}{Fore.LIGHTYELLOW_EX}                                       ║
╚═════════════════════════════════════════════════════════════════════════════╝
"""
	elif type == 'other options':
		return f"""{Fore.LIGHTYELLOW_EX}╔═════════════════════════════════════════════════════════════════════════════╗
║ {Fore.WHITE}1. {Fore.WHITE}Find index of a specific word{Fore.LIGHTYELLOW_EX}                                            ║
║ {Fore.WHITE}2. {Fore.WHITE}Find word at a specific index{Fore.LIGHTYELLOW_EX}                                            ║
║ {Fore.WHITE}3. {Fore.WHITE}Input another String{Fore.LIGHTYELLOW_EX}                                                     ║
║ {Fore.WHITE}4. {Fore.WHITE}Exit{Fore.LIGHTYELLOW_EX}                                                                     ║
╚═════════════════════════════════════════════════════════════════════════════╝
"""


# Errors
def error(type):
	if type == 'invalid choice':
		return f"""{Fore.LIGHTYELLOW_EX}╔═════════════════════════════════════════════════════════════════════════════╗
║                 {Style.BRIGHT}{Fore.RED}Invalid Choice. Please enter a valid number{Style.RESET_ALL}{Fore.LIGHTYELLOW_EX}                 ║
╚═════════════════════════════════════════════════════════════════════════════╝"""


# Fancy input
def fancy_input(type):
	if type == 'top':
		return f'{Fore.LIGHTGREEN_EX}╭─────────────────────────────────────────────────────────────────────────────╮{Fore.RESET}'
	if type == 'bottom':
		return f'{Fore.LIGHTGREEN_EX}╰─────────────────────────────────────────────────────────────────────────────╯{Fore.RESET}'
