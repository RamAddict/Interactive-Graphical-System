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
        self.displayFile.setSelectionRectVisible(True)

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

        self.viewportLayout = QGridLayout()
        self.viewportLayout.setObjectName(u"viewportLayout")
        self.viewportLayout.setHorizontalSpacing(0)
        self.viewportLayout.setVerticalSpacing(2)
        self.viewportLabel = QLabel(self.centralwidget)
        self.viewportLabel.setObjectName(u"viewportLabel")
        self.viewportLabel.setText(u"Viewport")

        self.viewportLayout.addWidget(self.viewportLabel, 0, 0, 1, 1)

        self.eyePositionLabel = QLabel(self.centralwidget)
        self.eyePositionLabel.setObjectName(u"eyePositionLabel")
        self.eyePositionLabel.setText(u"(0, 0)")
        self.eyePositionLabel.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.viewportLayout.addWidget(self.eyePositionLabel, 0, 1, 1, 1)

        self.canvasFrame = QFrame(self.centralwidget)
        self.canvasFrame.setObjectName(u"canvasFrame")
        self.canvasFrame.setFrameShape(QFrame.StyledPanel)
        self.canvasFrame.setFrameShadow(QFrame.Sunken)
        self.gridLayout_3 = QGridLayout(self.canvasFrame)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)

        self.viewportLayout.addWidget(self.canvasFrame, 1, 0, 1, 2)

        self.viewportLayout.setRowStretch(1, 1)
        self.viewportLayout.setColumnStretch(0, 1)
        self.viewportLayout.setColumnStretch(1, 1)

        self.gridLayout.addLayout(self.viewportLayout, 0, 0, 3, 1)

        self.consoleLayout = QVBoxLayout()
        self.consoleLayout.setSpacing(0)
        self.consoleLayout.setObjectName(u"consoleLayout")
        self.consoleLabel = QLabel(self.centralwidget)
        self.consoleLabel.setObjectName(u"consoleLabel")
        self.consoleLabel.setText(u"Console")

        self.consoleLayout.addWidget(self.consoleLabel)

        self.consoleArea = QTextBrowser(self.centralwidget)
        self.consoleArea.setObjectName(u"consoleArea")
        self.consoleArea.setOpenLinks(False)

        self.consoleLayout.addWidget(self.consoleArea)

        self.consoleLayout.setStretch(1, 1)

        self.gridLayout.addLayout(self.consoleLayout, 3, 0, 1, 1)

        self.componentWidget = QStackedWidget(self.centralwidget)
        self.componentWidget.setObjectName(u"componentWidget")
        self.emptyPage = QWidget()
        self.emptyPage.setObjectName(u"emptyPage")
        self.label = QLabel(self.emptyPage)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(50, 30, 151, 91))
        font = QFont()
        font.setFamily(u"Verdana")
        font.setPointSize(15)
        font.setItalic(True)
        self.label.setFont(font)
        self.label.setTextFormat(Qt.AutoText)
        self.label.setScaledContents(False)
        self.label.setAlignment(Qt.AlignCenter)
        self.label.setWordWrap(True)
        self.componentWidget.addWidget(self.emptyPage)
        self.objectPage = QWidget()
        self.objectPage.setObjectName(u"objectPage")
        self.verticalLayout_2 = QVBoxLayout(self.objectPage)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.objectLabel = QLabel(self.objectPage)
        self.objectLabel.setObjectName(u"objectLabel")

        self.verticalLayout_2.addWidget(self.objectLabel)

        self.objectArea = QScrollArea(self.objectPage)
        self.objectArea.setObjectName(u"objectArea")
        self.objectArea.setEnabled(True)
        self.objectArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 247, 261))
        self.verticalLayout = QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(-1, 5, -1, -1)
        self.formLayout = QFormLayout()
        self.formLayout.setObjectName(u"formLayout")
        self.formLayout.setFormAlignment(Qt.AlignHCenter|Qt.AlignTop)
        self.nameLabel = QLabel(self.scrollAreaWidgetContents)
        self.nameLabel.setObjectName(u"nameLabel")
        font1 = QFont()
        font1.setPointSize(12)
        self.nameLabel.setFont(font1)

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.nameLabel)

        self.nameEdit = QLineEdit(self.scrollAreaWidgetContents)
        self.nameEdit.setObjectName(u"nameEdit")

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.nameEdit)

        self.typeLabel = QLabel(self.scrollAreaWidgetContents)
        self.typeLabel.setObjectName(u"typeLabel")
        self.typeLabel.setFont(font1)

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

        self.verticalLayout_2.addWidget(self.objectArea)

        self.componentWidget.addWidget(self.objectPage)
        self.tabbedPage = QWidget()
        self.tabbedPage.setObjectName(u"tabbedPage")
        self.verticalLayout_3 = QVBoxLayout(self.tabbedPage)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.tabWidget = QTabWidget(self.tabbedPage)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tabWidget.setTabPosition(QTabWidget.North)
        self.tabWidget.setUsesScrollButtons(False)
        self.translateTab = QWidget()
        self.translateTab.setObjectName(u"translateTab")
        self.tabWidget.addTab(self.translateTab, "")
        self.rotateTab = QWidget()
        self.rotateTab.setObjectName(u"rotateTab")
        self.tabWidget.addTab(self.rotateTab, "")
        self.scaleTab = QWidget()
        self.scaleTab.setObjectName(u"scaleTab")
        self.tabWidget.addTab(self.scaleTab, "")

        self.verticalLayout_3.addWidget(self.tabWidget)

        self.componentWidget.addWidget(self.tabbedPage)
        self.transformPage = QWidget()
        self.transformPage.setObjectName(u"transformPage")
        self.translate_x_label = QLabel(self.transformPage)
        self.translate_x_label.setObjectName(u"translate_x_label")
        self.translate_x_label.setGeometry(QRect(55, 30, 16, 16))
        self.angle_label = QLabel(self.transformPage)
        self.angle_label.setObjectName(u"angle_label")
        self.angle_label.setGeometry(QRect(145, 140, 41, 16))
        self.rotate_label = QLabel(self.transformPage)
        self.rotate_label.setObjectName(u"rotate_label")
        self.rotate_label.setGeometry(QRect(35, 120, 41, 16))
        self.translate_z_label = QLabel(self.transformPage)
        self.translate_z_label.setObjectName(u"translate_z_label")
        self.translate_z_label.setGeometry(QRect(55, 70, 16, 16))
        self.translate_y_label_2 = QLabel(self.transformPage)
        self.translate_y_label_2.setObjectName(u"translate_y_label_2")
        self.translate_y_label_2.setGeometry(QRect(55, 50, 16, 16))
        self.line_3 = QFrame(self.transformPage)
        self.line_3.setObjectName(u"line_3")
        self.line_3.setGeometry(QRect(15, 210, 281, 16))
        self.line_3.setFrameShape(QFrame.HLine)
        self.line_3.setFrameShadow(QFrame.Sunken)
        self.rotate_angle_input = QLineEdit(self.transformPage)
        self.rotate_angle_input.setObjectName(u"rotate_angle_input")
        self.rotate_angle_input.setGeometry(QRect(185, 140, 41, 21))
        self.axis_label = QLabel(self.transformPage)
        self.axis_label.setObjectName(u"axis_label")
        self.axis_label.setGeometry(QRect(45, 140, 31, 16))
        self.transate_label = QLabel(self.transformPage)
        self.transate_label.setObjectName(u"transate_label")
        self.transate_label.setGeometry(QRect(35, 10, 60, 16))
        self.translate_x = QLineEdit(self.transformPage)
        self.translate_x.setObjectName(u"translate_x")
        self.translate_x.setGeometry(QRect(75, 30, 113, 21))
        self.scale_label = QLabel(self.transformPage)
        self.scale_label.setObjectName(u"scale_label")
        self.scale_label.setGeometry(QRect(35, 170, 41, 16))
        self.translate_z = QLineEdit(self.transformPage)
        self.translate_z.setObjectName(u"translate_z")
        self.translate_z.setGeometry(QRect(75, 70, 113, 21))
        self.translate_z.setReadOnly(True)
        self.translate_y = QLineEdit(self.transformPage)
        self.translate_y.setObjectName(u"translate_y")
        self.translate_y.setGeometry(QRect(75, 50, 113, 21))
        self.trs_box_confirm = QDialogButtonBox(self.transformPage)
        self.trs_box_confirm.setObjectName(u"trs_box_confirm")
        self.trs_box_confirm.setGeometry(QRect(65, 235, 164, 32))
        self.trs_box_confirm.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Ok)
        self.line = QFrame(self.transformPage)
        self.line.setObjectName(u"line")
        self.line.setGeometry(QRect(15, 110, 281, 16))
        self.line.setFrameShape(QFrame.HLine)
        self.line.setFrameShadow(QFrame.Sunken)
        self.line_2 = QFrame(self.transformPage)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setGeometry(QRect(15, 160, 281, 16))
        self.line_2.setFrameShape(QFrame.HLine)
        self.line_2.setFrameShadow(QFrame.Sunken)
        self.rotate_axis_select = QComboBox(self.transformPage)
        self.rotate_axis_select.setObjectName(u"rotate_axis_select")
        self.rotate_axis_select.setGeometry(QRect(75, 140, 51, 26))
        self.componentWidget.addWidget(self.transformPage)

        self.gridLayout.addWidget(self.componentWidget, 2, 1, 2, 1)

        self.gridLayout.setRowStretch(0, 4)
        self.gridLayout.setRowStretch(1, 7)
        self.gridLayout.setRowStretch(2, 4)
        self.gridLayout.setRowStretch(3, 5)
        self.gridLayout.setColumnStretch(0, 4)
        self.gridLayout.setColumnStretch(1, 1)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.displayFile.setCurrentRow(-1)
        self.componentWidget.setCurrentIndex(0)
        self.typeBox.setCurrentIndex(-1)
        self.tabWidget.setCurrentIndex(1)


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
        self.label.setText(QCoreApplication.translate("MainWindow", u"To move an object, select it on the display file first", None))
        self.objectLabel.setText(QCoreApplication.translate("MainWindow", u"Object", None))
        self.nameLabel.setText(QCoreApplication.translate("MainWindow", u"Name:", None))
        self.typeLabel.setText(QCoreApplication.translate("MainWindow", u"Type:", None))
        self.typeBox.setItemText(0, QCoreApplication.translate("MainWindow", u"Point", None))
        self.typeBox.setItemText(1, QCoreApplication.translate("MainWindow", u"Line", None))
        self.typeBox.setItemText(2, QCoreApplication.translate("MainWindow", u"Wireframe", None))

        self.tabWidget.setTabText(self.tabWidget.indexOf(self.translateTab), QCoreApplication.translate("MainWindow", u"Translate", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.rotateTab), QCoreApplication.translate("MainWindow", u"Rotate", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.scaleTab), QCoreApplication.translate("MainWindow", u"Scale", None))
        self.translate_x_label.setText(QCoreApplication.translate("MainWindow", u"X:", None))
        self.angle_label.setText(QCoreApplication.translate("MainWindow", u"Angle:", None))
        self.rotate_label.setText(QCoreApplication.translate("MainWindow", u"Rotate", None))
        self.translate_z_label.setText(QCoreApplication.translate("MainWindow", u"Z:", None))
        self.translate_y_label_2.setText(QCoreApplication.translate("MainWindow", u"Y:", None))
        self.axis_label.setText(QCoreApplication.translate("MainWindow", u"Axis:", None))
        self.transate_label.setText(QCoreApplication.translate("MainWindow", u"Translate", None))
        self.scale_label.setText(QCoreApplication.translate("MainWindow", u"Scale", None))
    # retranslateUi

