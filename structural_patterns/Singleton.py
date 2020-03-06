class Borg:

    _shared_state = {}

    def __init__(self):
        self.__dict__ = self._shared_state


class Singleton(Borg):

    def __init__(self, **kwargs):
        super().__init__()
        self._shared_state.update(**kwargs)

    def __str__(self):
        return str(self._shared_state)


x = Singleton(HTTP = "Hyper Text Transfer Protocol")
print(f"printing x: {x}")
print(f"printing x.__dict__: {x.__dict__}")

y = Singleton(FTP = "File Transfer Protocol")
print(f"printing y: {y}")
print(f"printing y.__dict__: {y.__dict__}")

x.__dict__ = {'breaking': 'singleton'}
print(f"printing x: {x}")
print(f"printing x.__dict__: {x.__dict__}")
print(f"printing y: {y}")
print(f"printing y.__dict__: {y.__dict__}")

z = Singleton(KYBO = "Keep Your Bowels Open")

print(f"printing x: {x}")
print(f"x id = {id(x)}")
print(f"x.__dict__ id = {id(x.__dict__)}")
print(f"printing y: {y}")
print(f"y id = {id(y)}")
print(f"y.__dict__ id = {id(y.__dict__)}")
print(f"printing z: {z}")
print(f"z id = {id(z)}")
print(f"z.__dict__ id = {id(z.__dict__)}")
