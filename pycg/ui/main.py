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
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 294, 271))
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
        self.transformPage = QWidget()
        self.transformPage.setObjectName(u"transformPage")
        self.translateXlabel = QLabel(self.transformPage)
        self.translateXlabel.setObjectName(u"translateXlabel")
        self.translateXlabel.setGeometry(QRect(85, 5, 16, 21))
        self.translateXlabel.setAlignment(Qt.AlignCenter)
        self.angleLabel = QLabel(self.transformPage)
        self.angleLabel.setObjectName(u"angleLabel")
        self.angleLabel.setGeometry(QRect(20, 115, 56, 21))
        self.angleLabel.setAlignment(Qt.AlignCenter)
        self.rotateLabel = QLabel(self.transformPage)
        self.rotateLabel.setObjectName(u"rotateLabel")
        self.rotateLabel.setGeometry(QRect(10, 85, 42, 16))
        self.translateYlabel = QLabel(self.transformPage)
        self.translateYlabel.setObjectName(u"translateYlabel")
        self.translateYlabel.setGeometry(QRect(85, 30, 16, 21))
        self.translateYlabel.setAlignment(Qt.AlignCenter)
        self.line = QFrame(self.transformPage)
        self.line.setObjectName(u"line")
        self.line.setGeometry(QRect(0, 65, 296, 16))
        self.line.setFrameShape(QFrame.HLine)
        self.line.setFrameShadow(QFrame.Sunken)
        self.angleInput = QLineEdit(self.transformPage)
        self.angleInput.setObjectName(u"angleInput")
        self.angleInput.setGeometry(QRect(75, 115, 56, 21))
        self.pivotLabel = QLabel(self.transformPage)
        self.pivotLabel.setObjectName(u"pivotLabel")
        self.pivotLabel.setGeometry(QRect(140, 110, 41, 26))
        self.pivotLabel.setAlignment(Qt.AlignCenter)
        self.transateLabel = QLabel(self.transformPage)
        self.transateLabel.setObjectName(u"transateLabel")
        self.transateLabel.setGeometry(QRect(10, 5, 60, 16))
        self.translateXinput = QLineEdit(self.transformPage)
        self.translateXinput.setObjectName(u"translateXinput")
        self.translateXinput.setGeometry(QRect(105, 5, 113, 21))
        self.scaleLabel = QLabel(self.transformPage)
        self.scaleLabel.setObjectName(u"scaleLabel")
        self.scaleLabel.setGeometry(QRect(10, 160, 42, 16))
        self.translateYinput = QLineEdit(self.transformPage)
        self.translateYinput.setObjectName(u"translateYinput")
        self.translateYinput.setGeometry(QRect(105, 30, 113, 21))
        self.transformConfirm = QDialogButtonBox(self.transformPage)
        self.transformConfirm.setObjectName(u"transformConfirm")
        self.transformConfirm.setGeometry(QRect(65, 255, 164, 32))
        self.transformConfirm.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Ok)
        self.line_3 = QFrame(self.transformPage)
        self.line_3.setObjectName(u"line_3")
        self.line_3.setGeometry(QRect(0, 230, 296, 16))
        self.line_3.setFrameShape(QFrame.HLine)
        self.line_3.setFrameShadow(QFrame.Sunken)
        self.line_2 = QFrame(self.transformPage)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setGeometry(QRect(0, 145, 296, 16))
        self.line_2.setFrameShape(QFrame.HLine)
        self.line_2.setFrameShadow(QFrame.Sunken)
        self.pivotSelect = QComboBox(self.transformPage)
        self.pivotSelect.addItem("")
        self.pivotSelect.addItem("")
        self.pivotSelect.setObjectName(u"pivotSelect")
        self.pivotSelect.setGeometry(QRect(185, 110, 96, 26))
        self.scaleXlabel = QLabel(self.transformPage)
        self.scaleXlabel.setObjectName(u"scaleXlabel")
        self.scaleXlabel.setGeometry(QRect(85, 175, 16, 21))
        self.scaleXlabel.setAlignment(Qt.AlignCenter)
        self.scaleYlabel = QLabel(self.transformPage)
        self.scaleYlabel.setObjectName(u"scaleYlabel")
        self.scaleYlabel.setGeometry(QRect(85, 200, 16, 21))
        self.scaleYlabel.setAlignment(Qt.AlignCenter)
        self.scaleXinput = QLineEdit(self.transformPage)
        self.scaleXinput.setObjectName(u"scaleXinput")
        self.scaleXinput.setGeometry(QRect(105, 175, 113, 21))
        self.scaleYinput = QLineEdit(self.transformPage)
        self.scaleYinput.setObjectName(u"scaleYinput")
        self.scaleYinput.setGeometry(QRect(105, 200, 113, 21))
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
        self.componentWidget.setCurrentIndex(2)
        self.typeBox.setCurrentIndex(-1)
        self.pivotSelect.setCurrentIndex(0)


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
        self.instructionsLabel.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-style:normal;\">Use the scene buttons to manipulate the Display File and its drawable objects.</span></p><p><span style=\" font-style:normal;\">The Window may be controlled using either the provided buttons, or mouse and keyboard bindings (WASD, Ctrl + -/=/Wheel, Middle Click &amp; Drag).</span></p></body></html>", None))
        self.objectLabel.setText(QCoreApplication.translate("MainWindow", u"Object", None))
        self.nameLabel.setText(QCoreApplication.translate("MainWindow", u"Name:", None))
        self.typeLabel.setText(QCoreApplication.translate("MainWindow", u"Type:", None))
        self.typeBox.setItemText(0, QCoreApplication.translate("MainWindow", u"Point", None))
        self.typeBox.setItemText(1, QCoreApplication.translate("MainWindow", u"Line", None))
        self.typeBox.setItemText(2, QCoreApplication.translate("MainWindow", u"Wireframe", None))

        self.translateXlabel.setText(QCoreApplication.translate("MainWindow", u"X:", None))
        self.angleLabel.setText(QCoreApplication.translate("MainWindow", u"Angle: \u00b0", None))
        self.rotateLabel.setText(QCoreApplication.translate("MainWindow", u"Rotate", None))
        self.translateYlabel.setText(QCoreApplication.translate("MainWindow", u"Y:", None))
        self.angleInput.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.pivotLabel.setText(QCoreApplication.translate("MainWindow", u"Pivot:", None))
        self.transateLabel.setText(QCoreApplication.translate("MainWindow", u"Translate", None))
        self.translateXinput.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.scaleLabel.setText(QCoreApplication.translate("MainWindow", u"Scale", None))
        self.translateYinput.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.pivotSelect.setItemText(0, QCoreApplication.translate("MainWindow", u"Center", None))
        self.pivotSelect.setItemText(1, QCoreApplication.translate("MainWindow", u"Origin", None))

        self.scaleXlabel.setText(QCoreApplication.translate("MainWindow", u"X:", None))
        self.scaleYlabel.setText(QCoreApplication.translate("MainWindow", u"Y:", None))
        self.scaleXinput.setText(QCoreApplication.translate("MainWindow", u"1", None))
        self.scaleYinput.setText(QCoreApplication.translate("MainWindow", u"1", None))
    # retranslateUi

