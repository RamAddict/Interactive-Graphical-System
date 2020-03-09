"""Primitive graphics API."""

from typing import Tuple

from util import pairwise


class Painter():
    """Interface providing primitive graphics drawing."""

    def draw_pixel(self, x, y):
        raise NotImplementedError("Painter is an abstract class.")

    def draw_line(self, xa, ya, xb, yb):
        raise NotImplementedError("Painter is an abstract class.")


class Drawable():
    def draw(self, painter: Painter):
        raise NotImplementedError("Drawable is an abstract class.")


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
    def y(self, y):
        self._coordinates[1] = y

    def __getitem__(self, key):
        return self._coordinates[key]

    def __setitem__(self, key, item):
        self._coordinates[key] = item

    def __str__(self):
        return '({} {})'.format(self.x, self.y)


class Line(Drawable):
    def __init__(self, pa: Point, pb: Point):
        self._points = [pa, pb]

    def draw(self, painter):
        painter.draw_line(self._points[0].x, self._points[0].y,
                          self._points[1].x, self._points[1].y)

    def __getitem__(self, key):
        return self._points[key]

    def __setitem__(self, key, point: Point):
        self._points[key] = point

    def __str__(self):
        return '({}; {})'.format(self[0], self[1])


class Wireframe(Drawable):
    """Polygon-like object defined by a sequence of points."""

    def __init__(self, *points: Tuple[Point]):
        self.points = list(points)

    def draw(self, painter):
        for pa, pb in pairwise(self.points + [self.points[0]]):
            painter.draw_line(pa.x, pa.y, pb.x, pb.y)

    def __getitem__(self, key):
        return self.points[key]

    def __setitem__(self, key, point: Point):
        self.points[key] = point

    def __str__(self):
        return '({})'.format(
            '; '.join(str(p) for p in self.points + [self.points[0]])
        )
