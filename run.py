from src import ask, interface, show

if __name__ == '__main__':
    choice = 'input'

    print(interface.greeting)
    while choice == 'input':
        delimiter = ask.get_delimiter()
        user_input = ask.get_string()
        show.get_output(user_input, delimiter)
        choice = ask.other_options()

        while choice != 'input' and choice != 'exit':
            show.get_other_option(user_input, choice, delimiter)
            choice = ask.other_options()

    raise SystemExit("Exiting the program.")
