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


class Ui_PointFields(object):
    def setupUi(self, PointFields):
        if PointFields.objectName():
            PointFields.setObjectName(u"PointFields")
        PointFields.resize(272, 34)
        PointFields.setLayoutDirection(Qt.LeftToRight)
        self.horizontalLayout = QHBoxLayout(PointFields)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.actionButton = QPushButton(PointFields)
        self.actionButton.setObjectName(u"actionButton")
        self.actionButton.setMaximumSize(QSize(32, 16777215))
        icon = QIcon(QIcon.fromTheme(u"list-remove"))
        self.actionButton.setIcon(icon)
        self.actionButton.setIconSize(QSize(16, 16))
        self.actionButton.setFlat(True)

        self.horizontalLayout.addWidget(self.actionButton)

        self.xHorizontalLayout = QHBoxLayout()
        self.xHorizontalLayout.setObjectName(u"xHorizontalLayout")
        self.xLabel = QLabel(PointFields)
        self.xLabel.setObjectName(u"xLabel")
        font = QFont()
        font.setPointSize(12)
        self.xLabel.setFont(font)

        self.xHorizontalLayout.addWidget(self.xLabel)

        self.xDoubleSpinBox = QDoubleSpinBox(PointFields)
        self.xDoubleSpinBox.setObjectName(u"xDoubleSpinBox")
        sizePolicy = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.xDoubleSpinBox.sizePolicy().hasHeightForWidth())
        self.xDoubleSpinBox.setSizePolicy(sizePolicy)
        self.xDoubleSpinBox.setDecimals(4)

        self.xHorizontalLayout.addWidget(self.xDoubleSpinBox)


        self.horizontalLayout.addLayout(self.xHorizontalLayout)

        self.yHorizontalLayout = QHBoxLayout()
        self.yHorizontalLayout.setObjectName(u"yHorizontalLayout")
        self.yLabel = QLabel(PointFields)
        self.yLabel.setObjectName(u"yLabel")
        self.yLabel.setFont(font)

        self.yHorizontalLayout.addWidget(self.yLabel)

        self.yDoubleSpinBox = QDoubleSpinBox(PointFields)
        self.yDoubleSpinBox.setObjectName(u"yDoubleSpinBox")
        sizePolicy.setHeightForWidth(self.yDoubleSpinBox.sizePolicy().hasHeightForWidth())
        self.yDoubleSpinBox.setSizePolicy(sizePolicy)
        self.yDoubleSpinBox.setDecimals(4)

        self.yHorizontalLayout.addWidget(self.yDoubleSpinBox)


        self.horizontalLayout.addLayout(self.yHorizontalLayout)


        self.retranslateUi(PointFields)

        QMetaObject.connectSlotsByName(PointFields)
    # setupUi

    def retranslateUi(self, PointFields):
        PointFields.setWindowTitle(QCoreApplication.translate("PointFields", u"Form", None))
        self.actionButton.setText("")
        self.xLabel.setText(QCoreApplication.translate("PointFields", u"X:", None))
        self.yLabel.setText(QCoreApplication.translate("PointFields", u"Y:", None))
    # retranslateUi

