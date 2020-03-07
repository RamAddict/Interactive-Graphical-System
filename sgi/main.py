"""@TODO: main module docstring"""

import sys
from PySide2.QtWidgets import QApplication, QMainWindow, QGraphicsView
from PySide2.QtGui import QPainter
from PySide2.QtCore import (QCoreApplication, QMetaObject, QObject, QPoint,
    QRect, QSize, QUrl, Qt)

from gui import Ui_MainWindow
from graphics import *


class MyPainter(Painter):
    def __init__(self, widget):
        self.painter = QPainter(widget)

    def draw_pixel(self, x, y):
        self.painter.drawPoint(x, y)

    def draw_line(self, x1, y1, x2, y2):
        self.painter.drawLine(x1, y1, x2, y2)

class MyGraphicsView(QGraphicsView):
    def __init__(self, widget, objects):
        QGraphicsView.__init__(self, widget)
        self.objects = objects

    def paintEvent(self, event):
        painter = MyPainter(self.viewport())
        for name, obj in self.objects.items():
            obj.draw(painter)

class InteractiveGraphicalSystem(QMainWindow, Ui_MainWindow):
    """@TODO: SGI class docstring"""

    def __init__(self):
        super(InteractiveGraphicalSystem, self).__init__()

        self.objects = {'line': Line(Point(500, 500), Point(700, 500)),
                        'point': Point(250, 250),
                        'wireframe': Wireframe(Point(0, 0), Point(300, 0), Point(300, 400))}

        self.setupUi(self)
        self.view_port = MyGraphicsView(self.centralwidget, self.objects)
        self.view_port.setObjectName(u"view_port")
        self.view_port.setGeometry(QRect(10, 10, 581, 391))
        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    gui = InteractiveGraphicalSystem()
    sys.exit(app.exec_())
