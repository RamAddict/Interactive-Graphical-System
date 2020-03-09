"""Higher-level graphics API."""

from typing import Tuple

from primitives import Painter, Point


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

    def draw_line(self, xa, ya, xb, yb):
        xa, ya = self._transform(xa - self.x, ya - self.y)
        xb, yb = self._transform(xb - self.x, yb - self.y)
        self.painter.draw_line(xa, ya, xb, yb)

    def _transform(self, x, y) -> Tuple:
        """Apply the Window-to-Viewport Transformation on given coordinates."""
        # x: equivalent to lerp(x, x_min, x_min+width, 0, _viewport_width)
        x_min = self.x - self.width/2
        x = (x - x_min) * self._viewport_width / self.width
        # _viewport_height - lerp(y, y_min, y_min+height, 0, _viewport_height)
        y_min = self.y - self.height/2
        y = self._viewport_height * (1 - (y - y_min)/self.height)
        return x, y

    @property
    def zoom(self):
        return self._viewport_width / self.width

    @zoom.setter
    def zoom(self, scale: float):
        self.width = self._viewport_width / scale
        self.height = self._viewport_height / scale

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
