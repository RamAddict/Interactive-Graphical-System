"""Computer Graphics API."""

from typing import Tuple

from utilities import pairwise


class Painter():
    """Interface providing primitive graphics drawing."""

    def draw_pixel(self, x: int, y: int):
        raise NotImplementedError("Painter is an abstract class.")

    def draw_line(self, xa: int, ya: int, xb: int, yb: int):
        # Bresenham's line algorithm, which is based on a decision parameter p
        # allowing to solve y = mx + c using only integer operations {+, -, 2*}
        xa, ya, xb, yb = int(xa), int(ya), int(xb), int(yb)
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
        painter.draw_pixel(round(self._coordinates[0]),
                           round(self._coordinates[1]))

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
        painter.draw_line(round(self._points[0].x), round(self._points[0].y),
                          round(self._points[1].x), round(self._points[1].y))

    def __getitem__(self, key):
        return self._points[key]

    def __setitem__(self, key, point: Point):
        self._points[key] = point

    def __str__(self):
        return '({}; {})'.format(self[0], self[1])


class Wireframe(Drawable):
    """Polygon-like object defined by a sequence of points."""

    def __init__(self, *points: Tuple[Point]):
        self._points = list(points)

    def draw(self, painter):
        for pa, pb in pairwise(self._points + [self._points[0]]):
            painter.draw_line(round(pa.x), round(pa.y),
                              round(pb.x), round(pb.y))

    def __getitem__(self, key):
        return self._points[key]

    def __setitem__(self, key, point: Point):
        self._points[key] = point

    def __str__(self):
        return '({})'.format(
            '; '.join(str(p) for p in self._points + [self._points[0]])
        )


class Camera(Painter):
    """Window used as reference to render objects."""

    def __init__(self, viewport_width: int, viewport_height: int,
                 painter: Painter, center: Point):
        self._viewport_width = viewport_width
        self._viewport_height = viewport_height
        self.painter = painter
        self.position = center
        self.width = viewport_width
        self.height = viewport_height
        self._x_min = int(self.x - self.width/2)
        self._y_min = int(self.y - self.height/2)

    def draw_pixel(self, x: int, y: int):
        # @TODO: camera-relative transform can be optimized
        x, y = self._transform(x - self.x, y - self.y)
        self.painter.draw_pixel(x, y)

    def draw_line(self, xa: int, ya: int, xb: int, yb: int):
        xa, ya = self._transform(xa - self.x, ya - self.y)
        xb, yb = self._transform(xb - self.x, yb - self.y)
        self.painter.draw_line(xa, ya, xb, yb)

    def _transform(self, x, y) -> Tuple[int, int]:
        """Apply the Window-to-Viewport Transformation on given coordinates."""
        # equivalent to lerp(x, _x_min, x_min+width, 0, _viewport_width),
        x = (x - self._x_min) * self._viewport_width / self.width
        # _viewport_height - lerp(y, _y_min, y_min+height, 0, _viewport_height)
        y = self._viewport_height * (1 - (y - self._y_min)/self.height)
        return int(x), int(y)

    @property
    def zoom(self) -> float:
        return self._viewport_width / self.width

    @zoom.setter
    def zoom(self, scale: float):
        self.width = int(self._viewport_width / scale)
        self.height = int(self._viewport_height / scale)
        self._x_min = int(self.x - self.width/2)
        self._y_min = int(self.y - self.height/2)

    @property
    def x(self):
        return self.position.x

    @x.setter
    def x(self, x):
        self.position.x = x
        self._x_min = int(self.x - self.width/2)

    @property
    def y(self):
        return self.position.y

    @y.setter
    def y(self, y):
        self.position.y = y
        self._y_min = int(self.y - self.height/2)
