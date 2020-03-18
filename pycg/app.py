#!/usr/bin/env python3
from sys import argv
from math import inf
from typing import Optional, Callable
from PySide2.QtWidgets import QApplication, QMainWindow, QWidget, QListWidget
from PySide2.QtGui import QPainter, QIcon
from PySide2.QtCore import Qt

from ui.main import Ui_MainWindow
from ui.point import Ui_PointFields
from graphics import Point, Line, Wireframe, Painter, Drawable, Camera, Vector
from utilities import experp, begin


class InteractiveGraphicalSystem(QMainWindow, Ui_MainWindow):
    _console = None

    @staticmethod
    def log(message):
        if InteractiveGraphicalSystem._console:
            InteractiveGraphicalSystem._console.append(str(message))
        else:
            print(message)

    def __init__(self):
        # imported Qt UI setup
        super(InteractiveGraphicalSystem, self).__init__()
        self.setupUi(self)

        # viewport setup
        self.viewport = QtViewport(self.canvasFrame, self.displayFile)
        self.canvasFrame.layout().addWidget(self.viewport)

        # debug console setup
        InteractiveGraphicalSystem._console = self.consoleArea
        self.log = lambda message: InteractiveGraphicalSystem.log(message)

        # setting up camera pan controls
        self._pan: int = 10
        self.upButton.clicked.connect(lambda: self.pan_camera(0, self._pan))
        self.downButton.clicked.connect(lambda: self.pan_camera(0, -self._pan))
        self.leftButton.clicked.connect(lambda: self.pan_camera(-self._pan, 0))
        self.rightButton.clicked.connect(lambda: self.pan_camera(self._pan, 0))

        # zoom slider setup
        def zoom_slide():
            self.update_zoom(self.zoomSlider.value(),
                             self.zoomSlider.minimum(),
                             self.zoomSlider.maximum())
        self.zoomSlider.valueChanged.connect(zoom_slide)
        zoom_slide()

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
        self.newButton.clicked.connect(
            lambda: begin(self.objectLabel.show(), self.objectArea.show())
        )
        # @TODO: edit selected object
        self.editButton.setEnabled(False)

        def new_type_select(index: int):
            # clean all fields after 'name' and 'type'
            while self.formLayout.rowCount() > 2:
                self.formLayout.removeRow(2)

            typename = self.typeBox.itemText(index)
            if typename == 'Point':
                self.formLayout.addRow(PointFields())
            elif typename == 'Line':
                self.formLayout.addRow(PointFields())
                self.formLayout.addRow(PointFields())
            elif typename == 'Wireframe':
                self.formLayout.addRow(PointFields())
                self.formLayout.addRow(PointFields())
                self.formLayout.addRow(PointFields())
                self.formLayout.addRow(make_extra_point())

        def make_extra_point() -> PointFields:
            extra = PointFields()
            extra.set_active(False)
            extra.set_icon('list-add')
            extra.set_action(lambda: begin(
                extra.set_active(True),
                extra.set_icon('list-remove'),
                extra.set_action(lambda: self.formLayout.removeRow(extra)),
                self.formLayout.addRow(make_extra_point())
            ))
            return extra

        def new_object() -> Optional[Drawable]:
            # @TODO: improve parameter validation (name conflict, valid fields)
            if self.typeBox.currentIndex() < 0:
                return

            name = self.nameEdit.text()
            typename = self.typeBox.currentText()

            # QLayout.itemAt on a QFormLayout -> label, field: QLayoutItem
            obj = None
            if typename == 'Point':
                obj = self.formLayout.itemAt(4).widget().to_point()
            elif typename == 'Line':
                pa = self.formLayout.itemAt(4).widget().to_point()
                pb = self.formLayout.itemAt(5).widget().to_point()
                obj = Line(pa, pb)
            elif typename == 'Wireframe':
                points = []
                for i in range(4, self.formLayout.count() - 1):
                    p = self.formLayout.itemAt(i).widget().to_point()
                    points.append(p)
                obj = Wireframe(*points)

            gui.add_object(obj, name, self.displayFile.currentRow() + 1)
            finish_object()

        def finish_object():
            self.objectLabel.hide()
            self.typeBox.setCurrentIndex(-1)
            self.nameEdit.setText("")
            self.objectArea.hide()

        self.typeBox.currentIndexChanged.connect(new_type_select)
        self.dialogBox.accepted.connect(new_object)
        self.dialogBox.rejected.connect(finish_object)
        finish_object()

        # render it all
        self.show()
        self.log("Interactive Graphical System initialized.")

    def pan_camera(self, dx, dy):
        self.viewport.camera.x += dx
        self.viewport.camera.y += dy
        self.viewport.update()

    def update_zoom(self, value, minimum, maximum):
        zoom = experp(value, minimum, maximum, 0.1, 10)
        self.viewport.camera.zoom = zoom
        self._pan = int(10 / zoom)  # @NOTE: camera step is adjusted by zoom
        self.viewport.update()

    def add_object(self, obj: Drawable, name: str, index: int = None) -> int:
        """Add an object to the Display File, returning its position."""

        n = self.displayFile.count()
        if index and (index < 0 or index > n):
            raise IndexError("Invalid Display File index: %d" & index)
        elif index is None:
            index = n

        self.displayFile.insertItem(index, name)
        self.displayFile.item(index).setData(Qt.UserRole, obj)
        self.log("Added %s '%s' to Display File." % (type(obj).__name__, name))
        self.displayFile.setCurrentRow(index)
        self.viewport.update()
        return index

    def remove_object(self, index: int) -> object:
        """Take an object out from a certain index in the Display File."""
        item = self.displayFile.takeItem(index)
        if item:
            self.log("Removed '%s' from Display File." % item.text())
            self.viewport.update()
            item = item.data(Qt.UserRole)
        return item

    def move_object(self, position: int, offset: int):
        """Offset an object's position in the Display File."""
        pos = position + offset
        if pos < 0 or pos >= self.displayFile.count():
            return
        self.displayFile.insertItem(pos, self.displayFile.takeItem(position))
        self.displayFile.setCurrentRow(pos)
        self.viewport.update()


