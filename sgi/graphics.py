"""@TODO: graphics module docstring"""

from abc import ABC, abstractmethod
from collections import namedtuple

import colors


class Painter(ABC):
    """@TODO: Painter class docstrings"""

    def __init__(self):
        self.color = colors.BLACK

    @abstractmethod
    def draw_pixel(self, x: int, y: int):
        pass

    @abstractmethod
    def draw_line(self, x1: int, y1: int, x2: int, y2: int):
        pass


class Drawable(ABC):
    """@TODO: Drawable interface docstrings"""

    @abstractmethod
    def draw(self, painter: Painter):
        pass


"""@TODO: drawable primitives docstrings"""

class Point(Drawable, namedtuple('Point', ['x', 'y'])):
    def draw(self, painter):
        painter.draw_pixel(self.x, self.y)

class Line(Drawable, namedtuple('Line', ['p1', 'p2'])):
    def draw(self, painter):
        painter.draw_line(self.p1.x, self.p1.y, self.p2.x, self.p2.y)

class Wireframe(Drawable):  # @TODO
    def draw(self, painter):
        pass
