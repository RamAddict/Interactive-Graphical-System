"""Higher-level graphics API."""

from primitives import Drawable, Point, Painter
from typing import Tuple

from util import pairwise


class Wireframe(Drawable):
    def __init__(self, *points: Tuple[Point]):
        self.points = list(points)

    def draw(self, painter):
        for p1, p2 in pairwise(self.points + [self.points[0]]):
            painter.draw_line(p1.x, p1.y, p2.x, p2.y)

    def __getitem__(self, key):
        return self.points[key]

    def __setitem__(self, key, point: Point):
        self.points[key] = point

    def __str__(self):
        return '({})'.format(
            '; '.join(str(p) for p in self.points + [self.points[0]])
        )


class Camera(Painter):
    """Used to render objects using a window as reference."""

    def __init__(self, viewport_width, viewport_height, painter: Painter,
                 center: Point):
        self._viewport_width = viewport_width
        self._viewport_height = viewport_height
        self.painter = painter
        self.position = center
        self.width = viewport_width
        self.height = viewport_height

    def draw_pixel(self, x, y):
        x, y = self._transform(x - self.x, y - self.y)
        self.painter.draw_pixel(x, y)

    def draw_line(self, x1, y1, x2, y2):
        x1, y1 = self._transform(x1 - self.x, y1 - self.y)
        x2, y2 = self._transform(x2 - self.x, y2 - self.y)
        self.painter.draw_line(x1, y1, x2, y2)

    def _transform(self, x, y) -> Tuple:
        """Apply the Window to Viewport Transformation on given coordinates."""
        x_min = self.x - self.width/2
        x = (x - x_min) * self._viewport_width / self.width
        y_min = self.y - self.height/2
        y = self._viewport_height * (1 - (y - y_min)/self.height)
        return x, y

    @property
    def zoom(self):
        return self._viewport_width / self.width

    @zoom.setter
    def zoom(self, scale):
        self.width /= scale
        self.height /= scale

    @property
    def x(self):
        return self.position.x

    @x.setter
    def x(self, x):
        self.position.x = x

    @property
    def y(self):
        return self.position.y

    @y.setter
    def y(self, y):
        self.position.y = y
