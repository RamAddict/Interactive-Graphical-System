#!/usr/bin/env python3

from math import inf, radians
from sys import argv
from os import path
from typing import Optional, Callable, Dict, Sequence, Tuple
from ast import literal_eval, parse

from PySide2.QtWidgets import (QApplication, QMainWindow, QWidget, QDialog,
                               QColorDialog, QFileDialog, QMessageBox, QInputDialog,
                               QDialogButtonBox)
from PySide2.QtGui import (QPainter, QKeySequence, QColor, QPalette, QIcon,
                           QPixmap, QPolygon)
from PySide2.QtCore import Qt, QPoint

from blas import Vector
from graphics import (BSpline, Painter, Camera, Transformation, Drawable, Point, Line,
                      Linestring, Polygon, Color, Bezier)
from utilities import experp, begin, sign, to_float, lerp
import obj as wavefront_obj
from ui.main import Ui_MainWindow
from ui.settings import Ui_SettingsDialog


class InteractiveGraphicalSystem(QMainWindow, Ui_MainWindow):
    _console = None

    @staticmethod
    def log(message: str):
        console = InteractiveGraphicalSystem._console
        if console:
            console.append(str(message))
        else:
            print(message)

    def __init__(self, *args, **kwargs):
        # imported Qt UI setup
        QMainWindow.__init__(self, *args, **kwargs)
        self.setupUi(self)

        self.display_file: Dict[str, Drawable] = dict()

        # viewport setup
        self.viewport = QtViewport(self.canvasFrame,
                                   self.display_file,
                                   self.zoomSlider,
                                   self.mousePositionLabel)
        self.canvasFrame.layout().addWidget(self.viewport)
        self.viewport.setFocus(Qt.OtherFocusReason)

        # debug console setup
        InteractiveGraphicalSystem._console = self.consoleArea
        self.log = lambda message: InteractiveGraphicalSystem.log(message)

        # setting up camera controls
        self.upBtn.clicked.connect(lambda: self.viewport.pan_camera(0, 1))
        self.downBtn.clicked.connect(lambda: self.viewport.pan_camera(0, -1))
        self.leftBtn.clicked.connect(lambda: self.viewport.pan_camera(-1, 0))
        self.rightBtn.clicked.connect(lambda: self.viewport.pan_camera(1, 0))
        self.rollLeftBtn.clicked.connect(lambda: self.viewport.tilt_view(1, Camera.ROLL))
        self.rollRightBtn.clicked.connect(lambda: self.viewport.tilt_view(-1, Camera.ROLL))
        self.pitchUpBtn.clicked.connect(lambda: self.viewport.tilt_view(1, Camera.PITCH))
        self.pitchDownBtn.clicked.connect(lambda: self.viewport.tilt_view(-1, Camera.PITCH))
        self.yawLeftBtn.clicked.connect(lambda: self.viewport.tilt_view(1, Camera.YAW))
        self.yawRightBtn.clicked.connect(lambda: self.viewport.tilt_view(-1, Camera.YAW))

        # zoom slider setup
        self.zoomSlider.valueChanged.connect(
            lambda _: self.viewport.update_zoom(self.zoomSlider.value(),
                                                self.zoomSlider.minimum(),
                                                self.zoomSlider.maximum()))
        self.zoomSlider.valueChanged.emit(None)

        # setting up scene controls
        self.removeButton.clicked.connect(lambda: self.remove_object(self.displayFile.currentRow()))
        self.upListButton.clicked.connect(lambda: self.move_object(self.displayFile.currentRow(), -1))
        self.downListButton.clicked.connect(lambda: self.move_object(self.displayFile.currentRow(), 1))
        self.newButton.clicked.connect(lambda: begin(
            self.typeBox.setCurrentIndex(-1),
            self.nameEdit.setText(""),
            self.componentWidget.setCurrentWidget(self.objectPage),
        ))
        self._delayed_transformations = []
        self.transformButton.clicked.connect(  # ensures something is selected
            lambda: None if self.displayFile.currentRow() < 0
            else begin(
                self._delayed_transformations.clear(),
                self.transformList.clear(),
                self.translateInput.setText("(0, 0, 0)"),
                self.scaleInput.setText("(1, 1, 1)"),
                self.angleInput.setText("0.0"),
                self.axisInput.setText("(0, 0, 1)"),
                self.pivotSelect.setCurrentIndex(0),
                self.componentWidget.setCurrentWidget(self.transformPage),
            )
        )

        def handle_save_action(all: bool = False):
            if not all and self.displayFile.currentRow() < 0:
                QMessageBox.question(
                    self,
                    "Message",
                    "Please select an object before saving",
                    QMessageBox.Ok
                )
            else:
                name = "world" if all else self.displayFile.currentItem().text()

                modelpath, _ = QFileDialog.getSaveFileName(
                    self,
                    "Select .obj file to save",
                    name + '.obj',
                )
                if modelpath.strip() == '': return

                mtlpath, _ = QFileDialog.getSaveFileName(
                    self,
                    "Select .mtl file to save",
                    name + '.mtl',
                )
                if mtlpath.strip() == '': return

                models = self.display_file if all else {name: self.display_file[name]}

                with open(mtlpath, 'w+') as file:
                    for name, model in models.items():
                        color = model.color
                        mtl = model.attributes.get('usemtl', f"{name}_color")
                        file.write(f"newmtl {mtl}\n")
                        file.write(f"Kd {color.r/255} {color.g/255} {color.b/255}\n")
                        self.log(f"Saved material '{mtl}' to '{path.relpath(mtlpath)}'")

                with wavefront_obj.open(
                    modelpath,
                    'w+',
                    mtllib=path.basename(mtlpath),
                ) as file:
                    for name, model in models.items():
                        mtl = model.attributes.get('usemtl', f"{name}_color")
                        file.write(model, name, usemtl=mtl)
                        self.log(f"Saved object '{name}' to '{path.relpath(modelpath)}'")

        def handle_settings_action():
            dialog = SettingsDialog(self)
            cs = self.viewport.camera.line_clipping_algorithm == SettingsDialog.CLIP_CS
            dialog.clipLBButton.setChecked(not cs)
            dialog.clipCSButton.setChecked(cs)
            status = dialog.exec_()
            if status != QDialog.Accepted: return
            algo = (SettingsDialog.CLIP_CS if dialog.clipCSButton.isChecked()
                    else SettingsDialog.CLIP_LB)
            self.viewport.camera.line_clipping_algorithm = algo
            self.log(f"Settings: line clipping algorithm set to '{algo}'.")

        # setting up toolbar actions
        self.toolBar.setContextMenuPolicy(Qt.PreventContextMenu)
        self.actionSave.triggered.connect(lambda: handle_save_action(all=False))
        self.actionSave.setShortcut(QKeySequence.Save)
        self.actionSaveAll.triggered.connect(lambda: handle_save_action(all=True))
        self.actionSaveAll.setShortcut(QKeySequence.SaveAs)
        self.actionLoad.triggered.connect(lambda: self.load_obj())
        self.actionLoad.setShortcut(QKeySequence.Open)
        self.actionSettings.triggered.connect(handle_settings_action)
        self.actionSettings.setShortcut(QKeySequence.Preferences)

        def new_object():
            if self.typeBox.currentIndex() < 0: return

            name = self.nameEdit.text()
            typename = self.typeBox.currentText()
            color = QColor(self.colorEdit.text())
            color = Color(color.red(), color.green(), color.blue())

            text = self.pointsText.toPlainText().replace("\n", " ")
            parsed = literal_eval(text)
            if not isinstance(parsed, tuple): return

            obj = None
            if typename == 'Point' and len(parsed) >= 2 and isinstance(parsed[0], (int, float)):
                obj = Point(*parsed)
            elif typename == 'Line' and len(parsed) == 2 and isinstance(parsed[0], tuple):
                a, b = parsed
                obj = Line(Point(*a), Point(*b))
            elif typename == 'Linestring' and len(parsed) > 2:
                obj = Linestring([Point(*p) for p in parsed])
            elif typename == 'Polygon' and len(parsed) > 2:
                obj = Polygon([Point(*p) for p in parsed])
            elif typename == 'Bezier' and len(parsed) >= 4 and len(parsed) % 3 == 1:
                obj = Bezier([Point(*p) for p in parsed])
            elif typename == 'BSpline' and len(parsed) >= 4:
                obj = BSpline([Point(*p) for p in parsed])
            else:
                return

            self.insert_object(obj, name,
                               index=self.displayFile.currentRow() + 1,
                               color=color)
            self.componentWidget.setCurrentWidget(self.emptyPage)

        def pick_color(override: str = None):
            color = QColor(override) if override else \
                    QColorDialog.getColor(initial=QColor(self.colorEdit.text()))
            self.colorEdit.setText(color.name())
            pixmap = QPixmap(100, 100)
            pixmap.fill(color)
            self.colorEdit.setIcon(QIcon(pixmap))

        # object page controls
        self.typeBox.currentIndexChanged.connect(lambda _: self.pointsText.clear())
        self.colorEdit.clicked.connect(pick_color)
        pick_color(QPalette().color(QPalette.Foreground).name())
        self.dialogBox.accepted.connect(new_object)
        self.dialogBox.rejected.connect(
            lambda: self.componentWidget.setCurrentWidget(self.emptyPage))

        def do_transformations():
            if not self._delayed_transformations: return
            name = self.displayFile.currentItem().text()
            drawable = self.display_file[name]
            result = Transformation().matrix()  # <- identity
            for transformation, pivot, axis in reversed(self._delayed_transformations):
                pivot = pivot or drawable.center()
                matrix = transformation.matrix(pivot, axis)
                result = result @ matrix
            drawable.transform(result)
            self.viewport.update()
            self.log("Applied transformation\n" + str(result))

        def add_transformation():
            def parse_tuple3(text):
                parsed = literal_eval(text)
                if not isinstance(parsed, tuple):
                    return None
                elif len(parsed) != 3 or not isinstance(parsed[0], (int, float)):
                    return None
                else:
                    return float(parsed[0]), float(parsed[1]), float(parsed[2])

            tx, ty, tz = parse_tuple3(self.translateInput.text())
            sx, sy, sz = parse_tuple3(self.scaleInput.text())
            theta = radians(to_float(self.angleInput.text()))
            rx, ry, rz = parse_tuple3(self.axisInput.text())
            axis = Vector(rx, ry, rz).normalized()

            pivot = None
            if self.pivotSelect.currentText() == 'Origin':
                pivot = Point(0, 0, 0)
            elif self.pivotSelect.currentText() == 'Custom':
                pivot = Point(*parse_tuple3(self.customInput.text()))

            transform = Transformation().translate(tx, ty, tz).rotate(theta).scale(sx, sy, sz)
            self._delayed_transformations.append((transform, pivot, axis))
            self.transformList.addItem(
                f"{{\n  T({tx}, {ty}, {tz});\n  R({theta}, ({axis.x}, {axis.y}, {axis.z}));\n  S({sx},{sy},{sz});\n}}")

            self.translateInput.setText("(0, 0, 0)")
            self.scaleInput.setText("(1, 1, 1)")
            self.angleInput.setText("0.0")
            self.axisInput.setText("(0, 0, 1)")

        # transformation page setup
        self.pivotSelect.currentIndexChanged.connect(lambda:
            self.customInput.setEnabled(self.pivotSelect.currentText() == 'Custom')
        )
        self.transformAddButton.clicked.connect(add_transformation)
        self.transformList.itemDoubleClicked.connect(lambda item: begin(
            self._delayed_transformations.pop(self.transformList.indexFromItem(item).row()),
            self.transformList.takeItem(self.transformList.indexFromItem(item).row()),
        ))
        self.transformApplyButtons.button(QDialogButtonBox.Apply) \
                                  .clicked.connect(do_transformations)
        self.transformApplyButtons.rejected.connect(
            lambda: self.componentWidget.setCurrentWidget(self.emptyPage))

        # render it all
        self.show()
        self.log("Interactive Graphical System initialized.")

    def insert_object(self, obj: Drawable, name: str,
                      index: int = None, color: Color = None, **kwargs) -> int:
        """Put an object in the Display File, returning its position."""

        n = self.displayFile.count()
        if index and (index < 0 or index > n):
            raise IndexError("Invalid Display File index", index)
        elif index is None:
            index = n

        # when names collide, add a counter (eg name, name1, name2, ...)
        while name in self.display_file:
            self.consoleArea.append(f"Renaming '{name}' on collision.")
            prefix = name.rstrip('0123456789')
            suffix = name[len(prefix):] if len(prefix) < len(name) else '0'
            count = int(suffix) + 1
            name = prefix + str(count)
        self.display_file[name] = obj

        if not color:
            color = QPalette().color(QPalette.Foreground)
            color = Color(color.red(), color.green(), color.blue())
        obj.color = color
        obj.attributes = kwargs
        obj.attributes['name'] = name
        obj.attributes['color'] = color

        self.displayFile.insertItem(index, name)
        self.log(f"Added {type(obj).__name__} '{name}' to Display File.")
        self.displayFile.setCurrentRow(index)
        self.componentWidget.setCurrentWidget(self.emptyPage)
        self.viewport.update()
        return index

    def remove_object(self, index: int) -> Optional[Drawable]:
        """Take an object out from a certain index in the Display File."""
        item = self.displayFile.takeItem(index)
        if not item:
            return None
        else:
            name = item.text()
            model = self.display_file.pop(name)
            self.log(f"Removed '{name}' from Display File.")
            self.viewport.update()
            return model

    def move_object(self, position: int, offset: int):
        """Offset an object's position in the Display File."""
        pos = position + offset
        if pos < 0 or pos >= self.displayFile.count():
            return
        self.displayFile.insertItem(pos, self.displayFile.takeItem(position))
        self.displayFile.setCurrentRow(pos)
        self.viewport.update()

    def load_obj(self, path: str = None):
        """Loads drawable objects from target OBJ file in disk."""
        path = path or QFileDialog.getOpenFileName(self, "Select .obj file to load")[0]
        if path.strip() != '':
            with wavefront_obj.open(path, 'r') as file:
                for model, attributes in file:
                    self.insert_object(model, **attributes)


