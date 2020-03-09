"""Primitive graphics API."""

from typing import Tuple

from util import pairwise


class Painter():
    """Interface providing primitive graphics drawing."""

    def draw_pixel(self, x: int, y: int):
        raise NotImplementedError("Painter is an abstract class.")

    # @NOTE: evidently, draw_line can be implemented with draw_pixel
    def draw_line(self, xa: int, ya: int, xb: int, yb: int):
        # Bresenham's line algorithm, which is based on a decision parameter p
        # allowing to solve y = mx + c using only integer operations {+, -, 2*}
        dx = xb - xa
        dy = yb - ya
        sign_x = +1 if dx >= 0 else -1
        sign_y = +1 if dy >= 0 else -1
        x, y = xa, ya

        # common subexpression optimization
        DX2 = 2*dx*sign_x
        DY2 = 2*dy*sign_y
        DY2X2 = DY2 - DX2
        DX2Y2 = DX2 - DY2

        if abs(dx) >= abs(dy):
            # pi = (d1-d2)*dx, d1 = y - yi, d2 = (yi + 1) - y -> pa = 2*dy - dx
            p = 2*dy*sign_y - dx*sign_x

            # dp = 2*dy - 2*dx*inc_x
            for _ in range(dx*sign_x + 1):
                self.draw_pixel(x, y)
                x += sign_x
                if p >= 0:
                    y += sign_y
                    p += DY2X2
                else:
                    p += DY2
        else:
            # pi = (d1-d2)*dy, d1 = x - xi, d2 = (xi + 1) - x -> pa = 2*dx - dy
            p = 2*dx*sign_x - dy*sign_y

            # dp = 2*dx - 2*dy*inc_y
            for _ in range(dy*sign_y + 1):
                self.draw_pixel(x, y)
                y += sign_y
                if p >= 0:
                    x += sign_x
                    p += DX2Y2
                else:
                    p += DX2


class Drawable():
    def draw(self, painter: Painter):
        raise NotImplementedError("Drawable is an abstract class.")


class Point(Drawable):
    def __init__(self, x, y):
        self._coordinates = [x, y]

    def draw(self, painter):
        painter.draw_pixel(int(self._coordinates[0]),
                           int(self._coordinates[1]))

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
        painter.draw_line(int(self._points[0].x), int(self._points[0].y),
                          int(self._points[1].x), int(self._points[1].y))

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
            painter.draw_line(int(pa.x), int(pa.y), int(pb.x), int(pb.y))

    def __getitem__(self, key):
        return self.points[key]

    def __setitem__(self, key, point: Point):
        self.points[key] = point

    def __str__(self):
        return '({})'.format(
            '; '.join(str(p) for p in self.points + [self.points[0]])
        )
