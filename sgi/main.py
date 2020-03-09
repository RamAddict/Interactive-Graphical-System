#!/usr/bin/env python

import sys
from typing import Dict
from PySide2.QtWidgets import QApplication, QMainWindow, QWidget, QTextBrowser
from PySide2.QtGui import QPainter

from gui import Ui_MainWindow
from primitives import Point, Line, Wireframe, Painter, Drawable
from graphics import Camera
from util import experp


class InteractiveGraphicalSystem(QMainWindow, Ui_MainWindow):
    def __init__(self):
        # imported Qt UI setup
        super(InteractiveGraphicalSystem, self).__init__()
        self.setupUi(self)

        self.display_file: Dict[str, Drawable] = {}

        # viewport setup
        self.viewport = QtViewport(self.centralwidget, self.display_file,
                                   Camera(960, 540, QtPainter(), Point(0, 0)))
        self.viewport.setObjectName(u"viewport")
        self.viewport.setGeometry(10, 10, 960, 540)

        # console setup
        self.console = QTextBrowser(self.centralwidget)
        self.console.setObjectName(u"console")
        self.console.setGeometry(10, 560, 960, 150)

        # setting up camera pan controls
        self._pan: int = 10  # @NOTE: camera step is adjusted by zoom
        self.upButton.clicked.connect(lambda: self.pan_camera(0, self._pan))
        self.downButton.clicked.connect(lambda: self.pan_camera(0, -self._pan))
        self.leftButton.clicked.connect(lambda: self.pan_camera(-self._pan, 0))
        self.rightButton.clicked.connect(lambda: self.pan_camera(self._pan, 0))

        # zoom slider setup
        self.zoomSlider.valueChanged.connect(
            lambda: self.update_zoom(self.zoomSlider.value(),
                                     self.zoomSlider.minimum(),
                                     self.zoomSlider.maximum())
        )
        self.update_zoom(self.zoomSlider.value(),
                         self.zoomSlider.minimum(), self.zoomSlider.maximum())

        # render it all
        self.show()
        self.log("Interactive Graphical System initialized.")

    def pan_camera(self, dx, dy):
        self.viewport.camera.x += dx
        self.viewport.camera.y += dy
        self.viewport.update()

    def update_zoom(self, value, minimum=0, maximum=1.0):
        zoom = experp(value, minimum, maximum, 0.1, 10)
        self.viewport.camera.zoom = zoom
        self._pan = int(10 / zoom)
        self.viewport.update()

    def log(self, message: str):
        self.console.append(message)

    def add_object(self, obj: Drawable, name: str):
        self.display_file[name] = obj
        self.objectList.addItem(name)
        self.log("%s '%s' added to display file." % (type(obj).__name__, name))


class QtPainter(QPainter, Painter):
    """Qt-based implementation of an abstract Painter."""

    def draw_pixel(self, x: int, y: int):
        self.drawPoint(x, y)

    def draw_line(self, xa: int, ya: int, xb: int, yb: int):
        self.drawLine(xa, ya, xb, yb)


class QtViewport(QWidget):
    def __init__(self, parent, objects: Dict[str, Drawable], _qt_cam: Camera):
        QWidget.__init__(self, parent)
        self.objects = objects
        self.camera = _qt_cam

    def paintEvent(self, event):
        self.camera.painter.begin(self)
        for obj in self.objects.values():
            obj.draw(self.camera)
        self.camera.painter.end()


if __name__ == '__main__':
    app = QApplication(sys.argv)

    gui = InteractiveGraphicalSystem()  # gui variable is needed
    gui.add_object(Point(250, 250), "p0")
    gui.add_object(Line(Point(500, 500), Point(700, 500)), "lh")
    gui.add_object(Wireframe(Point(300, 400),  # ->    /|
                             Point(300, 0),    # -v   / |
                             Point(0, 0)),     # ->  *---
                   "tr")
    gui.add_object(Line(Point(600, 400), Point(600, 600)), "lv")

    sys.exit(app.exec_())
