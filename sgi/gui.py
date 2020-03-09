# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'g.ui'
##
## Created by: Qt User Interface Compiler version 5.14.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import (QCoreApplication, QMetaObject, QObject, QPoint,
    QRect, QSize, QUrl, Qt)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont,
    QFontDatabase, QIcon, QLinearGradient, QPalette, QPainter, QPixmap,
    QRadialGradient)
from PySide2.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1280, 720)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.objectList = QListWidget(self.centralwidget)
        self.objectList.setObjectName(u"objectList")
        self.objectList.setGeometry(QRect(980, 10, 290, 200))
        self.layoutWidget = QWidget(self.centralwidget)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(970, 220, 304, 171))
        self.cameraControls = QGridLayout(self.layoutWidget)
        self.cameraControls.setObjectName(u"cameraControls")
        self.cameraControls.setContentsMargins(20, 0, 20, 0)
        self.upButton = QPushButton(self.layoutWidget)
        self.upButton.setObjectName(u"upButton")
        self.upButton.setText(u"^")

        self.cameraControls.addWidget(self.upButton, 0, 1, 1, 1)

        self.leftButton = QPushButton(self.layoutWidget)
        self.leftButton.setObjectName(u"leftButton")
        self.leftButton.setText(u"<")

        self.cameraControls.addWidget(self.leftButton, 1, 0, 1, 1)

        self.rightButton = QPushButton(self.layoutWidget)
        self.rightButton.setObjectName(u"rightButton")
        self.rightButton.setText(u">")

        self.cameraControls.addWidget(self.rightButton, 1, 2, 1, 1)

        self.downButton = QPushButton(self.layoutWidget)
        self.downButton.setObjectName(u"downButton")
        self.downButton.setText(u"v")

        self.cameraControls.addWidget(self.downButton, 2, 1, 1, 1)

        self.zoomSlider = QSlider(self.layoutWidget)
        self.zoomSlider.setObjectName(u"zoomSlider")
        self.zoomSlider.setMinimum(0)
        self.zoomSlider.setMaximum(100)
        self.zoomSlider.setSingleStep(10)
        self.zoomSlider.setValue(50)
        self.zoomSlider.setOrientation(Qt.Horizontal)
        self.zoomSlider.setTickPosition(QSlider.TicksBothSides)
        self.zoomSlider.setTickInterval(5)

        self.cameraControls.addWidget(self.zoomSlider, 3, 0, 1, 3)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Interactive Graphical System - INE5420-CG - 2020/1", None))
    # retranslateUi

