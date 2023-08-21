# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'unitconv.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QFrame, QGridLayout,
    QLCDNumber, QLabel, QPushButton, QRadioButton,
    QSizePolicy, QVBoxLayout, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(450, 600)
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Form.sizePolicy().hasHeightForWidth())
        Form.setSizePolicy(sizePolicy)
        Form.setMinimumSize(QSize(450, 600))
        Form.setMaximumSize(QSize(450, 600))
        self.verticalLayout = QVBoxLayout(Form)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.gridLayout_2 = QGridLayout()
        self.gridLayout_2.setSpacing(20)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.radioButton_up = QRadioButton(Form)
        self.radioButton_up.setObjectName(u"radioButton_up")
        sizePolicy1 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.radioButton_up.sizePolicy().hasHeightForWidth())
        self.radioButton_up.setSizePolicy(sizePolicy1)
        self.radioButton_up.setLayoutDirection(Qt.RightToLeft)
        self.radioButton_up.setChecked(True)

        self.gridLayout_2.addWidget(self.radioButton_up, 0, 0, 1, 1)

        self.lcdNumber_up = QLCDNumber(Form)
        self.lcdNumber_up.setObjectName(u"lcdNumber_up")
        self.lcdNumber_up.setMinimumSize(QSize(300, 50))
        self.lcdNumber_up.setFrameShape(QFrame.Panel)
        self.lcdNumber_up.setDigitCount(9)
        self.lcdNumber_up.setSegmentStyle(QLCDNumber.Flat)

        self.gridLayout_2.addWidget(self.lcdNumber_up, 0, 1, 1, 1)

        self.comboBox_up = QComboBox(Form)
        self.comboBox_up.setObjectName(u"comboBox_up")
        sizePolicy1.setHeightForWidth(self.comboBox_up.sizePolicy().hasHeightForWidth())
        self.comboBox_up.setSizePolicy(sizePolicy1)
        self.comboBox_up.setMaximumSize(QSize(16777215, 16777215))

        self.gridLayout_2.addWidget(self.comboBox_up, 0, 3, 1, 1)

        self.radioButton_down = QRadioButton(Form)
        self.radioButton_down.setObjectName(u"radioButton_down")
        sizePolicy1.setHeightForWidth(self.radioButton_down.sizePolicy().hasHeightForWidth())
        self.radioButton_down.setSizePolicy(sizePolicy1)
        self.radioButton_down.setLayoutDirection(Qt.RightToLeft)

        self.gridLayout_2.addWidget(self.radioButton_down, 1, 0, 1, 1)

        self.lcdNumber_down = QLCDNumber(Form)
        self.lcdNumber_down.setObjectName(u"lcdNumber_down")
        self.lcdNumber_down.setMinimumSize(QSize(300, 50))
        self.lcdNumber_down.setFrameShape(QFrame.Panel)
        self.lcdNumber_down.setDigitCount(9)
        self.lcdNumber_down.setSegmentStyle(QLCDNumber.Flat)

        self.gridLayout_2.addWidget(self.lcdNumber_down, 1, 1, 1, 1)

        self.comboBox_down = QComboBox(Form)
        self.comboBox_down.setObjectName(u"comboBox_down")
        sizePolicy1.setHeightForWidth(self.comboBox_down.sizePolicy().hasHeightForWidth())
        self.comboBox_down.setSizePolicy(sizePolicy1)
        self.comboBox_down.setMaximumSize(QSize(16777215, 16777215))

        self.gridLayout_2.addWidget(self.comboBox_down, 1, 3, 1, 1)


        self.verticalLayout.addLayout(self.gridLayout_2)

        self.gridLayout = QGridLayout()
        self.gridLayout.setSpacing(15)
        self.gridLayout.setObjectName(u"gridLayout")
        self.pushButton_clr = QPushButton(Form)
        self.pushButton_clr.setObjectName(u"pushButton_clr")
        sizePolicy1.setHeightForWidth(self.pushButton_clr.sizePolicy().hasHeightForWidth())
        self.pushButton_clr.setSizePolicy(sizePolicy1)
        self.pushButton_clr.setMinimumSize(QSize(0, 30))

        self.gridLayout.addWidget(self.pushButton_clr, 0, 1, 1, 1)

        self.pushButton_del = QPushButton(Form)
        self.pushButton_del.setObjectName(u"pushButton_del")
        sizePolicy1.setHeightForWidth(self.pushButton_del.sizePolicy().hasHeightForWidth())
        self.pushButton_del.setSizePolicy(sizePolicy1)
        self.pushButton_del.setMinimumSize(QSize(0, 30))

        self.gridLayout.addWidget(self.pushButton_del, 0, 2, 1, 1)

        self.pushButton_7 = QPushButton(Form)
        self.pushButton_7.setObjectName(u"pushButton_7")
        sizePolicy1.setHeightForWidth(self.pushButton_7.sizePolicy().hasHeightForWidth())
        self.pushButton_7.setSizePolicy(sizePolicy1)
        self.pushButton_7.setMinimumSize(QSize(0, 30))

        self.gridLayout.addWidget(self.pushButton_7, 1, 0, 1, 1)

        self.pushButton_8 = QPushButton(Form)
        self.pushButton_8.setObjectName(u"pushButton_8")
        sizePolicy1.setHeightForWidth(self.pushButton_8.sizePolicy().hasHeightForWidth())
        self.pushButton_8.setSizePolicy(sizePolicy1)
        self.pushButton_8.setMinimumSize(QSize(0, 30))

        self.gridLayout.addWidget(self.pushButton_8, 1, 1, 1, 1)

        self.pushButton_9 = QPushButton(Form)
        self.pushButton_9.setObjectName(u"pushButton_9")
        sizePolicy1.setHeightForWidth(self.pushButton_9.sizePolicy().hasHeightForWidth())
        self.pushButton_9.setSizePolicy(sizePolicy1)
        self.pushButton_9.setMinimumSize(QSize(0, 30))

        self.gridLayout.addWidget(self.pushButton_9, 1, 2, 1, 1)

        self.pushButton_4 = QPushButton(Form)
        self.pushButton_4.setObjectName(u"pushButton_4")
        sizePolicy1.setHeightForWidth(self.pushButton_4.sizePolicy().hasHeightForWidth())
        self.pushButton_4.setSizePolicy(sizePolicy1)
        self.pushButton_4.setMinimumSize(QSize(0, 30))

        self.gridLayout.addWidget(self.pushButton_4, 2, 0, 1, 1)

        self.pushButton_5 = QPushButton(Form)
        self.pushButton_5.setObjectName(u"pushButton_5")
        sizePolicy1.setHeightForWidth(self.pushButton_5.sizePolicy().hasHeightForWidth())
        self.pushButton_5.setSizePolicy(sizePolicy1)
        self.pushButton_5.setMinimumSize(QSize(0, 30))

        self.gridLayout.addWidget(self.pushButton_5, 2, 1, 1, 1)

        self.pushButton_6 = QPushButton(Form)
        self.pushButton_6.setObjectName(u"pushButton_6")
        sizePolicy1.setHeightForWidth(self.pushButton_6.sizePolicy().hasHeightForWidth())
        self.pushButton_6.setSizePolicy(sizePolicy1)
        self.pushButton_6.setMinimumSize(QSize(0, 30))

        self.gridLayout.addWidget(self.pushButton_6, 2, 2, 1, 1)

        self.pushButton_1 = QPushButton(Form)
        self.pushButton_1.setObjectName(u"pushButton_1")
        sizePolicy1.setHeightForWidth(self.pushButton_1.sizePolicy().hasHeightForWidth())
        self.pushButton_1.setSizePolicy(sizePolicy1)
        self.pushButton_1.setMinimumSize(QSize(0, 30))

        self.gridLayout.addWidget(self.pushButton_1, 3, 0, 1, 1)

        self.pushButton_2 = QPushButton(Form)
        self.pushButton_2.setObjectName(u"pushButton_2")
        sizePolicy1.setHeightForWidth(self.pushButton_2.sizePolicy().hasHeightForWidth())
        self.pushButton_2.setSizePolicy(sizePolicy1)
        self.pushButton_2.setMinimumSize(QSize(0, 30))

        self.gridLayout.addWidget(self.pushButton_2, 3, 1, 1, 1)

        self.pushButton_3 = QPushButton(Form)
        self.pushButton_3.setObjectName(u"pushButton_3")
        sizePolicy1.setHeightForWidth(self.pushButton_3.sizePolicy().hasHeightForWidth())
        self.pushButton_3.setSizePolicy(sizePolicy1)
        self.pushButton_3.setMinimumSize(QSize(0, 30))

        self.gridLayout.addWidget(self.pushButton_3, 3, 2, 1, 1)

        self.pushButton_0 = QPushButton(Form)
        self.pushButton_0.setObjectName(u"pushButton_0")
        sizePolicy1.setHeightForWidth(self.pushButton_0.sizePolicy().hasHeightForWidth())
        self.pushButton_0.setSizePolicy(sizePolicy1)
        self.pushButton_0.setMinimumSize(QSize(0, 30))

        self.gridLayout.addWidget(self.pushButton_0, 4, 1, 1, 1)

        self.pushButton_dot = QPushButton(Form)
        self.pushButton_dot.setObjectName(u"pushButton_dot")
        sizePolicy1.setHeightForWidth(self.pushButton_dot.sizePolicy().hasHeightForWidth())
        self.pushButton_dot.setSizePolicy(sizePolicy1)
        self.pushButton_dot.setMinimumSize(QSize(0, 30))

        self.gridLayout.addWidget(self.pushButton_dot, 4, 2, 1, 1)

        self.comboBox_type = QComboBox(Form)
        self.comboBox_type.setObjectName(u"comboBox_type")
        sizePolicy1.setHeightForWidth(self.comboBox_type.sizePolicy().hasHeightForWidth())
        self.comboBox_type.setSizePolicy(sizePolicy1)
        font = QFont()
        font.setPointSize(10)
        self.comboBox_type.setFont(font)
        self.comboBox_type.setLayoutDirection(Qt.LeftToRight)

        self.gridLayout.addWidget(self.comboBox_type, 0, 0, 1, 1)

        self.label = QLabel(Form)
        self.label.setObjectName(u"label")
        font1 = QFont()
        font1.setFamilies([u"Euclid Fraktur"])
        font1.setPointSize(16)
        self.label.setFont(font1)
        self.label.setLayoutDirection(Qt.LeftToRight)
        self.label.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.label, 4, 0, 1, 1)


        self.verticalLayout.addLayout(self.gridLayout)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Unit Converter", None))
        self.radioButton_up.setText("")
        self.radioButton_down.setText("")
        self.pushButton_clr.setText(QCoreApplication.translate("Form", u"C", None))
        self.pushButton_del.setText(QCoreApplication.translate("Form", u"Del", None))
        self.pushButton_7.setText(QCoreApplication.translate("Form", u"7", None))
        self.pushButton_8.setText(QCoreApplication.translate("Form", u"8", None))
        self.pushButton_9.setText(QCoreApplication.translate("Form", u"9", None))
        self.pushButton_4.setText(QCoreApplication.translate("Form", u"4", None))
        self.pushButton_5.setText(QCoreApplication.translate("Form", u"5", None))
        self.pushButton_6.setText(QCoreApplication.translate("Form", u"6", None))
        self.pushButton_1.setText(QCoreApplication.translate("Form", u"1", None))
        self.pushButton_2.setText(QCoreApplication.translate("Form", u"2", None))
        self.pushButton_3.setText(QCoreApplication.translate("Form", u"3", None))
        self.pushButton_0.setText(QCoreApplication.translate("Form", u"0", None))
        self.pushButton_dot.setText(QCoreApplication.translate("Form", u".", None))
        self.comboBox_type.setCurrentText("")
        self.comboBox_type.setPlaceholderText(QCoreApplication.translate("Form", u"\u8f6c\u6362\u7c7b\u578b", None))
        self.label.setText(QCoreApplication.translate("Form", u"Wei Zeng", None))
    # retranslateUi

