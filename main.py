import interface
import ask
import show

choice = 'input'

print(interface.greeting)
while choice == 'input':
    delimiter = ask.get_delimiter()
    user_input = ask.get_string()
    show.get_output(user_input, delimiter)

    while choice != 'exit' and choice == 'input':
        choice = ask.other_options()
        print(f'choice is {choice}')
        if choice != 'input' and choice != 'exit':
            show.get_other_option(user_input, choice)
            print(f'end of choice {choice}')
raise SystemExit("Exiting the program.")
