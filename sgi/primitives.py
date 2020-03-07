"""Primitive graphics API."""

from abc import ABC, abstractmethod


class Painter(ABC):
    """Interface providing primitive graphics drawing."""

    @abstractmethod
    def draw_pixel(self, x, y):
        pass

    @abstractmethod
    def draw_line(self, x1, y1, x2, y2):
        pass


class Drawable(ABC):
    @abstractmethod
    def draw(self, painter: Painter):
        pass


class Point(Drawable):
    def __init__(self, x, y):
        self._coordinates = [x, y]

    def draw(self, painter):
        painter.draw_pixel(self._coordinates[0], self._coordinates[1])

    @property
    def x(self):
        return self._coordinates[0]

    @x.setter
    def x(self, x):
        self._coordinates[0] = x

    @property
    def y(self):
        return self._coordinates[1]

    @y.setter
    def y(self, t):
        self._coordinates[1] = t

    def __getitem__(self, key):
        return self._coordinates[key]

    def __setitem__(self, key, item):
        self._coordinates[key] = item

    def __str__(self):
        return '({} {})'.format(self.x, self.y)


class Line(Drawable):
    def __init__(self, p1: Point, p2: Point):
        self._points = [p1, p2]

    def draw(self, painter):
        painter.draw_line(self._points[0].x, self._points[0].y,
                          self._points[1].x, self._points[1].y)

    def __getitem__(self, key):
        return self._points[key]

    def __setitem__(self, key, point: Point):
        self._points[key] = point

    def __str__(self):
        return '({}; {})'.format(self[0], self[1])
