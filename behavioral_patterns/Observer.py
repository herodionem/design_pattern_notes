class Subject(object):

    def __init__(self):
        self._observers = []

    def attach(self, observer):
        if observer not in self._observers:
            self._observers.append(observer)

    def detach(self, observer):
        try:
            self._observers.remove(observer)
        except ValueError:
            pass

    def notify(self, modifier=None):
        for o in self._observers:
            if modifier != o:
                o.update(self)


class Core(Subject):

    def __init__(self, name=""):
        super().__init__()
        self._name = name
        self._temp = 0

    @property
    def temp(self):
        return self._temp

    @temp.setter
    def temp(self, temp):
        self._temp = temp
        self.notify(self)


class TempViewer:

    def update(self, subject):
        print(f"Temperature Viewer <{id(self)}>: {subject._name} has a temperature of {subject._temp}")


c1 = Core("core 1")
c2 = Core("core 2")

v1 = TempViewer()
v2 = TempViewer()
v3 = TempViewer()

c1.attach(v1)
c1.attach(v2)
c2.attach(v3)

c1.temp = 64
c1.temp = 74
c2.temp = 101.5

c1.detach(v1)
c2.detach(v3)

c1.temp = '10,000 Kelvin'
c2.temp = 'Romm Temperature'
