# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main.ui'
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
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.viewportLayout = QVBoxLayout()
        self.viewportLayout.setSpacing(0)
        self.viewportLayout.setObjectName(u"viewportLayout")
        self.viewportLabel = QLabel(self.centralwidget)
        self.viewportLabel.setObjectName(u"viewportLabel")
        self.viewportLabel.setText(u"Viewport")

        self.viewportLayout.addWidget(self.viewportLabel)

        self.canvasFrame = QFrame(self.centralwidget)
        self.canvasFrame.setObjectName(u"canvasFrame")
        self.canvasFrame.setFrameShape(QFrame.StyledPanel)
        self.canvasFrame.setFrameShadow(QFrame.Sunken)
        self.gridLayout_3 = QGridLayout(self.canvasFrame)
        self.gridLayout_3.setObjectName(u"gridLayout_3")

        self.viewportLayout.addWidget(self.canvasFrame)

        self.viewportLayout.setStretch(1, 1)

        self.gridLayout.addLayout(self.viewportLayout, 0, 0, 3, 1)

        self.displayFileLayout = QVBoxLayout()
        self.displayFileLayout.setSpacing(0)
        self.displayFileLayout.setObjectName(u"displayFileLayout")
        self.sceneLabel = QLabel(self.centralwidget)
        self.sceneLabel.setObjectName(u"sceneLabel")

        self.displayFileLayout.addWidget(self.sceneLabel)

        self.scenelLayout = QHBoxLayout()
        self.scenelLayout.setSpacing(6)
        self.scenelLayout.setObjectName(u"scenelLayout")
        self.displayFile = QListWidget(self.centralwidget)
        self.displayFile.setObjectName(u"displayFile")
        self.displayFile.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)

        self.scenelLayout.addWidget(self.displayFile)

        self.actionsLayout = QVBoxLayout()
        self.actionsLayout.setObjectName(u"actionsLayout")
        self.newButton = QPushButton(self.centralwidget)
        self.newButton.setObjectName(u"newButton")

        self.actionsLayout.addWidget(self.newButton)

        self.editButton = QPushButton(self.centralwidget)
        self.editButton.setObjectName(u"editButton")

        self.actionsLayout.addWidget(self.editButton)

        self.removeButton = QPushButton(self.centralwidget)
        self.removeButton.setObjectName(u"removeButton")

        self.actionsLayout.addWidget(self.removeButton)

        self.upListButton = QPushButton(self.centralwidget)
        self.upListButton.setObjectName(u"upListButton")

        self.actionsLayout.addWidget(self.upListButton)

        self.downListButton = QPushButton(self.centralwidget)
        self.downListButton.setObjectName(u"downListButton")

        self.actionsLayout.addWidget(self.downListButton)


        self.scenelLayout.addLayout(self.actionsLayout)

        self.scenelLayout.setStretch(0, 1)

        self.displayFileLayout.addLayout(self.scenelLayout)

        self.displayFileLayout.setStretch(1, 1)

        self.gridLayout.addLayout(self.displayFileLayout, 0, 1, 1, 1)

        self.windowLayout = QVBoxLayout()
        self.windowLayout.setSpacing(0)
        self.windowLayout.setObjectName(u"windowLayout")
        self.controlLabel = QLabel(self.centralwidget)
        self.controlLabel.setObjectName(u"controlLabel")

        self.windowLayout.addWidget(self.controlLabel)

        self.controlFrame = QFrame(self.centralwidget)
        self.controlFrame.setObjectName(u"controlFrame")
        self.controlFrame.setFrameShape(QFrame.StyledPanel)
        self.controlFrame.setFrameShadow(QFrame.Sunken)
        self.controlLayout = QGridLayout(self.controlFrame)
        self.controlLayout.setObjectName(u"controlLayout")
        self.controlLayout.setContentsMargins(20, -1, 20, -1)
        self.upBtn = QPushButton(self.controlFrame)
        self.upBtn.setObjectName(u"upBtn")
        self.upBtn.setText(u"^")

        self.controlLayout.addWidget(self.upBtn, 0, 1, 1, 1)

        self.leftBtn = QPushButton(self.controlFrame)
        self.leftBtn.setObjectName(u"leftBtn")
        self.leftBtn.setText(u"<")

        self.controlLayout.addWidget(self.leftBtn, 1, 0, 1, 1)

        self.rightBtn = QPushButton(self.controlFrame)
        self.rightBtn.setObjectName(u"rightBtn")
        self.rightBtn.setText(u">")

        self.controlLayout.addWidget(self.rightBtn, 1, 2, 1, 1)

        self.downBtn = QPushButton(self.controlFrame)
        self.downBtn.setObjectName(u"downBtn")
        self.downBtn.setText(u"v")

        self.controlLayout.addWidget(self.downBtn, 2, 1, 1, 1)

        self.zoomSlider = QSlider(self.controlFrame)
        self.zoomSlider.setObjectName(u"zoomSlider")
        self.zoomSlider.setFocusPolicy(Qt.WheelFocus)
        self.zoomSlider.setMinimum(0)
        self.zoomSlider.setMaximum(100)
        self.zoomSlider.setValue(50)
        self.zoomSlider.setOrientation(Qt.Horizontal)
        self.zoomSlider.setTickPosition(QSlider.TicksBothSides)
        self.zoomSlider.setTickInterval(5)

        self.controlLayout.addWidget(self.zoomSlider, 3, 0, 1, 3)

        self.controlLayout.setRowStretch(3, 1)

        self.windowLayout.addWidget(self.controlFrame)

        self.windowLayout.setStretch(1, 1)

        self.gridLayout.addLayout(self.windowLayout, 1, 1, 1, 1)

        self.objectLayout = QVBoxLayout()
        self.objectLayout.setSpacing(0)
        self.objectLayout.setObjectName(u"objectLayout")
        self.objectLabel = QLabel(self.centralwidget)
        self.objectLabel.setObjectName(u"objectLabel")

        self.objectLayout.addWidget(self.objectLabel)

        self.objectArea = QScrollArea(self.centralwidget)
        self.objectArea.setObjectName(u"objectArea")
        self.objectArea.setEnabled(True)
        self.objectArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 304, 247))
        self.verticalLayout = QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(-1, 5, -1, -1)
        self.formLayout = QFormLayout()
        self.formLayout.setObjectName(u"formLayout")
        self.formLayout.setFormAlignment(Qt.AlignHCenter|Qt.AlignTop)
        self.nameLabel = QLabel(self.scrollAreaWidgetContents)
        self.nameLabel.setObjectName(u"nameLabel")
        font = QFont()
        font.setPointSize(12)
        self.nameLabel.setFont(font)

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.nameLabel)

        self.nameEdit = QLineEdit(self.scrollAreaWidgetContents)
        self.nameEdit.setObjectName(u"nameEdit")

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.nameEdit)

        self.typeLabel = QLabel(self.scrollAreaWidgetContents)
        self.typeLabel.setObjectName(u"typeLabel")
        self.typeLabel.setFont(font)

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.typeLabel)

        self.typeBox = QComboBox(self.scrollAreaWidgetContents)
        self.typeBox.addItem("")
        self.typeBox.addItem("")
        self.typeBox.addItem("")
        self.typeBox.setObjectName(u"typeBox")

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.typeBox)


        self.verticalLayout.addLayout(self.formLayout)

        self.dialogBox = QDialogButtonBox(self.scrollAreaWidgetContents)
        self.dialogBox.setObjectName(u"dialogBox")
        self.dialogBox.setLayoutDirection(Qt.LeftToRight)
        self.dialogBox.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Ok)
        self.dialogBox.setCenterButtons(True)

        self.verticalLayout.addWidget(self.dialogBox)

        self.verticalLayout.setStretch(0, 1)
        self.objectArea.setWidget(self.scrollAreaWidgetContents)

        self.objectLayout.addWidget(self.objectArea)

        self.objectLayout.setStretch(1, 1)

        self.gridLayout.addLayout(self.objectLayout, 2, 1, 2, 1)

        self.consoleLayout = QVBoxLayout()
        self.consoleLayout.setSpacing(0)
        self.consoleLayout.setObjectName(u"consoleLayout")
        self.consoleLabel = QLabel(self.centralwidget)
        self.consoleLabel.setObjectName(u"consoleLabel")

        self.consoleLayout.addWidget(self.consoleLabel)

        self.consoleArea = QTextBrowser(self.centralwidget)
        self.consoleArea.setObjectName(u"consoleArea")

        self.consoleLayout.addWidget(self.consoleArea)

        self.consoleLayout.setStretch(1, 1)

        self.gridLayout.addLayout(self.consoleLayout, 3, 0, 1, 1)

        self.gridLayout.setRowStretch(0, 4)
        self.gridLayout.setRowStretch(1, 7)
        self.gridLayout.setRowStretch(2, 4)
        self.gridLayout.setRowStretch(3, 5)
        self.gridLayout.setColumnStretch(0, 4)
        self.gridLayout.setColumnStretch(1, 1)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.typeBox.setCurrentIndex(-1)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Interactive Graphical System - INE5420-CG - 2020/1", None))
        self.sceneLabel.setText(QCoreApplication.translate("MainWindow", u"Display File", None))
        self.newButton.setText(QCoreApplication.translate("MainWindow", u"New", None))
        self.editButton.setText(QCoreApplication.translate("MainWindow", u"Edit", None))
        self.removeButton.setText(QCoreApplication.translate("MainWindow", u"Remove", None))
        self.upListButton.setText(QCoreApplication.translate("MainWindow", u"Move Up", None))
        self.downListButton.setText(QCoreApplication.translate("MainWindow", u"Move Down", None))
        self.controlLabel.setText(QCoreApplication.translate("MainWindow", u"Window Control", None))
        self.objectLabel.setText(QCoreApplication.translate("MainWindow", u"Object", None))
        self.nameLabel.setText(QCoreApplication.translate("MainWindow", u"Name:", None))
        self.typeLabel.setText(QCoreApplication.translate("MainWindow", u"Type:", None))
        self.typeBox.setItemText(0, QCoreApplication.translate("MainWindow", u"Point", None))
        self.typeBox.setItemText(1, QCoreApplication.translate("MainWindow", u"Line", None))
        self.typeBox.setItemText(2, QCoreApplication.translate("MainWindow", u"Wireframe", None))

        self.consoleLabel.setText(QCoreApplication.translate("MainWindow", u"Console", None))
    # retranslateUi

