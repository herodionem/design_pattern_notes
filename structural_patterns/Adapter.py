class Chinese:
    def __init__(self):
        self.name = "Chinese"

    def speak_chinese(self):
        return "Ni hao ma?"


class American:
    def __init__(self):
        self.name = "American"

    def speak_american(self):
        return "'Sup ya'll?"


class Adapter:
    def __init__(self, object, **adapted_method):
        self._object = object
        self.__dict__.update(adapted_method)

    def __getattr__(self, attr):
        return getattr(self._object, attr)


objects = []

zhongguoren = Chinese()
americanperson = American()

objects += [
    Adapter(zhongguoren, speak=zhongguoren.speak_chinese),
    Adapter(americanperson, speak=americanperson.speak_american)
]

for obj in objects:
    print(f"{obj.name} people say '{obj.speak()}'")
