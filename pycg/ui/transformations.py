# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'transformations.ui'
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


class Ui_trs_box(object):
    def setupUi(self, trs_box):
        if trs_box.objectName():
            trs_box.setObjectName(u"trs_box")
        trs_box.resize(200, 356)
        self.translate_x_label = QLabel(trs_box)
        self.translate_x_label.setObjectName(u"translate_x_label")
        self.translate_x_label.setGeometry(QRect(40, 30, 16, 16))
        self.translate_y_label_2 = QLabel(trs_box)
        self.translate_y_label_2.setObjectName(u"translate_y_label_2")
        self.translate_y_label_2.setGeometry(QRect(40, 50, 16, 16))
        self.translate_z_label = QLabel(trs_box)
        self.translate_z_label.setObjectName(u"translate_z_label")
        self.translate_z_label.setGeometry(QRect(40, 70, 16, 16))
        self.transate_label = QLabel(trs_box)
        self.transate_label.setObjectName(u"transate_label")
        self.transate_label.setGeometry(QRect(20, 10, 60, 16))
        self.rotate_label = QLabel(trs_box)
        self.rotate_label.setObjectName(u"rotate_label")
        self.rotate_label.setGeometry(QRect(20, 120, 41, 16))
        self.rotate_axis_select = QComboBox(trs_box)
        self.rotate_axis_select.setObjectName(u"rotate_axis_select")
        self.rotate_axis_select.setGeometry(QRect(60, 140, 51, 26))
        self.axis_label = QLabel(trs_box)
        self.axis_label.setObjectName(u"axis_label")
        self.axis_label.setGeometry(QRect(30, 140, 31, 16))
        self.line = QFrame(trs_box)
        self.line.setObjectName(u"line")
        self.line.setGeometry(QRect(0, 110, 281, 16))
        self.line.setFrameShape(QFrame.HLine)
        self.line.setFrameShadow(QFrame.Sunken)
        self.line_2 = QFrame(trs_box)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setGeometry(QRect(0, 160, 281, 16))
        self.line_2.setFrameShape(QFrame.HLine)
        self.line_2.setFrameShadow(QFrame.Sunken)
        self.scale_label = QLabel(trs_box)
        self.scale_label.setObjectName(u"scale_label")
        self.scale_label.setGeometry(QRect(20, 170, 41, 16))
        self.translate_x = QLineEdit(trs_box)
        self.translate_x.setObjectName(u"translate_x")
        self.translate_x.setGeometry(QRect(60, 30, 113, 21))
        self.translate_y = QLineEdit(trs_box)
        self.translate_y.setObjectName(u"translate_y")
        self.translate_y.setGeometry(QRect(60, 50, 113, 21))
        self.translate_z = QLineEdit(trs_box)
        self.translate_z.setObjectName(u"translate_z")
        self.translate_z.setGeometry(QRect(60, 70, 113, 21))
        self.translate_z.setReadOnly(True)
        self.rotate_angle_input = QLineEdit(trs_box)
        self.rotate_angle_input.setObjectName(u"rotate_angle_input")
        self.rotate_angle_input.setGeometry(QRect(170, 140, 41, 21))
        self.angle_label = QLabel(trs_box)
        self.angle_label.setObjectName(u"angle_label")
        self.angle_label.setGeometry(QRect(130, 140, 41, 16))
        self.line_3 = QFrame(trs_box)
        self.line_3.setObjectName(u"line_3")
        self.line_3.setGeometry(QRect(0, 260, 281, 16))
        self.line_3.setFrameShape(QFrame.HLine)
        self.line_3.setFrameShadow(QFrame.Sunken)
        self.trs_box_confirm = QDialogButtonBox(trs_box)
        self.trs_box_confirm.setObjectName(u"trs_box_confirm")
        self.trs_box_confirm.setGeometry(QRect(50, 270, 164, 32))
        self.trs_box_confirm.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Ok)

        self.retranslateUi(trs_box)

        QMetaObject.connectSlotsByName(trs_box)
    # setupUi

    def retranslateUi(self, trs_box):
        trs_box.setWindowTitle(QCoreApplication.translate("trs_box", u"TRS box", None))
        self.translate_x_label.setText(QCoreApplication.translate("trs_box", u"X:", None))
        self.translate_y_label_2.setText(QCoreApplication.translate("trs_box", u"Y:", None))
        self.translate_z_label.setText(QCoreApplication.translate("trs_box", u"Z:", None))
        self.transate_label.setText(QCoreApplication.translate("trs_box", u"Translate", None))
        self.rotate_label.setText(QCoreApplication.translate("trs_box", u"Rotate", None))
        self.axis_label.setText(QCoreApplication.translate("trs_box", u"Axis:", None))
        self.scale_label.setText(QCoreApplication.translate("trs_box", u"Scale", None))
        self.angle_label.setText(QCoreApplication.translate("trs_box", u"Angle:", None))
    # retranslateUi