class QtViewport(QWidget):
    def __init__(self, parent_widget, display_file, zoom_slider, eye_position):
        class QtPainter(QPainter, Painter):
            """Qt-based implementation of an abstract Painter."""

            def draw_pixel(self, x, y):
                self.drawPoint(x, y)

            def draw_line(self, xa, ya, xb, yb):
                self.drawLine(xa, ya, xb, yb)

            def draw_polygon(self, points):
                self.drawPolygon(QPolygon([QPoint(x, y) for x, y in points]))

        super().__init__(parent_widget)
        self._display_file = display_file  # modified by main window
        self._zoom_slider = zoom_slider
        self._eye_position = eye_position
        size = Vector(self.width() - 80, self.height() - 80)
        self.camera = Camera(QtPainter(), size, Point(40, 40))
        self._pan = 10
        self._drag_begin = None
        self._rotate_begin = None
        self.setFocusPolicy(Qt.StrongFocus)
        self.setMouseTracking(True)

    def pan_camera(self, dx, dy, _normalized=True):
        """Move the camera by a certain amount of dynamically-sized steps.
        Takes the camera tilt into account, such that movement is view-aligned.
        """
        if _normalized:
            dx *= self._pan
            dy *= self._pan
        delta = self.camera.view_right * dx + self.camera.view_up * dy
        self.camera.x += delta.x
        self.camera.y += delta.y
        self.update()

    def update_zoom(self, value, minimum, maximum):
        """Update zoom within a certain range."""
        zoom = experp(value, minimum, maximum, 0.1, 10)
        self.camera.zoom = zoom
        self._pan = 10 / zoom  # NOTE: camera step is adjusted by zoom
        self.update()

    def tilt_view(self, theta: float, axis = Camera.ROLL, _normalized=True):
        """Tilt the camera view by the given amount."""
        self.camera.rotate(theta * radians(15), axis)
        self.update()

    def paintEvent(self, event):  # this is where we draw our scene
        w, h = self.width(), self.height()
        painter = self.camera.painter
        painter.begin(self)
        painter.setRenderHint(QPainter.Antialiasing, False)
        painter.setRenderHint(QPainter.SmoothPixmapTransform, False)

        painter.setPen(QPalette().color(QPalette.Highlight))
        painter.drawRect(40, 40, w - 80, h-80)

        for drawable in self._display_file.values():
            painter.setPen(QColor(str(drawable.color)))
            painter.setBrush(QColor(str(drawable.color)))
            drawable.render(self.camera)

        painter.end()
        return super().paintEvent(event)

    def resizeEvent(self, event):
        w, h = self.width(), self.height()
        self.camera.viewport_size = Vector(w - 80, h - 80)
        InteractiveGraphicalSystem.log(f"Viewport resized to {w}x{h}")
        return super().resizeEvent(event)

    def keyPressEvent(self, e):
        # camera movement
        if e.key() == Qt.Key_W:
            self.pan_camera(0, 1)
        elif e.key() == Qt.Key_S and not e.modifiers():
            self.pan_camera(0, -1)
        elif e.key() == Qt.Key_A:
            self.pan_camera(-1, 0)
        elif e.key() == Qt.Key_D:
            self.pan_camera(1, 0)
        # camera rotation
        elif e.key() == Qt.Key_Q:
            self.tilt_view(1, Camera.ROLL)
        elif e.key() == Qt.Key_E:
            self.tilt_view(-1, Camera.ROLL)
        elif e.key() == Qt.Key_I:
            self.tilt_view(1, Camera.PITCH)
        elif e.key() == Qt.Key_K:
            self.tilt_view(-1, Camera.PITCH)
        elif e.key() == Qt.Key_J:
            self.tilt_view(1, Camera.YAW)
        elif e.key() == Qt.Key_L:
            self.tilt_view(-1, Camera.YAW)
        # camera zooming
        elif e.key() == Qt.Key_Minus and e.modifiers() & Qt.ControlModifier:
            step = self._zoom_slider.pageStep()
            self._zoom_slider.setValue(self._zoom_slider.value() - step)
        elif e.key() == Qt.Key_Equal and e.modifiers() & Qt.ControlModifier:
            step = self._zoom_slider.pageStep()
            self._zoom_slider.setValue(self._zoom_slider.value() + step)
        # also forward (most) events to parent widget
        if e.key() != Qt.Key_Tab:
            return super().keyPressEvent(e)

    def focusNextPrevChild(self, next):  # disable focus change with Tab
        return False

    def wheelEvent(self, e):  # ctrl + mouse wheel also zooms
        if e.modifiers() & Qt.ControlModifier:
            step = self._zoom_slider.singleStep() * sign(e.angleDelta().y())
            self._zoom_slider.setValue(self._zoom_slider.value() + step)
        else:
            return super().wheelEvent(e)

    def mousePressEvent(self, e):
        if e.button() == Qt.MiddleButton:
            if e.modifiers() & Qt.ShiftModifier:
                self._drag_begin = Point(e.x(), e.y())
            elif e.modifiers() & Qt.ControlModifier:
                self._rotate_begin = Point(e.x(), e.y())
        else:
            return super().mousePressEvent(e)

    def mouseReleaseEvent(self, e):
        if e.button() == Qt.MiddleButton:
            if self._drag_begin:
                InteractiveGraphicalSystem.log(
                    "Window dragged to (%g, %g, %g)" %
                    (self.camera.x, self.camera.y, self.camera.z)
                )
            self._drag_begin = None
            self._rotate_begin = None
        else:
            return super().mouseReleaseEvent(e)

    def mouseMoveEvent(self, e):
        if self._drag_begin:
            # compute motion vector and update drag initial position
            delta = Point(e.x(), e.y()) - self._drag_begin
            self._drag_begin += delta
            # adjust delta based on window zoom
            dx = delta.x / self.camera.zoom
            dy = delta.y / self.camera.zoom
            # move the window accordingly (scene follows mouse)
            self.pan_camera(-dx, dy, _normalized=False)
        elif self._rotate_begin:
            delta = Point(e.x(), e.y()) - self._rotate_begin
            self._rotate_begin += delta
            rx = lerp(delta.x, 0, self.width(), 0, radians(180))
            ry = lerp(delta.y, 0, self.height(), 0, radians(180))
            self.tilt_view(rx, Camera.YAW, _normalized=False)
            self.tilt_view(ry, Camera.PITCH, _normalized=False)
        else:
            self._eye_position.setText(f"[{e.x()}, {e.y()}]")
            return super().mouseMoveEvent(e)


class SettingsDialog(QDialog, Ui_SettingsDialog):
    CLIP_CS = 'Cohen-Sutherland'
    CLIP_LB = 'Liang-Barsky'

    def __init__(self, *args, **kwargs):
        QDialog.__init__(self, *args, **kwargs)
        self.setupUi(self)
        self.buttonBox.accepted.connect(lambda: self.accept())
        self.buttonBox.rejected.connect(lambda: self.reject())


if __name__ == '__main__':
    if '-h' in argv:
        print(f"Usage: {argv[0]} [<objfiles> ...] | -h")
        exit(0)
    else:
        app = QApplication(argv)
        gui = InteractiveGraphicalSystem()
        for obj in argv[1:]:
            gui.load_obj(obj)
        gui.displayFile.setCurrentRow(-1)
        exit(app.exec_())
