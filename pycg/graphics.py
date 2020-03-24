"""Computer Graphics API."""

from typing import Tuple
from math import sqrt

from blas import Vector, Matrix
from utilities import pairwise


class Painter():
    """Interface providing primitive graphics drawing."""

    def draw_pixel(self, x: int, y: int):
        raise NotImplementedError("Painter is an abstract class.")

    def draw_line(self, xa: int, ya: int, xb: int, yb: int):
        # Bresenham's line algorithm, which is based on a decision parameter p
        # allowing to solve y = mx + c using only integer operations {+, -, 2*}
        xa, ya, xb, yb = int(xa), int(ya), int(xb), int(yb)  # "typing"
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


class Point(Drawable, Vector):
    def __init__(self, x, y):
        super(Point, self).__init__(x, y)

    def draw(self, painter):
        painter.draw_pixel(self.x, self.y)

    def __repr__(self):  # as by the Well-known text representation of geometry
        return "POINT ({} {})".format(self.x, self.y)

    def center(self):
        return self

    def transform(self, transformation: Matrix, pivot=None):
        pivot = pivot if pivot else self.center()
        self._coordinates = transformation * pivot

class Line(Drawable):
    def __init__(self, pa: Point, pb: Point):
        self._points = [pa, pb]

    def draw(self, painter):
        painter.draw_line(self._points[0].x, self._points[0].y,
                          self._points[1].x, self._points[1].y)

    def __getitem__(self, key: int) -> Point:
        return self._points[key]

    def __setitem__(self, key: int, point: Point):
        self._points[key] = point

    def __repr__(self):  # WKT
        return "LINESTRING ({} {}, {} {})".format(
            self[0].x, self[0].y,
            self[1].x, self[1].y
        )

    def __len__(self) -> float:
        return sqrt((self[0].x - self[1].x)**2 + (self[0].y - self[1].y)**2)


class Wireframe(Drawable):
    """Polygon-like object defined by a sequence of points."""

    def __init__(self, a: Point, b: Point, c: Point, *points: Point):
        self._points = [a, b, c] + list(points) + [a]  # closed polygon

    def draw(self, painter):
        for pa, pb in pairwise(self._points):
            painter.draw_line(pa.x, pa.y, pb.x, pb.y)

    def __len__(self):
        return len(self._points) - 1

    def __getitem__(self, key: int) -> Point:
        if key >= len(self):
            raise IndexError("Index {} out of range.".format(key))
        else:
            return self._points[key]

    def __setitem__(self, key: int, point: Point):
        if key >= len(self):
            raise IndexError("Index {} out of range.".format(key))
        else:
            self._points[key] = point

    def __repr__(self):  # WKT
        return "POLYGON ((%s))" % ", ".join(
            "{} {}".format(p.x, p.y) for p in self._points
        )


class Camera(Painter):
    """Window used as reference to render objects."""

    def __init__(self, painter: Painter, center: Point, viewport_size: Vector):
        self.painter = painter
        self._position = center
        self._viewport_size = viewport_size
        self._width = viewport_size.x
        self._height = viewport_size.y
        self._recalculate_corners()

    def _recalculate_corners(self):
        self._x_min = self.x - self._width/2
        self._y_min = self.y - self._height/2

    def draw_pixel(self, x: int, y: int):
        x, y = self._to_viewport(x, y)
        self.painter.draw_pixel(x, y)

    def draw_line(self, xa: int, ya: int, xb: int, yb: int):
        xa, ya = self._to_viewport(xa, ya)
        xb, yb = self._to_viewport(xb, yb)
        self.painter.draw_line(xa, ya, xb, yb)

    def _to_viewport(self, x, y) -> Tuple:  # @XXX: private or public?
        """Apply the Window-to-Viewport Transformation on given coordinates."""
        # equivalent to lerp(x, x_min, x_max, 0, viewport_width),
        x = (x - self._x_min) * self._viewport_size.x / self._width
        # viewport_height - lerp(y, y_min, y_max, 0, viewport_height)
        y = self._viewport_size.y * (1 - (y - self._y_min)/self._height)
        return x, y

    @property
    def x(self):
        return self._position.x

    @x.setter
    def x(self, x):
        self._position.x = x
        self._recalculate_corners()

    @property
    def y(self):
        return self._position.y

    @y.setter
    def y(self, y):
        self._position.y = y
        self._recalculate_corners()

    @property  # @XXX: perhaps width AND height are not necessary -> see FOV
    def width(self):
        return self._width

    @width.setter
    def width(self, w):
        self._width = w
        self._recalculate_corners()

    @property
    def height(self):
        return self._height

    @height.setter
    def height(self, h):
        self._height = h
        self._recalculate_corners()

    @property
    def zoom(self) -> float:
        return self._viewport_size.x / float(self._width)

    @zoom.setter
    def zoom(self, scale: float):
        self._width = int(self._viewport_size.x / scale)
        self._height = int(self._viewport_size.y / scale)
        self._recalculate_corners()


def translate_object(obj: Drawable, vector: Vector):
    # Grabbing
    tr = Matrix.identity(len(vector) +1)
    tr = tr.translate(vector)
    # print(tr)
    for point in obj:
        if len(point._coordinates) != len(tr):
            # project onto next axis
            point._coordinates.append(0)
        print(Matrix(Vector(*point)))
        print(tr)
        point = Point(*((tr * Matrix(point))._matrix[0]._coordinates[:-1]))


def scale_object(obj: Drawable, x: float, y: float, z: float):
    # Scaling
    for point in obj:
        point.x *= x
        point.y *= y
