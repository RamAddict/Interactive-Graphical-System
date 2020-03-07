"""@TODO: main module docstring"""

import sys
from PySide2.QtWidgets import QApplication, QMainWindow
from PySide2.QtGui import QPainter

from .gui import Ui_MainWindow
from .graphics import *


class MyPainter(Painter):
    def __init__(self, widget):
        self.painter = QPainter(widget)

    def draw_pixel(self, x, y):
        self.painter.drawPoint(x, y)

    def draw_line(self, x1, y1, x2, y2):
        self.painter.drawLine(x1, y1, x2, y2)


class InteractiveGraphicalSystem(QMainWindow, Ui_MainWindow):
    """@TODO: SGI class docstring"""

    def __init__(self):
        super(InteractiveGraphicalSystem, self).__init__()
        self.setupUi(self)
        self.show()

        self.objects = {'line': Line(Point(500, 500), Point(700, 500)),
                        'point': Point(250, 250),
                        'wireframe': Wireframe(Point(0, 0), Point(300, 0), Point(300, 400))}

    def paintEvent(self, event):
        painter = MyPainter(self)
        for name, obj in self.objects.items():
            obj.draw(painter)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    gui = InteractiveGraphicalSystem()
    sys.exit(app.exec_())
