# Class I created to help me keep track of all the user interactions
# to make it possible to retain history when I create the next scene


class Logger:
    log = []

    def __init__(self) -> None:
        print('Test')

    @staticmethod
    def add(state, data=None):
        if data == None:
            data = 1
        Logger.log.append((state, data))

    @staticmethod
    def retrieve():
        return Logger.log


Logger()
Logger.add('greeting')
Logger.add('printed', 'true')
Logger.add('exit')
print(Logger.retrieve())
