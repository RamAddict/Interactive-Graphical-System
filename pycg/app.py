#!/usr/bin/env python3
from sys import argv
from math import inf
from PySide2.QtWidgets import QApplication, QMainWindow, QWidget, QListWidget
from PySide2.QtGui import QPainter
from PySide2.QtCore import Qt

from ui.main import Ui_MainWindow
from ui.point import Ui_PointFields
from graphics import Point, Line, Wireframe, Painter, Drawable, Camera
from utilities import experp


class InteractiveGraphicalSystem(QMainWindow, Ui_MainWindow):
    _console = None

    def log(message: str):
        if InteractiveGraphicalSystem._console:
            InteractiveGraphicalSystem._console.append(message)
        else:
            print(message)

    def __init__(self):
        # imported Qt UI setup
        super(InteractiveGraphicalSystem, self).__init__()
        self.setupUi(self)

        # viewport setup
        self.viewport = QtViewport(self.canvasFrame, self.displayFile,
                                   Camera(950, 535, QtPainter(), Point(0, 0)))
        self.viewport.setGeometry(0, 0, 950, 535)

        # static console setup
        InteractiveGraphicalSystem._console = self.consoleArea

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

        # setting up scene controls
        self.removeButton.clicked.connect(
            lambda: self.remove_object(self.displayFile.currentRow())
        )
        self.upListButton.clicked.connect(
            lambda: self.move_object(self.displayFile.currentRow(), -1)
        )
        self.downListButton.clicked.connect(
            lambda: self.move_object(self.displayFile.currentRow(), 1)
        )

        # @TODO: new object dialogue
        # self.newButton
        # self.editButton
        # self.nameEdit
        self.typeBox.currentIndexChanged.connect(lambda shape: print(shape))
        # self.dialogBox
        # self.objectArea / self.formLayout
        self.formLayout.addRow(PointFields())

        # render it all
        self.show()
        InteractiveGraphicalSystem.log(
            "Interactive Graphical System initialized."
        )

    def pan_camera(self, dx, dy):
        self.viewport.camera.x += dx
        self.viewport.camera.y += dy
        self.viewport.update()

    def update_zoom(self, value, minimum=0, maximum=1.0):
        zoom = experp(value, minimum, maximum, 0.1, 10)
        self.viewport.camera.zoom = zoom
        self._pan = int(10 / zoom)
        self.viewport.update()

    def add_object(self, obj: Drawable, name: str, index: int = None) -> int:
        """Adds an object to the Display File, returning its position."""

        n = self.displayFile.count()
        if index and (index < 0 or index > n):
            raise IndexError("Invalid Display File index: %d" & index)
        elif index is None:
            index = n

        self.displayFile.insertItem(index, name)  # @FIXME: name conflicts
        self.displayFile.item(index).setData(Qt.UserRole, obj)
        InteractiveGraphicalSystem.log(
            "Added %s '%s' to Display File." % (type(obj).__name__, name)
        )
        self.displayFile.setCurrentRow(index)
        self.viewport.update()
        return index

    def remove_object(self, index: int) -> object:
        item = self.displayFile.takeItem(index)
        if item:
            InteractiveGraphicalSystem.log(
                "Removed '%s' from Display File." % item.text()
            )
            self.viewport.update()
            item = item.data(Qt.UserRole)
        return item

    def move_object(self, current: int, offset: int):
        pos = current + offset
        if pos < 0 or pos >= self.displayFile.count():
            return
        self.displayFile.insertItem(pos, self.displayFile.takeItem(current))
        self.displayFile.setCurrentRow(pos)
        self.viewport.update()


class QtPainter(QPainter, Painter):
    """Qt-based implementation of an abstract Painter."""

    def draw_pixel(self, x: int, y: int):
        self.drawPoint(x, y)

    def draw_line(self, xa: int, ya: int, xb: int, yb: int):
        self.drawLine(xa, ya, xb, yb)


class QtViewport(QWidget):
    def __init__(self, parent, objects: QListWidget, _qt_cam: Camera):
        super().__init__(parent)
        self.display_file = objects
        self.camera = _qt_cam

    def paintEvent(self, event):
        self.camera.painter.begin(self)
        for i in range(self.display_file.count()):
            self.display_file.item(i).data(Qt.UserRole).draw(self.camera)
        self.camera.painter.end()


class PointFields(QWidget, Ui_PointFields):
    def __init__(self):
        super(PointFields, self).__init__()
        self.setupUi(self)
        self.xDoubleSpinBox.setRange(-inf, inf)
        self.yDoubleSpinBox.setRange(-inf, inf)


if __name__ == '__main__':
    app = QApplication(argv)

    gui = InteractiveGraphicalSystem()  # gui variable is needed
    gui.add_object(Point(250, 250), "p0")
    gui.add_object(Line(Point(500, 500), Point(700, 500)), "lh")
    gui.add_object(Wireframe(Point(300, 400),  # ->    /|
                             Point(300, 0),    # -v   / |
                             Point(0, 0)),     # ->  *---
                   "tr")
    gui.add_object(Line(Point(600, 400), Point(600, 600)), "lv")

    exit(app.exec_())
