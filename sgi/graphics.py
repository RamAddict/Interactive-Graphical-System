"""Higher-level graphics API."""

from typing import Tuple

from primitives import Painter, Point


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
