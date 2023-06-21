# This file's purpose is storing all print statemnts
from os import error
from colorama import Fore, Style


# Greeting
greeting = f'''
{Fore.LIGHTYELLOW_EX}┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
{Fore.LIGHTYELLOW_EX}┃ {Fore.RED}█▀ █ █▀▄▀█ █▀█ █░░ █▀▀   █▀ ▀█▀ █▀█ █ █▄░█ █▀▀   █ █▄░█ █▀▄ █▀▀ ▀▄▀ █▀▀ █▀█{Fore.LIGHTYELLOW_EX} ┃
{Fore.LIGHTYELLOW_EX}┃ {Fore.RED}▄█ █ █░▀░█ █▀▀ █▄▄ ██▄   ▄█ ░█░ █▀▄ █ █░▀█ █▄█   █ █░▀█ █▄▀ ██▄ █░█ ██▄ █▀▄{Fore.LIGHTYELLOW_EX} ┃
{Fore.LIGHTYELLOW_EX}┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛

{Fore.CYAN}:::::::::::::::::· {Fore.RESET}Welcome user to my simple Python program! {Fore.CYAN}·:::::::::::::::::
{Fore.CYAN}:::::::· {Fore.RESET}Coded & designed by suhaybu. ASCII text https://fsymbols.com/ {Fore.CYAN}·:::::::{Fore.RESET}
'''


# Ask for string input
ask_option = f'{Fore.CYAN}:: {Fore.YELLOW}Enter your choice{Fore.WHITE}: {Fore.RESET}'
ask_delimiter = f'{Fore.CYAN}:: {Fore.YELLOW}Enter the delimiter of your choice{Fore.WHITE}: {Fore.RESET}'
ask_input = f'{Fore.CYAN}:: {Fore.YELLOW}Enter the string you wish to index{Fore.WHITE}: {Fore.RESET}'

# Splitters
split_option = f'{Fore.CYAN}:::::::::::::::::::::::::::::· {Fore.LIGHTYELLOW_EX}Select an option: {Fore.CYAN}·:::::::::::::::::::::::::::::{Fore.RESET}'
split_input = f'{Fore.CYAN}::::::::::::::::::::::::::::::::· {Fore.LIGHTYELLOW_EX}Your input: {Fore.CYAN}·::::::::::::::::::::::::::::::::{Fore.RESET}'
split_result = f'{Fore.CYAN}::::::::::::::::::::::::::::::· {Fore.LIGHTYELLOW_EX}Indexed Result: {Fore.CYAN}·::::::::::::::::::::::::::::::{Fore.RESET}'


# MENUES
menu_delimiter = f'''{Fore.LIGHTYELLOW_EX}╔═════════════════════════════════════════════════════════════════════════════╗
║ {Fore.WHITE}1. {Fore.LIGHTBLUE_EX}Default{Fore.WHITE}: {Fore.WHITE}Words in string are seperated with single SPACE{Style.RESET_ALL}{Fore.LIGHTYELLOW_EX}                 ║
║ {Fore.WHITE}2. {Fore.LIGHTBLUE_EX}Custom{Fore.WHITE}: {Fore.WHITE}Provide a custom delimiter{Style.RESET_ALL}{Fore.LIGHTYELLOW_EX}                                       ║
╚═════════════════════════════════════════════════════════════════════════════╝
'''
menu_other_options = f'''{Fore.LIGHTYELLOW_EX}╔═════════════════════════════════════════════════════════════════════════════╗
║ {Fore.WHITE}1. {Fore.WHITE}Find index of a specific word{Fore.LIGHTYELLOW_EX}                                            ║
║ {Fore.WHITE}2. {Fore.WHITE}Find word at a specfiic index{Fore.LIGHTYELLOW_EX}                                            ║
║ {Fore.WHITE}3. {Fore.WHITE}Input another String{Fore.LIGHTYELLOW_EX}                                                     ║
║ {Fore.WHITE}4. {Fore.WHITE}Exit{Fore.LIGHTYELLOW_EX}                                                                     ║
╚═════════════════════════════════════════════════════════════════════════════╝
'''

# Errors
error_option = f'''{Fore.LIGHTYELLOW_EX}╔═════════════════════════════════════════════════════════════════════════════╗
║                 {Style.BRIGHT}{Fore.RED}Invalid Choice. Please enter a valid number{Style.RESET_ALL}{Fore.LIGHTYELLOW_EX}                 ║
╚═════════════════════════════════════════════════════════════════════════════╝
'''
