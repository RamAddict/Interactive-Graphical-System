# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'point.ui'
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


class Ui_PointForm(object):
    def setupUi(self, PointForm):
        if PointForm.objectName():
            PointForm.setObjectName(u"PointForm")
        PointForm.resize(272, 34)
        self.horizontalLayout = QHBoxLayout(PointForm)
        self.horizontalLayout.setSpacing(6)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.xHorizontalLayout = QHBoxLayout()
        self.xHorizontalLayout.setObjectName(u"xHorizontalLayout")
        self.xLabel = QLabel(PointForm)
        self.xLabel.setObjectName(u"xLabel")
        font = QFont()
        font.setPointSize(12)
        self.xLabel.setFont(font)

        self.xHorizontalLayout.addWidget(self.xLabel)

        self.xDoubleSpinBox = QDoubleSpinBox(PointForm)
        self.xDoubleSpinBox.setObjectName(u"xDoubleSpinBox")
        self.xDoubleSpinBox.setDecimals(0)

        self.xHorizontalLayout.addWidget(self.xDoubleSpinBox)

        self.xHorizontalLayout.setStretch(1, 1)

        self.horizontalLayout.addLayout(self.xHorizontalLayout)

        self.yHorizontalLayout = QHBoxLayout()
        self.yHorizontalLayout.setObjectName(u"yHorizontalLayout")
        self.yLabel = QLabel(PointForm)
        self.yLabel.setObjectName(u"yLabel")
        self.yLabel.setFont(font)

        self.yHorizontalLayout.addWidget(self.yLabel)

        self.yDoubleSpinBox = QDoubleSpinBox(PointForm)
        self.yDoubleSpinBox.setObjectName(u"yDoubleSpinBox")
        self.yDoubleSpinBox.setDecimals(0)

        self.yHorizontalLayout.addWidget(self.yDoubleSpinBox)

        self.yHorizontalLayout.setStretch(1, 1)

        self.horizontalLayout.addLayout(self.yHorizontalLayout)


        self.retranslateUi(PointForm)

        QMetaObject.connectSlotsByName(PointForm)
    # setupUi

    def retranslateUi(self, PointForm):
        PointForm.setWindowTitle(QCoreApplication.translate("PointForm", u"Form", None))
        self.xLabel.setText(QCoreApplication.translate("PointForm", u"X:", None))
        self.yLabel.setText(QCoreApplication.translate("PointForm", u"Y:", None))
    # retranslateUi

