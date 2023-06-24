import interface
import ask
import show

choice = 'input'

print(interface.greeting)
while choice == 'input':
    delimiter = ask.get_delimiter()
    user_input = ask.get_string()
    show.get_output(user_input, delimiter)
    choice = ask.other_options()

if choice == 'exit':
    raise SystemExit("Exiting the program.")
