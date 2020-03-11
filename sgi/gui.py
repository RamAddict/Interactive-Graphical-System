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
        MainWindow.setEnabled(True)
        MainWindow.resize(1280, 720)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.displayFile = QListWidget(self.centralwidget)
        self.displayFile.setObjectName(u"displayFile")
        self.displayFile.setGeometry(QRect(980, 25, 190, 205))
        self.controlFrame = QFrame(self.centralwidget)
        self.controlFrame.setObjectName(u"controlFrame")
        self.controlFrame.setGeometry(QRect(980, 260, 290, 170))
        self.controlFrame.setFrameShape(QFrame.StyledPanel)
        self.controlFrame.setFrameShadow(QFrame.Sunken)
        self.controlLayout = QGridLayout(self.controlFrame)
        self.controlLayout.setObjectName(u"controlLayout")
        self.controlLayout.setContentsMargins(20, -1, 20, -1)
        self.upButton = QPushButton(self.controlFrame)
        self.upButton.setObjectName(u"upButton")
        self.upButton.setText(u"^")

        self.controlLayout.addWidget(self.upButton, 0, 1, 1, 1)

        self.leftButton = QPushButton(self.controlFrame)
        self.leftButton.setObjectName(u"leftButton")
        self.leftButton.setText(u"<")

        self.controlLayout.addWidget(self.leftButton, 1, 0, 1, 1)

        self.rightButton = QPushButton(self.controlFrame)
        self.rightButton.setObjectName(u"rightButton")
        self.rightButton.setText(u">")

        self.controlLayout.addWidget(self.rightButton, 1, 2, 1, 1)

        self.downButton = QPushButton(self.controlFrame)
        self.downButton.setObjectName(u"downButton")
        self.downButton.setText(u"v")

        self.controlLayout.addWidget(self.downButton, 2, 1, 1, 1)

        self.zoomSlider = QSlider(self.controlFrame)
        self.zoomSlider.setObjectName(u"zoomSlider")
        self.zoomSlider.setMinimum(0)
        self.zoomSlider.setMaximum(100)
        self.zoomSlider.setSingleStep(10)
        self.zoomSlider.setValue(50)
        self.zoomSlider.setOrientation(Qt.Horizontal)
        self.zoomSlider.setTickPosition(QSlider.TicksBothSides)
        self.zoomSlider.setTickInterval(5)

        self.controlLayout.addWidget(self.zoomSlider, 3, 0, 1, 3)

        self.viewportLabel = QLabel(self.centralwidget)
        self.viewportLabel.setObjectName(u"viewportLabel")
        self.viewportLabel.setGeometry(QRect(10, 5, 58, 18))
        self.viewportLabel.setText(u"Viewport")
        self.sceneLabel = QLabel(self.centralwidget)
        self.sceneLabel.setObjectName(u"sceneLabel")
        self.sceneLabel.setGeometry(QRect(980, 5, 70, 18))
        self.controlLabel = QLabel(self.centralwidget)
        self.controlLabel.setObjectName(u"controlLabel")
        self.controlLabel.setGeometry(QRect(980, 240, 100, 18))
        self.consoleLabel = QLabel(self.centralwidget)
        self.consoleLabel.setObjectName(u"consoleLabel")
        self.consoleLabel.setGeometry(QRect(10, 570, 50, 18))
        self.objectLabel = QLabel(self.centralwidget)
        self.objectLabel.setObjectName(u"objectLabel")
        self.objectLabel.setGeometry(QRect(980, 440, 40, 18))
        self.canvasFrame = QFrame(self.centralwidget)
        self.canvasFrame.setObjectName(u"canvasFrame")
        self.canvasFrame.setGeometry(QRect(10, 25, 960, 540))
        self.canvasFrame.setFrameShape(QFrame.StyledPanel)
        self.canvasFrame.setFrameShadow(QFrame.Sunken)
        self.layoutWidget = QWidget(self.centralwidget)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(1180, 30, 90, 196))
        self.actionsLayout = QVBoxLayout(self.layoutWidget)
        self.actionsLayout.setObjectName(u"actionsLayout")
        self.actionsLayout.setContentsMargins(0, 0, 0, 0)
        self.newButton = QPushButton(self.layoutWidget)
        self.newButton.setObjectName(u"newButton")

        self.actionsLayout.addWidget(self.newButton)

        self.editButton = QPushButton(self.layoutWidget)
        self.editButton.setObjectName(u"editButton")

        self.actionsLayout.addWidget(self.editButton)

        self.removeButton = QPushButton(self.layoutWidget)
        self.removeButton.setObjectName(u"removeButton")

        self.actionsLayout.addWidget(self.removeButton)

        self.upListButton = QPushButton(self.layoutWidget)
        self.upListButton.setObjectName(u"upListButton")

        self.actionsLayout.addWidget(self.upListButton)

        self.downListButton = QPushButton(self.layoutWidget)
        self.downListButton.setObjectName(u"downListButton")

        self.actionsLayout.addWidget(self.downListButton)

        self.objectArea = QScrollArea(self.centralwidget)
        self.objectArea.setObjectName(u"objectArea")
        self.objectArea.setEnabled(True)
        self.objectArea.setGeometry(QRect(980, 460, 290, 250))
        self.objectArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 286, 246))
        self.nameLabel = QLabel(self.scrollAreaWidgetContents)
        self.nameLabel.setObjectName(u"nameLabel")
        self.nameLabel.setGeometry(QRect(10, 10, 50, 32))
        font = QFont()
        font.setPointSize(12)
        self.nameLabel.setFont(font)
        self.nameEdit = QLineEdit(self.scrollAreaWidgetContents)
        self.nameEdit.setObjectName(u"nameEdit")
        self.nameEdit.setGeometry(QRect(70, 10, 200, 32))
        self.typeBox = QComboBox(self.scrollAreaWidgetContents)
        self.typeBox.addItem("")
        self.typeBox.addItem("")
        self.typeBox.addItem("")
        self.typeBox.setObjectName(u"typeBox")
        self.typeBox.setGeometry(QRect(70, 50, 200, 32))
        self.typeLabel = QLabel(self.scrollAreaWidgetContents)
        self.typeLabel.setObjectName(u"typeLabel")
        self.typeLabel.setGeometry(QRect(10, 50, 40, 32))
        self.typeLabel.setFont(font)
        self.dialogBox = QDialogButtonBox(self.scrollAreaWidgetContents)
        self.dialogBox.setObjectName(u"dialogBox")
        self.dialogBox.setGeometry(QRect(60, 204, 160, 34))
        self.dialogBox.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Ok)
        self.objectArea.setWidget(self.scrollAreaWidgetContents)
        self.console = QTextBrowser(self.centralwidget)
        self.console.setObjectName(u"console")
        self.console.setGeometry(QRect(10, 590, 960, 120))
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.typeBox.setCurrentIndex(1)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Interactive Graphical System - INE5420-CG - 2020/1", None))
        self.sceneLabel.setText(QCoreApplication.translate("MainWindow", u"Display File", None))
        self.controlLabel.setText(QCoreApplication.translate("MainWindow", u"Window Control", None))
        self.consoleLabel.setText(QCoreApplication.translate("MainWindow", u"Console", None))
        self.objectLabel.setText(QCoreApplication.translate("MainWindow", u"Object", None))
        self.newButton.setText(QCoreApplication.translate("MainWindow", u"New", None))
        self.editButton.setText(QCoreApplication.translate("MainWindow", u"Edit", None))
        self.removeButton.setText(QCoreApplication.translate("MainWindow", u"Remove", None))
        self.upListButton.setText(QCoreApplication.translate("MainWindow", u"Move Up", None))
        self.downListButton.setText(QCoreApplication.translate("MainWindow", u"Move Down", None))
        self.nameLabel.setText(QCoreApplication.translate("MainWindow", u"Name:", None))
        self.nameEdit.setText(QCoreApplication.translate("MainWindow", u"Enter name here", None))
        self.typeBox.setItemText(0, QCoreApplication.translate("MainWindow", u"Point", None))
        self.typeBox.setItemText(1, QCoreApplication.translate("MainWindow", u"Line", None))
        self.typeBox.setItemText(2, QCoreApplication.translate("MainWindow", u"Wireframe", None))

        self.typeLabel.setText(QCoreApplication.translate("MainWindow", u"Type:", None))
    # retranslateUi

