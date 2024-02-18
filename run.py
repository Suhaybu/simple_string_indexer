from src import ask, interface, receive

if __name__ == '__main__':
	choice = 'input'  # Default state is receiving input
	print(interface.greeting)  # Prints the greetings banner

	while choice == 'input':  # Ensures program runs until exited
		delimiter = ask.get_delimiter()
		user_input = ask.get_string()

		receive.get_output(user_input, delimiter)
		choice = ask.other_options()

		while choice != 'input' and choice != 'exit':
			receive.get_other_option(user_input, choice, delimiter)
			choice = ask.other_options()

	raise SystemExit('Exiting the program.')
