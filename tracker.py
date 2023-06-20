# Class I created to help me keep track of all the user interactions
# to make it possible to retain history when I create the next scene


class Logger:
    log = []

    def __init__(self) -> None:
        print('Test')

    def add(state):
        Logger.log.append(state)

    def retrieve():
        return Logger.log


Logger()
Logger.add('greeting')
Logger.add('printed')
Logger.add('exit')
print(Logger.retrieve())
