import types

class Strategy:
    def __init__(self, function=None):
        self.name = "Default Strategy"

        if function:
            self.execute = types.MethodType(function, self)

    def execute(self):
        print(f"{self.name} is being used...")


def strategy_one(self):
    print(f"{self.name} is used to execute method 1")


def strategy_two(self):
    print(f"{self.name} is used to execute method 2")


s1 = Strategy()
s1.execute()

s2 = Strategy(strategy_one)
s2.name = "Strategy One"
s2.execute()

s3 = Strategy(strategy_two)
s3.name = "Strategy Two"
s3.execute()
