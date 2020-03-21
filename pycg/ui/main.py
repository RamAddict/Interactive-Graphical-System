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
        self.viewportLayout.setHorizontalSpacing(2)
        self.viewportLayout.setVerticalSpacing(0)
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
        self.instructionsLabel = QLabel(self.emptyPage)
        self.instructionsLabel.setObjectName(u"instructionsLabel")
        self.instructionsLabel.setGeometry(QRect(0, 0, 310, 271))
        font = QFont()
        font.setFamily(u"Verdana")
        font.setPointSize(15)
        font.setItalic(True)
        self.instructionsLabel.setFont(font)
        self.instructionsLabel.setAlignment(Qt.AlignCenter)
        self.instructionsLabel.setWordWrap(True)
        self.instructionsLabel.setMargin(5)
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
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 186, 123))
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
        self.translateXlabel = QLabel(self.transformPage)
        self.translateXlabel.setObjectName(u"translateXlabel")
        self.translateXlabel.setGeometry(QRect(85, 10, 16, 16))
        self.angleLabel = QLabel(self.transformPage)
        self.angleLabel.setObjectName(u"angleLabel")
        self.angleLabel.setGeometry(QRect(65, 105, 41, 16))
        self.rotateLabel = QLabel(self.transformPage)
        self.rotateLabel.setObjectName(u"rotateLabel")
        self.rotateLabel.setGeometry(QRect(10, 95, 41, 16))
        self.translateZlabel = QLabel(self.transformPage)
        self.translateZlabel.setObjectName(u"translateZlabel")
        self.translateZlabel.setGeometry(QRect(85, 55, 16, 16))
        self.translateYlabel = QLabel(self.transformPage)
        self.translateYlabel.setObjectName(u"translateYlabel")
        self.translateYlabel.setGeometry(QRect(85, 35, 16, 16))
        self.line_3 = QFrame(self.transformPage)
        self.line_3.setObjectName(u"line_3")
        self.line_3.setGeometry(QRect(10, 215, 286, 16))
        self.line_3.setFrameShape(QFrame.HLine)
        self.line_3.setFrameShadow(QFrame.Sunken)
        self.angleInput = QLineEdit(self.transformPage)
        self.angleInput.setObjectName(u"angleInput")
        self.angleInput.setGeometry(QRect(105, 100, 41, 21))
        self.axisLabel = QLabel(self.transformPage)
        self.axisLabel.setObjectName(u"axisLabel")
        self.axisLabel.setGeometry(QRect(165, 105, 31, 16))
        self.transateLabel = QLabel(self.transformPage)
        self.transateLabel.setObjectName(u"transateLabel")
        self.transateLabel.setGeometry(QRect(10, 5, 60, 16))
        self.translateXinput = QLineEdit(self.transformPage)
        self.translateXinput.setObjectName(u"translateXinput")
        self.translateXinput.setGeometry(QRect(105, 5, 113, 21))
        self.scaleLabel = QLabel(self.transformPage)
        self.scaleLabel.setObjectName(u"scaleLabel")
        self.scaleLabel.setGeometry(QRect(15, 140, 41, 16))
        self.translateZinput = QLineEdit(self.transformPage)
        self.translateZinput.setObjectName(u"translateZinput")
        self.translateZinput.setGeometry(QRect(105, 55, 113, 21))
        self.translateZinput.setReadOnly(True)
        self.translateYinput = QLineEdit(self.transformPage)
        self.translateYinput.setObjectName(u"translateYinput")
        self.translateYinput.setGeometry(QRect(105, 30, 113, 21))
        self.transformConfirm = QDialogButtonBox(self.transformPage)
        self.transformConfirm.setObjectName(u"transformConfirm")
        self.transformConfirm.setGeometry(QRect(65, 235, 164, 32))
        self.transformConfirm.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Ok)
        self.line = QFrame(self.transformPage)
        self.line.setObjectName(u"line")
        self.line.setGeometry(QRect(5, 80, 296, 16))
        self.line.setFrameShape(QFrame.HLine)
        self.line.setFrameShadow(QFrame.Sunken)
        self.line_2 = QFrame(self.transformPage)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setGeometry(QRect(5, 125, 296, 16))
        self.line_2.setFrameShape(QFrame.HLine)
        self.line_2.setFrameShadow(QFrame.Sunken)
        self.axisSelect = QComboBox(self.transformPage)
        self.axisSelect.addItem("")
        self.axisSelect.addItem("")
        self.axisSelect.addItem("")
        self.axisSelect.setObjectName(u"axisSelect")
        self.axisSelect.setGeometry(QRect(200, 100, 51, 26))
        self.scaleXlabel = QLabel(self.transformPage)
        self.scaleXlabel.setObjectName(u"scaleXlabel")
        self.scaleXlabel.setGeometry(QRect(85, 145, 16, 16))
        self.scaleYlabel = QLabel(self.transformPage)
        self.scaleYlabel.setObjectName(u"scaleYlabel")
        self.scaleYlabel.setGeometry(QRect(85, 170, 16, 16))
        self.scaleZlabel = QLabel(self.transformPage)
        self.scaleZlabel.setObjectName(u"scaleZlabel")
        self.scaleZlabel.setGeometry(QRect(85, 190, 16, 16))
        self.scaleXinput = QLineEdit(self.transformPage)
        self.scaleXinput.setObjectName(u"scaleXinput")
        self.scaleXinput.setGeometry(QRect(105, 140, 113, 21))
        self.scaleYinput = QLineEdit(self.transformPage)
        self.scaleYinput.setObjectName(u"scaleYinput")
        self.scaleYinput.setGeometry(QRect(105, 165, 113, 21))
        self.scaleZinput = QLineEdit(self.transformPage)
        self.scaleZinput.setObjectName(u"scaleZinput")
        self.scaleZinput.setGeometry(QRect(105, 190, 113, 21))
        self.scaleZinput.setReadOnly(True)
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
        self.tabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Interactive Graphical System - INE5420-CG - 2020/1", None))
