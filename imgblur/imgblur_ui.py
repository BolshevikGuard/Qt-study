# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'imgblur.ui'
##
## Created by: Qt User Interface Compiler version 6.5.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QComboBox, QHBoxLayout, QLabel,
    QPushButton, QSizePolicy, QSlider, QSpacerItem,
    QVBoxLayout, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(939, 685)
        sizePolicy = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Form.sizePolicy().hasHeightForWidth())
        Form.setSizePolicy(sizePolicy)
        Form.setMinimumSize(QSize(250, 300))
        self.verticalLayout = QVBoxLayout(Form)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.comboBox = QComboBox(Form)
        self.comboBox.setObjectName(u"comboBox")
        sizePolicy1 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.comboBox.sizePolicy().hasHeightForWidth())
        self.comboBox.setSizePolicy(sizePolicy1)
        self.comboBox.setMinimumSize(QSize(70, 20))
        self.comboBox.setMaximumSize(QSize(70, 20))

        self.horizontalLayout.addWidget(self.comboBox)

        self.pushButton_open = QPushButton(Form)
        self.pushButton_open.setObjectName(u"pushButton_open")
        sizePolicy1.setHeightForWidth(self.pushButton_open.sizePolicy().hasHeightForWidth())
        self.pushButton_open.setSizePolicy(sizePolicy1)
        self.pushButton_open.setMinimumSize(QSize(70, 20))
        self.pushButton_open.setMaximumSize(QSize(70, 20))

        self.horizontalLayout.addWidget(self.pushButton_open)

        self.pushButton_save = QPushButton(Form)
        self.pushButton_save.setObjectName(u"pushButton_save")
        sizePolicy1.setHeightForWidth(self.pushButton_save.sizePolicy().hasHeightForWidth())
        self.pushButton_save.setSizePolicy(sizePolicy1)
        self.pushButton_save.setMinimumSize(QSize(70, 20))
        self.pushButton_save.setMaximumSize(QSize(70, 20))

        self.horizontalLayout.addWidget(self.pushButton_save)

        self.horizontalSpacer = QSpacerItem(158, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.picLabel = QLabel(Form)
        self.picLabel.setObjectName(u"picLabel")
        sizePolicy2 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.picLabel.sizePolicy().hasHeightForWidth())
        self.picLabel.setSizePolicy(sizePolicy2)

        self.verticalLayout.addWidget(self.picLabel)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label = QLabel(Form)
        self.label.setObjectName(u"label")
        sizePolicy1.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy1)
        self.label.setMinimumSize(QSize(54, 20))
        self.label.setMaximumSize(QSize(54, 20))
        font = QFont()
        font.setFamilies([u"Euclid Fraktur"])
        font.setPointSize(10)
        self.label.setFont(font)

        self.horizontalLayout_2.addWidget(self.label)

        self.blurSlider = QSlider(Form)
        self.blurSlider.setObjectName(u"blurSlider")
        self.blurSlider.setMaximum(20)
        self.blurSlider.setPageStep(1)
        self.blurSlider.setOrientation(Qt.Horizontal)
        self.blurSlider.setInvertedAppearance(False)
        self.blurSlider.setTickPosition(QSlider.TicksBelow)
        self.blurSlider.setTickInterval(2)

        self.horizontalLayout_2.addWidget(self.blurSlider)


        self.verticalLayout.addLayout(self.horizontalLayout_2)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Image Blurer", None))
        self.comboBox.setCurrentText("")
        self.comboBox.setPlaceholderText(QCoreApplication.translate("Form", u"Type", None))
        self.pushButton_open.setText(QCoreApplication.translate("Form", u"Open", None))
        self.pushButton_save.setText(QCoreApplication.translate("Form", u"Save", None))
        self.picLabel.setText("")
        self.label.setText(QCoreApplication.translate("Form", u"Wei Zeng", None))
    # retranslateUi

