#!/usr/bin/env python3
from sys import argv
from math import inf
from typing import Optional, Callable
from PySide2.QtWidgets import QApplication, QMainWindow, QWidget
from PySide2.QtGui import QPainter, QIcon
from PySide2.QtCore import Qt

from ui.main import Ui_MainWindow
from ui.point import Ui_PointFields
from graphics import Point, Line, Wireframe, Painter, Drawable, Camera, Vector
from utilities import experp, begin, lerp, sign


class InteractiveGraphicalSystem(QMainWindow, Ui_MainWindow):
    _console = None

    @staticmethod
    def log(message):
        console = InteractiveGraphicalSystem._console
        if console:
            console.append(str(message))
        else:
            print(message)

    def __init__(self):
        # imported Qt UI setup
        super(InteractiveGraphicalSystem, self).__init__()
        self.setupUi(self)

        # viewport setup
        self.viewport = QtViewport(
            self.canvasFrame,
            self.displayFile,
            self.zoomSlider
        )
        self.canvasFrame.layout().addWidget(self.viewport)
        self.viewport.setFocus(Qt.OtherFocusReason)

        # debug console setup
        InteractiveGraphicalSystem._console = self.consoleArea
        self.log = lambda message: InteractiveGraphicalSystem.log(message)

        # setting up camera pan controls
        self.upBtn.clicked.connect(lambda: self.viewport.pan_camera(0, 1))
        self.downBtn.clicked.connect(lambda: self.viewport.pan_camera(0, -1))
        self.leftBtn.clicked.connect(lambda: self.viewport.pan_camera(-1, 0))
        self.rightBtn.clicked.connect(lambda: self.viewport.pan_camera(1, 0))

        # zoom slider setup
        def zoom_slide():
            self.viewport.update_zoom(self.zoomSlider.value(),
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
            extra.set_icon('list-add', fallback_text="+")
            extra.set_action(lambda: begin(
                extra.set_active(True),
                extra.set_icon('list-remove', fallback_text="-"),
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


class QtViewport(QWidget):
    class QtPainter(QPainter, Painter):
        """Qt-based implementation of an abstract Painter."""

        def draw_pixel(self, x, y):
            self.drawPoint(x, y)

        def draw_line(self, xa, ya, xb, yb):
            self.drawLine(xa, ya, xb, yb)

    def __init__(self, parent_widget, display_file, zoomSlider):
        super().__init__(parent_widget)
        self._display_file = display_file  # modified by main window
        self._zoomSlider = zoomSlider
        self.camera = Camera(
            QtViewport.QtPainter(),
            Point(-60, 40),
            Vector(950, 535)
        )
        self._pan = 10
        self._drag_begin = None
        self.setFocusPolicy(Qt.StrongFocus)

    def pan_camera(self, dx, dy, _normalized=True):
        """Move the camera by a certain amount of dynamically-sized steps."""
        if _normalized:
            dx = int(dx * self._pan)
            dy = int(dy * self._pan)
        self.camera.x += dx
        self.camera.y += dy
        self.update()

    def update_zoom(self, value, minimum, maximum):
        """Update zoom within a certain range."""
        zoom = experp(value, minimum, maximum, 0.1, 10)
        self.camera.zoom = zoom
        self._pan = 10 / zoom  # @NOTE: camera step is adjusted by zoom
        self.update()

    def paintEvent(self, event):
        self.camera.painter.begin(self)
        for i in range(self._display_file.count()):
            self._display_file.item(i).data(Qt.UserRole).draw(self.camera)
        self.camera.painter.end()
        return super().paintEvent(event)

    def resizeEvent(self, event):
        self.camera.width = self.width()
        self.camera.height = self.height()
        InteractiveGraphicalSystem.log(
            "Viewport resized to {}x{}.".format(self.camera.width,
                                                self.camera.height)
        )
        return super().resizeEvent(event)

    def keyPressEvent(self, e):
        # window movement
        if e.key() == Qt.Key_W:
            self.pan_camera(0, 1)
        elif e.key() == Qt.Key_A:
            self.pan_camera(-1, 0)
        elif e.key() == Qt.Key_S:
            self.pan_camera(0, -1)
        elif e.key() == Qt.Key_D:
            self.pan_camera(1, 0)
        # window zooming, @NOTE: some coupling to GUI's slider is necessary
        elif e.key() == Qt.Key_Minus and e.modifiers() & Qt.ControlModifier:
            step = self._zoomSlider.pageStep()
            self._zoomSlider.setValue(self._zoomSlider.value() - step)
        elif e.key() == Qt.Key_Equal and e.modifiers() & Qt.ControlModifier:
            step = self._zoomSlider.pageStep()
            self._zoomSlider.setValue(self._zoomSlider.value() + step)
        else:
            return super().keyPressEvent(e)

    def wheelEvent(self, event):
        # ctrl + mouse wheel also zooms
        if event.modifiers() & Qt.ControlModifier:
            step = self._zoomSlider.singleStep() * sign(event.angleDelta().y())
            self._zoomSlider.setValue(self._zoomSlider.value() + step)
        else:
            return super().wheelEvent(event)

    def focusNextPrevChild(self, next):  # disable focus change with Tab
        return False

    def mousePressEvent(self, event):
        if event.button() == Qt.MiddleButton:
            self._drag_begin = Point(event.x(), event.y())
        else:
            return super().mousePressEvent(event)

    def mouseReleaseEvent(self, event):
        if event.button() == Qt.MiddleButton:
            self._drag_begin = None
        else:
            return super().mouseReleaseEvent(event)

    def mouseMoveEvent(self, event):
        if self._drag_begin:
            # compute motion vector and update drag initial position
            delta = (event.x(), event.y()) - self._drag_begin
            self._drag_begin += delta
            # adjust delta to window size
            dx = int(lerp(delta.x, 0, self.width(), 0, self.camera.width))
            dy = int(lerp(delta.y, 0, self.height(), 0, self.camera.height))
            # move the window accordingly (scene follows mouse)
            self.pan_camera(-dx, dy, _normalized=False)
            InteractiveGraphicalSystem.log(
                "Window dragged to ({}, {})w.".format(self.camera.x,
                                                      self.camera.y)
            )
        else:
            return super().mouseMoveEvent(event)


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

    def set_icon(self, icon_name: str, fallback_text: str = ""):
        """Set the action button's icon as by the Icon Theme Specification."""

        if QIcon.hasThemeIcon(icon_name):
            self.actionButton.setIcon(QIcon.fromTheme(icon_name))
            self.actionButton.setText("")
        else:
            self.actionButton.setIcon(QIcon())
            self.actionButton.setText(fallback_text)

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
