import sys
from PySide2.QtWidgets import *
from PySide2.QtGui import *
from PySide2.QtCore import *

from .gui import Ui_MainWindow
from .display import *


class DisplayFile():
    def __init__(self):
        self.shapes = []
    def __iter__(self):
        return self.shapes.__iter__()


class InteractiveGraphicalSystem(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(InteractiveGraphicalSystem, self).__init__()
        self.setupUi(self)
        self.show()

        self.up_btn.clicked.connect(lambda: self.print("UP!"))
        test = QListWidgetItem()
        test.setText("list:")
        self.display_file.addItem(test)

    def print(self, str, end='\n'):
        self.textBrowser_2.setPlainText(self.textBrowser_2.toPlainText() + str + end)

    def list(self, shape):
        item = QListWidgetItem()
        item.setText(shape.name)
        self.display_file.addItem(item)


if __name__ == '__main__':
    qt = QApplication(sys.argv)

    app = InteractiveGraphicalSystem()

    df = [Point('p1', (0,0)), Point('p2', (10,10)), Line('l1', (2,2), (5,5)),
          Wireframe('s1', [Line('l1', (2,2), (5,5))])]
    for x in df:
        app.list(x)

    sys.exit(qt.exec_())