#if QT_CONFIG(tooltip)
        self.sceneLabel.setToolTip(QCoreApplication.translate("MainWindow", u"Scene", None))
#endif // QT_CONFIG(tooltip)
        self.sceneLabel.setText(QCoreApplication.translate("MainWindow", u"Display File", None))
        self.newButton.setText(QCoreApplication.translate("MainWindow", u"New", None))
        self.editButton.setText(QCoreApplication.translate("MainWindow", u"Edit", None))
        self.removeButton.setText(QCoreApplication.translate("MainWindow", u"Remove", None))
        self.upListButton.setText(QCoreApplication.translate("MainWindow", u"Move Up", None))
        self.downListButton.setText(QCoreApplication.translate("MainWindow", u"Move Down", None))
        self.controlLabel.setText(QCoreApplication.translate("MainWindow", u"Window Controls", None))
        self.instructionsLabel.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>Use the scene buttons to manipulate the Display File.</p><p>The Window may be controlled using either the provided buttons, or mouse and keyboard bindings.</p><p>Select an object in the Display File to apply transformations to it.</p></body></html>", None))
        self.objectLabel.setText(QCoreApplication.translate("MainWindow", u"Object", None))
        self.nameLabel.setText(QCoreApplication.translate("MainWindow", u"Name:", None))
        self.typeLabel.setText(QCoreApplication.translate("MainWindow", u"Type:", None))
        self.typeBox.setItemText(0, QCoreApplication.translate("MainWindow", u"Point", None))
        self.typeBox.setItemText(1, QCoreApplication.translate("MainWindow", u"Line", None))
        self.typeBox.setItemText(2, QCoreApplication.translate("MainWindow", u"Wireframe", None))

        self.tabWidget.setTabText(self.tabWidget.indexOf(self.translateTab), QCoreApplication.translate("MainWindow", u"Translate", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.rotateTab), QCoreApplication.translate("MainWindow", u"Rotate", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.scaleTab), QCoreApplication.translate("MainWindow", u"Scale", None))
        self.translateXlabel.setText(QCoreApplication.translate("MainWindow", u"X:", None))
        self.angleLabel.setText(QCoreApplication.translate("MainWindow", u"Angle:", None))
        self.rotateLabel.setText(QCoreApplication.translate("MainWindow", u"Rotate", None))
        self.translateZlabel.setText(QCoreApplication.translate("MainWindow", u"Z:", None))
        self.translateYlabel.setText(QCoreApplication.translate("MainWindow", u"Y:", None))
        self.angleInput.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.axisLabel.setText(QCoreApplication.translate("MainWindow", u"Axis:", None))
        self.transateLabel.setText(QCoreApplication.translate("MainWindow", u"Translate", None))
        self.translateXinput.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.scaleLabel.setText(QCoreApplication.translate("MainWindow", u"Scale", None))
        self.translateZinput.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.translateYinput.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.axisSelect.setItemText(0, QCoreApplication.translate("MainWindow", u"X", None))
        self.axisSelect.setItemText(1, QCoreApplication.translate("MainWindow", u"Y", None))
        self.axisSelect.setItemText(2, QCoreApplication.translate("MainWindow", u"Z", None))

        self.scaleXlabel.setText(QCoreApplication.translate("MainWindow", u"X:", None))
        self.scaleYlabel.setText(QCoreApplication.translate("MainWindow", u"Y:", None))
        self.scaleZlabel.setText(QCoreApplication.translate("MainWindow", u"Z:", None))
        self.scaleXinput.setText(QCoreApplication.translate("MainWindow", u"1", None))
        self.scaleYinput.setText(QCoreApplication.translate("MainWindow", u"1", None))
        self.scaleZinput.setText(QCoreApplication.translate("MainWindow", u"1", None))
    # retranslateUi

