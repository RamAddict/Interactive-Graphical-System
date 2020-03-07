"""@TODO: graphics module docstring"""

from abc import ABC, abstractmethod
from typing import Tuple

from .util import interlaced


class Painter(ABC):
    """@TODO: Painter class docstrings"""

    def __init__(self, camera):
        self.camera = camera

    @abstractmethod
    def draw_pixel(self, x, y):
        pass

    @abstractmethod
    def draw_line(self, x1, y1, x2, y2):
        pass


class Drawable(ABC):
    """@TODO: Drawable interface docstrings"""

    @abstractmethod
    def draw(self, painter: Painter):
        pass


class Point(Drawable):
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def draw(self, painter):
        painter.draw_pixel(self.x, self.y)


class Line(Drawable):
    def __init__(self, p1: Point, p2: Point):
        self._p1 = p1
        self._p2 = p2

    def draw(self, painter):  # @TODO: better names?
        painter.draw_line(self._p1.x, self._p1.y, self._p2.x, self._p2.y)


class Wireframe(Drawable):
    def __init__(self, *points: Tuple[Point]):
        self.points = list(points)

    def draw(self, painter):
        for p1, p2 in interlaced(self.points + [self.points[0]]):
            painter.draw_line(p1.x, p1.y, p2.x, p2.y)
