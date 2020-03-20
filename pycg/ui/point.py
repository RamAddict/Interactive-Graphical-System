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
        PointFields.setLayoutDirection(Qt.RightToLeft)
        self.horizontalLayout = QHBoxLayout(PointFields)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.yHorizontalLayout = QHBoxLayout()
        self.yHorizontalLayout.setObjectName(u"yHorizontalLayout")
        self.yDoubleSpinBox = QDoubleSpinBox(PointFields)
        self.yDoubleSpinBox.setObjectName(u"yDoubleSpinBox")
        sizePolicy = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.yDoubleSpinBox.sizePolicy().hasHeightForWidth())
        self.yDoubleSpinBox.setSizePolicy(sizePolicy)
        self.yDoubleSpinBox.setDecimals(0)

        self.yHorizontalLayout.addWidget(self.yDoubleSpinBox)

        self.yLabel = QLabel(PointFields)
        self.yLabel.setObjectName(u"yLabel")
        font = QFont()
        font.setPointSize(12)
        self.yLabel.setFont(font)

        self.yHorizontalLayout.addWidget(self.yLabel)


        self.horizontalLayout.addLayout(self.yHorizontalLayout)

        self.xHorizontalLayout = QHBoxLayout()
        self.xHorizontalLayout.setObjectName(u"xHorizontalLayout")
        self.xDoubleSpinBox = QDoubleSpinBox(PointFields)
        self.xDoubleSpinBox.setObjectName(u"xDoubleSpinBox")
        sizePolicy.setHeightForWidth(self.xDoubleSpinBox.sizePolicy().hasHeightForWidth())
        self.xDoubleSpinBox.setSizePolicy(sizePolicy)
        self.xDoubleSpinBox.setDecimals(0)

        self.xHorizontalLayout.addWidget(self.xDoubleSpinBox)

        self.xLabel = QLabel(PointFields)
        self.xLabel.setObjectName(u"xLabel")
        self.xLabel.setFont(font)

        self.xHorizontalLayout.addWidget(self.xLabel)


        self.horizontalLayout.addLayout(self.xHorizontalLayout)

        self.actionButton = QPushButton(PointFields)
        self.actionButton.setObjectName(u"actionButton")
        self.actionButton.setEnabled(False)
        self.actionButton.setMaximumSize(QSize(32, 16777215))
        self.actionButton.setFlat(True)

        self.horizontalLayout.addWidget(self.actionButton)


        self.retranslateUi(PointFields)

        QMetaObject.connectSlotsByName(PointFields)
    # setupUi

    def retranslateUi(self, PointFields):
        self.yLabel.setText(QCoreApplication.translate("PointFields", u"Y:", None))
        self.xLabel.setText(QCoreApplication.translate("PointFields", u"X:", None))
        self.actionButton.setText("")
    # retranslateUi

