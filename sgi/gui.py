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
        MainWindow.resize(830, 608)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.up_btn = QPushButton(self.centralwidget)
        self.up_btn.setObjectName(u"up_btn")
        self.up_btn.setGeometry(QRect(670, 210, 41, 25))
        self.left_btn = QPushButton(self.centralwidget)
        self.left_btn.setObjectName(u"left_btn")
        self.left_btn.setGeometry(QRect(630, 240, 41, 25))
        self.right_btn = QPushButton(self.centralwidget)
        self.right_btn.setObjectName(u"right_btn")
        self.right_btn.setGeometry(QRect(710, 240, 41, 25))
        self.down_btn = QPushButton(self.centralwidget)
        self.down_btn.setObjectName(u"down_btn")
        self.down_btn.setGeometry(QRect(670, 270, 41, 25))
        self.horizontalSlider = QSlider(self.centralwidget)
        self.horizontalSlider.setObjectName(u"horizontalSlider")
        self.horizontalSlider.setGeometry(QRect(610, 310, 160, 16))
        self.horizontalSlider.setOrientation(Qt.Horizontal)
        self.display_file = QListWidget(self.centralwidget)
        self.display_file.setObjectName(u"display_file")
        self.display_file.setGeometry(QRect(600, 10, 191, 171))
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.up_btn.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.left_btn.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.right_btn.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.down_btn.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
    # retranslateUi

