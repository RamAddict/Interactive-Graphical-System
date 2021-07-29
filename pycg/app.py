#!/usr/bin/env python3

from math import inf, radians
from sys import argv
from os import path
from typing import Optional, Callable, Dict, Sequence, Tuple
from ast import literal_eval

from PySide2.QtWidgets import (QApplication, QMainWindow, QWidget, QDialog,
                               QColorDialog, QFileDialog, QMessageBox, QInputDialog,
                               QDialogButtonBox)
from PySide2.QtGui import (QPainter, QKeySequence, QColor, QPalette, QIcon,
                           QPixmap, QPolygon)
from PySide2.QtCore import Qt, QPoint

from blas import Vector, Matrix
from graphics import (Painter, Camera, Transformation, Drawable, Point, Line,
                      Wireframe, Polygon, Color)
from utilities import experp, begin, sign, to_float
import obj as wavefront_obj
from ui.main import Ui_MainWindow
from ui.point import Ui_PointFields
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
        self.tiltRightBtn.clicked.connect(
            lambda: self.viewport.tilt_view(radians(-15)))
        self.tiltLeftBtn.clicked.connect(
            lambda: self.viewport.tilt_view(radians(15)))

        # zoom slider setup
        self.zoomSlider.valueChanged.connect(
            lambda _: self.viewport.update_zoom(self.zoomSlider.value(),
                                                self.zoomSlider.minimum(),
                                                self.zoomSlider.maximum()))
        self.zoomSlider.valueChanged.emit(None)

        # setting up scene controls
        self.removeButton.clicked.connect(
            lambda: self.remove_object(self.displayFile.currentRow()))
        self.upListButton.clicked.connect(
            lambda: self.move_object(self.displayFile.currentRow(), -1))
        self.downListButton.clicked.connect(
            lambda: self.move_object(self.displayFile.currentRow(), 1))
        self.newButton.clicked.connect(lambda: begin(
            self.typeBox.setCurrentIndex(-1),
            self.nameEdit.setText(""),
            self.componentWidget.setCurrentWidget(self.objectPage),
        ))
        self._transformations_with_pivots = []
        self.transformButton.clicked.connect(  # ensures something is selected
            lambda: None if self.displayFile.currentRow() < 0
            else begin(
                self._transformations_with_pivots.clear(),
                self.transformList.clear(),
                self.translateXinput.setText("0"),
                self.translateYinput.setText("0"),
                self.pivotSelect.setCurrentIndex(0),
                self.angleInput.setText("0"),
                self.scaleXinput.setText("1"),
                self.scaleYinput.setText("1"),
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

        def handle_new_action():
            new_obj = None
            text, _ = QInputDialog.getText(
                self,
                "Input",
                "Manual input in format (x1,y1),(x2,y2),...",
            )
            parsed = literal_eval(text)
            if not isinstance(parsed, tuple): return
            if len(parsed) == 2:  # single point, or tuple with 2 points
                a, b = parsed
                if isinstance(a, tuple):
                    new_obj = Line(Point(*a), Point(*b))
                elif isinstance(a, (int, float)):
                    new_obj = Point(a, b)
            else:
                points = [Point(x, y) for x, y in parsed]
                if points[-1] == points[0]: new_obj = Polygon(points)
                else: new_obj = Wireframe(points)
            if new_obj is not None:
                self.insert_object(new_obj, "object")

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
        self.actionNew.triggered.connect(handle_new_action)
        self.actionNew.setShortcut(QKeySequence.New)
        self.actionSettings.triggered.connect(handle_settings_action)
        self.actionSettings.setShortcut(QKeySequence.Preferences)

        def new_type_select(index: int):
            # clean all fields after 'name', 'color' and 'type'
            while self.formLayout.rowCount() > 3:
                self.formLayout.removeRow(3)

            typename = self.typeBox.itemText(index)
            if typename == 'Point':
                self.formLayout.addRow(PointFields())
            elif typename == 'Line':
                self.formLayout.addRow(PointFields())
                self.formLayout.addRow(PointFields())
            elif typename in ('Wireframe', 'Polygon'):
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

        def new_object():
            if self.typeBox.currentIndex() < 0:
                return

            name = self.nameEdit.text()
            typename = self.typeBox.currentText()
            color = QColor(self.colorEdit.text())
            color = Color(color.red(), color.green(), color.blue())

            # indexes of QLayout.itemAt() depend on the order of UI elements
            obj = None
            if typename == 'Point':
                obj = self.formLayout.itemAt(6).widget().to_point()
            elif typename == 'Line':
                pa = self.formLayout.itemAt(6).widget().to_point()
                pb = self.formLayout.itemAt(7).widget().to_point()
                obj = Line(pa, pb)
            elif typename in ('Wireframe', 'Polygon'):
                points = []
                for i in range(6, self.formLayout.count() - 1):
                    p = self.formLayout.itemAt(i).widget().to_point()
                    points.append(p)
                if typename == 'Polygon': obj = Polygon(points)
                else: obj = Wireframe(points)

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

        self.typeBox.currentIndexChanged.connect(new_type_select)
        self.colorEdit.clicked.connect(pick_color)
        pick_color(QPalette().color(QPalette.Foreground).name())
        self.dialogBox.accepted.connect(new_object)
        self.dialogBox.rejected.connect(
            lambda: self.componentWidget.setCurrentWidget(self.emptyPage))

        def do_transformations():
            if not self._transformations_with_pivots: return
            name = self.displayFile.currentItem().text()
            drawable = self.display_file[name]
            result = Matrix.identity(3)
            for transformation, pivot in reversed(self._transformations_with_pivots):
                pivot = pivot or drawable.center()
                matrix = transformation.matrix(pivot)
                result = result @ matrix
            drawable.transform(result)
            self.viewport.update()
            self.log("Applied transformation\n" + str(result))

        def add_transformation():
            # get the correct pivot from dropdown box
            pivot = None
            if self.pivotSelect.currentText() == 'Origin':
                pivot = Point(0, 0)
            elif self.pivotSelect.currentText() == 'Custom':
                pivot = Point(to_float(self.rotateXInput.text()),
                              to_float(self.rotateYInput.text()))

            tx = to_float(self.translateXinput.text()) or 0
            ty = to_float(self.translateYinput.text()) or 0
            theta = radians((to_float(self.angleInput.text()) or 0))
            sx = to_float(self.scaleXinput.text()) or 1
            sy = to_float(self.scaleYinput.text()) or 1
            transform = Transformation().translate(tx, ty).rotate(theta).scale(sx, sy)

            self._transformations_with_pivots.append((transform, pivot))
            self.transformList.addItem(f"T({tx}, {ty}), R({theta}), S({sx},{sy})")

        def enableRotateLabels():
            custom = self.pivotSelect.currentText() == 'Custom'
            self.rotateXInput.setEnabled(custom)
            self.rotateYInput.setEnabled(custom)

        self.pivotSelect.currentIndexChanged.connect(enableRotateLabels)
        self.transformAddButton.clicked.connect(add_transformation)
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

            def draw_polygon(self, points: Sequence[Tuple]):
                self.drawPolygon(QPolygon([QPoint(x, y) for x, y in points]))

        super().__init__(parent_widget)
        self._display_file = display_file  # modified by main window
        self._zoom_slider = zoom_slider
        self._eye_position = eye_position
        size = Vector(self.width() - 80, self.height() - 80)
        self.camera = Camera(QtPainter(), size, Point(40, 40))
        self._pan = 10
        self._drag_begin = None
        self.setFocusPolicy(Qt.StrongFocus)
        self.setMouseTracking(True)

    def pan_camera(self, dx, dy, _normalized=True):
        """Move the camera by a certain amount of dynamically-sized steps.
        Takes the camera tilt into account, such that movement is view-aligned.
        """
        if _normalized:
            dx *= self._pan
            dy *= dy * self._pan
        align = Transformation().rotate(self.camera.angle).matrix()
        dx, dy, _ = align @ Vector(dx, dy, 1)
        self.camera.x += dx
        self.camera.y += dy
        self.update()

    def update_zoom(self, value, minimum, maximum):
        """Update zoom within a certain range."""
        zoom = experp(value, minimum, maximum, 0.1, 10)
        self.camera.zoom = zoom
        self._pan = 10 / zoom  # NOTE: camera step is adjusted by zoom
        self.update()

    def tilt_view(self, theta: float):
        """Tilt the camera view by the given amount."""
        self.camera.angle += theta
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
            drawable.draw(self.camera)

        painter.end()
        return super().paintEvent(event)

    def resizeEvent(self, event):
        w, h = self.width(), self.height()
        self.camera.viewport_size = Vector(w - 80, h - 80)
        InteractiveGraphicalSystem.log(f"Viewport resized to {w}x{h}")
        return super().resizeEvent(event)

    def keyPressEvent(self, e):
        # window movement
        if e.key() == Qt.Key_W:
            self.pan_camera(0, 1)
        elif e.key() == Qt.Key_A:
            self.pan_camera(-1, 0)
        elif e.key() == Qt.Key_S and not e.modifiers() & Qt.ControlModifier:
            self.pan_camera(0, -1)
        elif e.key() == Qt.Key_D:
            self.pan_camera(1, 0)
        # window zooming
        elif e.key() == Qt.Key_Minus and e.modifiers() & Qt.ControlModifier:
            step = self._zoom_slider.pageStep()
            self._zoom_slider.setValue(self._zoom_slider.value() - step)
        elif e.key() == Qt.Key_Equal and e.modifiers() & Qt.ControlModifier:
            step = self._zoom_slider.pageStep()
            self._zoom_slider.setValue(self._zoom_slider.value() + step)
        # window rotation
        elif e.key() == Qt.Key_Q:
            self.tilt_view(radians(15))
        elif e.key() == Qt.Key_E:
            self.tilt_view(radians(-15))
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

    def mousePressEvent(self, event):
        if event.button() == Qt.MiddleButton:
            self._drag_begin = Point(event.x(), event.y())
        else:
            return super().mousePressEvent(event)

    def mouseReleaseEvent(self, event):
        if event.button() == Qt.MiddleButton:
            self._drag_begin = None
            InteractiveGraphicalSystem.log(
                "Window dragged to (%g, %g)" % (self.camera.x, self.camera.y))
        else:
            return super().mouseReleaseEvent(event)

    def mouseMoveEvent(self, event):
        if self._drag_begin:
            # compute motion vector and update drag initial position
            delta = (event.x(), event.y()) - self._drag_begin
            self._drag_begin += delta
            # adjust delta based on window zoom
            dx = delta.x / self.camera.zoom
            dy = delta.y / self.camera.zoom
            # move the window accordingly (scene follows mouse)
            self.pan_camera(-dx, dy, _normalized=False)
        else:
            self._eye_position.setText(f"[{event.x()}, {event.y()}]")
            return super().mouseMoveEvent(event)


class PointFields(QWidget, Ui_PointFields):
    def __init__(self, *args, **kwargs):
        QWidget.__init__(self, *args, **kwargs)
        self.setupUi(self)
        self.xDoubleSpinBox.setRange(-inf, inf)
        self.yDoubleSpinBox.setRange(-inf, inf)
        self._has_action = False

    def to_point(self) -> Point:
        return Point(self.xDoubleSpinBox.value(), self.yDoubleSpinBox.value())

    def set_action(self, action: Optional[Callable[[], None]]):
        """Set procedure to be executed when the action button is clicked."""

        # NOTE: multiple receivers must be disconnect()ed from a signal
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