class QtPainter(QPainter, Painter):
    """Qt-based implementation of an abstract Painter."""

    def draw_pixel(self, x, y):
        self.drawPoint(x, y)

    def draw_line(self, xa, ya, xb, yb):
        self.drawLine(xa, ya, xb, yb)


class QtViewport(QWidget):
    def __init__(self, parent, objects: QListWidget):
        super().__init__(parent)
        self._display_file = objects
        self._size = Vector(950, 535)
        self.camera = Camera(QtPainter(), Point(-60, 40), self._size)

    def paintEvent(self, event):
        self.camera.painter.begin(self)
        for i in range(self._display_file.count()):
            self._display_file.item(i).data(Qt.UserRole).draw(self.camera)
        self.camera.painter.end()
        return super().paintEvent(event)

    def resizeEvent(self, event):
        InteractiveGraphicalSystem.log(
            "Viewport resized to {}x{}".format(self.width(), self.height())
        )
        self._size.x = self.width()
        self._size.y = self.height()
        return super().resizeEvent(event)


class PointFields(QWidget, Ui_PointFields):
    def __init__(self):
        super(PointFields, self).__init__()
        self.setupUi(self)
        self.xDoubleSpinBox.setRange(-inf, inf)
        self.yDoubleSpinBox.setRange(-inf, inf)
        self._has_action = False

    def to_point(self) -> Point:
        return Point(int(self.xDoubleSpinBox.value()),
                     int(self.yDoubleSpinBox.value()))

    def set_action(self, action: Optional[Callable[[], None]]):
        """Set procedure to be executed when the action button is clicked."""

        # @NOTE: multiple receivers must be disconnect()ed from a signal
        if self._has_action:
            self.actionButton.clicked.disconnect()
            self._has_action = False

        if action:
            self.actionButton.clicked.connect(action)
            self._has_action = True
            self.actionButton.setEnabled(True)
        else:
            self.actionButton.setEnabled(False)

    def set_icon(self, icon_name: str):
        """Set the action button's icon as by the Icon Theme Specification."""
        icon = QIcon()
        if QIcon.hasThemeIcon(icon_name):
            icon = QIcon.fromTheme(icon_name)
        self.actionButton.setIcon(icon)

    def set_active(self, active: bool):
        """Set whether or not the fields are enabled."""
        self.xDoubleSpinBox.setEnabled(active)
        self.yDoubleSpinBox.setEnabled(active)


if __name__ == '__main__':
    app = QApplication(argv)

    gui = InteractiveGraphicalSystem()  # @NOTE: variable is needed

    gui.add_object(Line(Point(-950, 0), Point(1605, 3)), "lhor")
    gui.add_object(Wireframe(Point(100, 0),
                             Point(475, 250),
                             Point(300, 133),
                             Point(478, 75),
                             Point(696, 134),
                             Point(475, 250),
                             Point(950, 0)),
                   "wmmc")
    gui.add_object(Line(Point(220, 75), Point(80, 135)), "lve")
    gui.add_object(Line(Point(80, 135), Point(-40, 83)), "lvw")
    gui.add_object(Wireframe(Point(-575, 0),
                             Point(-475, 135),
                             Point(-220, 152),
                             Point(-130, 300),
                             Point(0, 0)),
                   "wmt")
    gui.add_object(Point(-130, 297), "ppmt")
    gui.add_object(Line(Point(-237, 72), Point(-118, -253)), "lar")
    gui.add_object(Line(Point(-237, 72), Point(-356, -253)), "lal")
    gui.add_object(Line(Point(-336, -103), Point(-138, -103)), "lab")

    exit(app.exec_())
