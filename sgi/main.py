"""Main Qt application."""

import sys
from PySide2.QtWidgets import QApplication, QMainWindow, QGraphicsView, QTextBrowser, QSlider, QWidget
from PySide2.QtGui import QPainter
from PySide2.QtCore import (QCoreApplication, QMetaObject, QObject, QPoint,
    QRect, QSize, QUrl, Qt)

from gui import Ui_MainWindow
from primitives import *
from graphics import *


class DebugConsole(QTextBrowser):
    def __init__(self, widget):
        QTextBrowser.__init__(self, widget)
    
    def print(self, str):
        self.setPlainText(self.toPlainText() + str + '\n')


class MyPainter(Painter):
    def __init__(self):
        self.painter = QPainter()

    def draw_pixel(self, x, y):
        self.painter.drawPoint(x, y)

    def draw_line(self, x1, y1, x2, y2):
        self.painter.drawLine(x1, y1, x2, y2)

class MainGraphicsView(QWidget):
    def __init__(self, widget, objects, camera):
        QWidget.__init__(self, widget)
        self.objects = objects
        self.camera = camera

    def paintEvent(self, event):
        self.camera.painter = MyPainter()
        self.camera.painter.painter.begin(self)
        for name, obj in self.objects.items():
            obj.draw(self.camera)
        self.camera.painter.painter.end()

class InteractiveGraphicalSystem(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(InteractiveGraphicalSystem, self).__init__()

        self.objects = {'line': Line(Point(500, 500), Point(700, 500)),
                        'point': Point(250, 250),
                        'wireframe': Wireframe(Point(0, 0), Point(300, 0), Point(300, 400))}

        

        # Setting up ViewPort
        self.setupUi(self)
        self.view_port = MainGraphicsView(self.centralwidget, self.objects, Camera(581, 391, None, Point(00, 00)))
        self.view_port.setObjectName(u"view_port")
        self.view_port.setGeometry(QRect(10, 10, 581, 391))

        # Adding items to DisplayFile
        for num, name in enumerate(self.objects.keys()):
            self.display_file.insertItem(num, name)

        # Setting up debug console
        self.debug_console = DebugConsole(self.centralwidget)
        self.debug_console.setObjectName(u"debug_console")
        self.debug_console.setGeometry(QRect(0, 430, 591, 171))
        self.debug_console.print("Setting up debug console")

        # Setting up moving around buttons
        self.up_btn.setText("^")
        self.down_btn.setText("v")
        self.left_btn.setText("<")
        self.right_btn.setText(">")

        def go_up():
            self.view_port.camera.y += 10
            self.view_port.update()
        def go_down():
            self.view_port.camera.y -= 10
            self.view_port.update()
        def go_left():
            self.view_port.camera.x -= 10
            self.view_port.update()
        def go_right():
            self.view_port.camera.x += 10
            self.view_port.update()
        
        self.up_btn.clicked.connect(go_up)
        self.down_btn.clicked.connect(go_down)
        self.left_btn.clicked.connect(go_left)
        self.right_btn.clicked.connect(go_right)

        # Setting up Slider
        self.horizontalSlider.setMinimum(-9.9)
        self.horizontalSlider.setMaximum(10)
        self.horizontalSlider.setTickInterval(2)
        self.horizontalSlider.setValue(0)
        self.horizontalSlider.setTickPosition(QSlider.TickPosition.TicksBothSides)
        def changeZoom():
            self.view_port.camera.zoom = (10+(self.horizontalSlider.value()))/10
            self.view_port.update()
        self.horizontalSlider.valueChanged.connect(changeZoom)

        # render it all
        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    gui = InteractiveGraphicalSystem()  # gui variable is needed
    sys.exit(app.exec_())
