class DrawingAPIOne(object):
    def draw_circle(self, x, y, r):
        print(f"API 1 drawing a circle at ({x}, {y} with radius {r})")


class DrawingAPITwo(object):
    def draw_circle(self, x, y, r):
        print(f"API 2 drawing a circle at ({x}, {y} with radius {r})")


class Circle(object):
    def __init__(self, x, y, r, api):
        self._x = x
        self._y = y
        self._r = r
        self._api = api

    def draw(self):
        self._api.draw_circle(self._x, self._y, self._r)

    def scale(self, percent):
        self._r *= percent


circle1 = Circle(1, 2, 3, DrawingAPIOne())
circle1.draw()

circle2 = Circle(2, 3, 4, DrawingAPITwo())
circle2.draw()