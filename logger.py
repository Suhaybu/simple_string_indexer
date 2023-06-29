# Class I created to help me keep track of all the user interactions
# to make it possible to retain history when I create the next scene


class Logger:
    def __init__(self, name):
        self.name = name
        self.log = {}

    def add(self, state, data=None):
        state_type = 0 if data is None else 1
        self.log[state] = state_type, data

    def retrieve(self):
        return self.log

    def clear(self):
        self.log = {}

    def print_log(self):
        for state, (state_type, data) in self.log.items():
            print(f"{state}: {state_type} {data}")


Logger()
Logger.add('greeting')
Logger.add('printed', 'true')
Logger.add('exit')
print(Logger.retrieve())
