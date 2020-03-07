"""@TODO: main module docstring"""

import sys
from PySide2.QtWidgets import QApplication, QMainWindow

from .gui import Ui_MainWindow


class InteractiveGraphicalSystem(QMainWindow, Ui_MainWindow):
    """@TODO: SGI class docstring"""

    def __init__(self):
        super(InteractiveGraphicalSystem, self).__init__()
        self.setupUi(self)
        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    gui = InteractiveGraphicalSystem()
    sys.exit(app.exec_())
