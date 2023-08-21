# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'calculator.ui'
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
from PySide6.QtWidgets import (QApplication, QDialog, QGridLayout, QLCDNumber,
    QPushButton, QSizePolicy, QVBoxLayout, QWidget)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(338, 272)
        self.verticalLayout_2 = QVBoxLayout(Dialog)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(-1, -1, -1, 0)
        self.lcdNumber = QLCDNumber(Dialog)
        self.lcdNumber.setObjectName(u"lcdNumber")
        sizePolicy = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lcdNumber.sizePolicy().hasHeightForWidth())
        self.lcdNumber.setSizePolicy(sizePolicy)
        self.lcdNumber.setMinimumSize(QSize(0, 100))
        self.lcdNumber.setMaximumSize(QSize(16777215, 16777215))
        self.lcdNumber.setSmallDecimalPoint(False)
        self.lcdNumber.setDigitCount(10)
        self.lcdNumber.setProperty("value", 0.000000000000000)
        self.lcdNumber.setProperty("intValue", 0)

        self.verticalLayout.addWidget(self.lcdNumber)


        self.verticalLayout_2.addLayout(self.verticalLayout)

        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.pushButton_6 = QPushButton(Dialog)
        self.pushButton_6.setObjectName(u"pushButton_6")
        sizePolicy.setHeightForWidth(self.pushButton_6.sizePolicy().hasHeightForWidth())
        self.pushButton_6.setSizePolicy(sizePolicy)

        self.gridLayout.addWidget(self.pushButton_6, 2, 2, 1, 1)

        self.pushButton_8 = QPushButton(Dialog)
        self.pushButton_8.setObjectName(u"pushButton_8")
        sizePolicy.setHeightForWidth(self.pushButton_8.sizePolicy().hasHeightForWidth())
        self.pushButton_8.setSizePolicy(sizePolicy)

        self.gridLayout.addWidget(self.pushButton_8, 1, 1, 1, 1)

        self.pushButton_7 = QPushButton(Dialog)
        self.pushButton_7.setObjectName(u"pushButton_7")
        sizePolicy.setHeightForWidth(self.pushButton_7.sizePolicy().hasHeightForWidth())
        self.pushButton_7.setSizePolicy(sizePolicy)

        self.gridLayout.addWidget(self.pushButton_7, 1, 0, 1, 1)

        self.pushButton_Dot = QPushButton(Dialog)
        self.pushButton_Dot.setObjectName(u"pushButton_Dot")
        sizePolicy.setHeightForWidth(self.pushButton_Dot.sizePolicy().hasHeightForWidth())
        self.pushButton_Dot.setSizePolicy(sizePolicy)

        self.gridLayout.addWidget(self.pushButton_Dot, 4, 2, 1, 1)

        self.pushButton_9 = QPushButton(Dialog)
        self.pushButton_9.setObjectName(u"pushButton_9")
        sizePolicy.setHeightForWidth(self.pushButton_9.sizePolicy().hasHeightForWidth())
        self.pushButton_9.setSizePolicy(sizePolicy)

        self.gridLayout.addWidget(self.pushButton_9, 1, 2, 1, 1)

        self.pushButton_1 = QPushButton(Dialog)
        self.pushButton_1.setObjectName(u"pushButton_1")
        sizePolicy.setHeightForWidth(self.pushButton_1.sizePolicy().hasHeightForWidth())
        self.pushButton_1.setSizePolicy(sizePolicy)

        self.gridLayout.addWidget(self.pushButton_1, 3, 2, 1, 1)

        self.pushButton_Alt = QPushButton(Dialog)
        self.pushButton_Alt.setObjectName(u"pushButton_Alt")
        self.pushButton_Alt.setEnabled(False)
        sizePolicy.setHeightForWidth(self.pushButton_Alt.sizePolicy().hasHeightForWidth())
        self.pushButton_Alt.setSizePolicy(sizePolicy)

        self.gridLayout.addWidget(self.pushButton_Alt, 4, 0, 1, 1)

        self.pushButton_0 = QPushButton(Dialog)
        self.pushButton_0.setObjectName(u"pushButton_0")
        sizePolicy.setHeightForWidth(self.pushButton_0.sizePolicy().hasHeightForWidth())
        self.pushButton_0.setSizePolicy(sizePolicy)

        self.gridLayout.addWidget(self.pushButton_0, 4, 1, 1, 1)

        self.pushButton_5 = QPushButton(Dialog)
        self.pushButton_5.setObjectName(u"pushButton_5")
        sizePolicy.setHeightForWidth(self.pushButton_5.sizePolicy().hasHeightForWidth())
        self.pushButton_5.setSizePolicy(sizePolicy)

        self.gridLayout.addWidget(self.pushButton_5, 2, 1, 1, 1)

        self.pushButton_Clr = QPushButton(Dialog)
        self.pushButton_Clr.setObjectName(u"pushButton_Clr")
        sizePolicy.setHeightForWidth(self.pushButton_Clr.sizePolicy().hasHeightForWidth())
        self.pushButton_Clr.setSizePolicy(sizePolicy)

        self.gridLayout.addWidget(self.pushButton_Clr, 0, 0, 1, 1)

        self.pushButton_Del = QPushButton(Dialog)
        self.pushButton_Del.setObjectName(u"pushButton_Del")
        sizePolicy.setHeightForWidth(self.pushButton_Del.sizePolicy().hasHeightForWidth())
        self.pushButton_Del.setSizePolicy(sizePolicy)

        self.gridLayout.addWidget(self.pushButton_Del, 0, 1, 1, 1)

        self.pushButton_4 = QPushButton(Dialog)
        self.pushButton_4.setObjectName(u"pushButton_4")
        sizePolicy.setHeightForWidth(self.pushButton_4.sizePolicy().hasHeightForWidth())
        self.pushButton_4.setSizePolicy(sizePolicy)

        self.gridLayout.addWidget(self.pushButton_4, 2, 0, 1, 1)

        self.pushButton_3 = QPushButton(Dialog)
        self.pushButton_3.setObjectName(u"pushButton_3")
        sizePolicy.setHeightForWidth(self.pushButton_3.sizePolicy().hasHeightForWidth())
        self.pushButton_3.setSizePolicy(sizePolicy)

        self.gridLayout.addWidget(self.pushButton_3, 3, 0, 1, 1)

        self.pushButton_2 = QPushButton(Dialog)
        self.pushButton_2.setObjectName(u"pushButton_2")
        sizePolicy.setHeightForWidth(self.pushButton_2.sizePolicy().hasHeightForWidth())
        self.pushButton_2.setSizePolicy(sizePolicy)

        self.gridLayout.addWidget(self.pushButton_2, 3, 1, 1, 1)

        self.pushButton_Per = QPushButton(Dialog)
        self.pushButton_Per.setObjectName(u"pushButton_Per")
        self.pushButton_Per.setEnabled(False)
        sizePolicy.setHeightForWidth(self.pushButton_Per.sizePolicy().hasHeightForWidth())
        self.pushButton_Per.setSizePolicy(sizePolicy)

        self.gridLayout.addWidget(self.pushButton_Per, 0, 2, 1, 1)

        self.pushButton_Div = QPushButton(Dialog)
        self.pushButton_Div.setObjectName(u"pushButton_Div")
        sizePolicy.setHeightForWidth(self.pushButton_Div.sizePolicy().hasHeightForWidth())
        self.pushButton_Div.setSizePolicy(sizePolicy)

        self.gridLayout.addWidget(self.pushButton_Div, 0, 3, 1, 1)

        self.pushButton_Tim = QPushButton(Dialog)
        self.pushButton_Tim.setObjectName(u"pushButton_Tim")
        sizePolicy.setHeightForWidth(self.pushButton_Tim.sizePolicy().hasHeightForWidth())
        self.pushButton_Tim.setSizePolicy(sizePolicy)

        self.gridLayout.addWidget(self.pushButton_Tim, 1, 3, 1, 1)

        self.pushButton_Min = QPushButton(Dialog)
        self.pushButton_Min.setObjectName(u"pushButton_Min")
        sizePolicy.setHeightForWidth(self.pushButton_Min.sizePolicy().hasHeightForWidth())
        self.pushButton_Min.setSizePolicy(sizePolicy)

        self.gridLayout.addWidget(self.pushButton_Min, 2, 3, 1, 1)

        self.pushButton_Plu = QPushButton(Dialog)
        self.pushButton_Plu.setObjectName(u"pushButton_Plu")
        sizePolicy.setHeightForWidth(self.pushButton_Plu.sizePolicy().hasHeightForWidth())
        self.pushButton_Plu.setSizePolicy(sizePolicy)

        self.gridLayout.addWidget(self.pushButton_Plu, 3, 3, 1, 1)

        self.pushButton_Eql = QPushButton(Dialog)
        self.pushButton_Eql.setObjectName(u"pushButton_Eql")
        sizePolicy.setHeightForWidth(self.pushButton_Eql.sizePolicy().hasHeightForWidth())
        self.pushButton_Eql.setSizePolicy(sizePolicy)

        self.gridLayout.addWidget(self.pushButton_Eql, 4, 3, 1, 1)


        self.verticalLayout_2.addLayout(self.gridLayout)


        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Calculator", None))
        self.pushButton_6.setText(QCoreApplication.translate("Dialog", u"6", None))
        self.pushButton_8.setText(QCoreApplication.translate("Dialog", u"8", None))
        self.pushButton_7.setText(QCoreApplication.translate("Dialog", u"7", None))
        self.pushButton_Dot.setText(QCoreApplication.translate("Dialog", u".", None))
        self.pushButton_9.setText(QCoreApplication.translate("Dialog", u"9", None))
        self.pushButton_1.setText(QCoreApplication.translate("Dialog", u"1", None))
        self.pushButton_Alt.setText(QCoreApplication.translate("Dialog", u"Alt", None))
        self.pushButton_0.setText(QCoreApplication.translate("Dialog", u"0", None))
        self.pushButton_5.setText(QCoreApplication.translate("Dialog", u"5", None))
        self.pushButton_Clr.setText(QCoreApplication.translate("Dialog", u"C", None))
        self.pushButton_Del.setText(QCoreApplication.translate("Dialog", u"Del", None))
        self.pushButton_4.setText(QCoreApplication.translate("Dialog", u"4", None))
        self.pushButton_3.setText(QCoreApplication.translate("Dialog", u"3", None))
        self.pushButton_2.setText(QCoreApplication.translate("Dialog", u"2", None))
        self.pushButton_Per.setText(QCoreApplication.translate("Dialog", u"%", None))
        self.pushButton_Div.setText(QCoreApplication.translate("Dialog", u"/", None))
        self.pushButton_Tim.setText(QCoreApplication.translate("Dialog", u"*", None))
        self.pushButton_Min.setText(QCoreApplication.translate("Dialog", u"-", None))
        self.pushButton_Plu.setText(QCoreApplication.translate("Dialog", u"+", None))
        self.pushButton_Eql.setText(QCoreApplication.translate("Dialog", u"=", None))
    # retranslateUi

