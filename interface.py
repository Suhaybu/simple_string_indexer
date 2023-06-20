# This file's purpose is handelling most of the print statemnts

from magic import index_string, clear_terminal
from colorama import init, Fore

init()

# Greeting
greeting = f'''
{Fore.CYAN}:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
{Fore.CYAN}::{Fore.RED}█▀ █ █▀▄▀█ █▀█ █░░ █▀▀   █▀ ▀█▀ █▀█ █ █▄░█ █▀▀   █ █▄░█ █▀▄ █▀▀ ▀▄▀ █▀▀ █▀█{Fore.CYAN}::
{Fore.CYAN}::{Fore.RED}▄█ █ █░▀░█ █▀▀ █▄▄ ██▄   ▄█ ░█░ █▀▄ █ █░▀█ █▄█   █ █░▀█ █▄▀ ██▄ █░█ ██▄ █▀▄{Fore.CYAN}::
{Fore.CYAN}:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
{Fore.CYAN}:::::::::::::::::· {Fore.RESET}Welcome user to my simple Python program! {Fore.CYAN}·:::::::::::::::::
{Fore.CYAN}:::::::· {Fore.RESET}Coded & designed by suhaybu. ASCII text https://fsymbols.com/ {Fore.CYAN}·:::::::{Fore.RESET}
'''

# Breaker
breaker = f'{Fore.CYAN}:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::{Fore.RESET}'


# Ask for input
def get_input():
    input_string = input(f'{Fore.CYAN}:: {Fore.YELLOW}Enter the string you wish to index:\n{Fore.WHITE}')
    return input_string


# Print method
def get_output(input_string):
    # Prepares the terminal for new output interface
    clear_terminal()
    print(greeting)
    print(breaker)

    print('HERE ARE YOUR STRING WITH INDEXES:')
    print(index_string(input_string))


input_string = ''

print(greeting)
input = get_input()
get_output(input)
# get_output('My test is this sentence')
