from functools import wraps


class Director():
    def __init__(self, builder):
        self._builder = builder

    def construct_car(self):
        self._builder.create_new_car()
        self._builder.add_model(**self._builder.kwargs)
        self._builder.add_tires(**self._builder.kwargs)
        self._builder.add_engine(**self._builder.kwargs)

    def get_car(self):
        return self._builder.car


class Builder():
    def __init__(self, **kwargs):
        self.car = None
        self.kwargs = kwargs

    def create_new_car(self):
        self.car = Car()


class CarBuilder(Builder):
    class _decor(object):
        @classmethod
        def check_kwargs(cls, decorated):
            @wraps(decorated)
            def wrapper(*args, **kwargs):
                send_kwargs = dict(model='Standard', tires='Basic', engine='250cc')
                for k, v in kwargs.items():
                    send_kwargs[k] = v
                return decorated(*args, **send_kwargs)
            return wrapper

    @_decor.check_kwargs
    def add_model(self, **kwargs):
        self.car.model = kwargs.get('model', None)

    @_decor.check_kwargs
    def add_tires(self, **kwargs):
        self.car.tires = kwargs.get('tires', None)

    @_decor.check_kwargs
    def add_engine(self, **kwargs):
        self.car.engine = kwargs.get('engine', None)


class Car():
    def __init__(self):
        self.model = None
        self.tires = None
        self.engine = None

    def __str__(self):
        return f'{self.model} | {self.tires} | {self.engine}'


specs = [
    {},
    {'model': 'Jeep Grand Cherokee'},
    {'model': 'Ford F-250', 'tires': 'Really Big Ones'},
    {'model': 'Honda Accord', 'engine': 'Really small one...'},
]

cars = []

for i in specs:
    d = Director(CarBuilder(**i))
    d.construct_car()
    cars.append(str(d.get_car()))

print(cars)
