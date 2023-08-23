# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'pa.ui'
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
from PySide6.QtWidgets import (QApplication, QGridLayout, QPushButton, QSizePolicy,
    QTextEdit, QVBoxLayout, QWidget)

class Ui_Form_pa(object):
    def setupUi(self, Form_pa):
        if not Form_pa.objectName():
            Form_pa.setObjectName(u"Form_pa")
        Form_pa.resize(400, 300)
        self.verticalLayout = QVBoxLayout(Form_pa)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.textEdit_pa = QTextEdit(Form_pa)
        self.textEdit_pa.setObjectName(u"textEdit_pa")

        self.verticalLayout.addWidget(self.textEdit_pa)

        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.pushButton_open = QPushButton(Form_pa)
        self.pushButton_open.setObjectName(u"pushButton_open")

        self.gridLayout.addWidget(self.pushButton_open, 0, 0, 1, 1)

        self.pushButton_hide = QPushButton(Form_pa)
        self.pushButton_hide.setObjectName(u"pushButton_hide")

        self.gridLayout.addWidget(self.pushButton_hide, 0, 1, 1, 1)

        self.pushButton_close = QPushButton(Form_pa)
        self.pushButton_close.setObjectName(u"pushButton_close")

        self.gridLayout.addWidget(self.pushButton_close, 1, 0, 1, 1)

        self.pushButton_pa = QPushButton(Form_pa)
        self.pushButton_pa.setObjectName(u"pushButton_pa")

        self.gridLayout.addWidget(self.pushButton_pa, 1, 1, 1, 1)


        self.verticalLayout.addLayout(self.gridLayout)


        self.retranslateUi(Form_pa)

        QMetaObject.connectSlotsByName(Form_pa)
    # setupUi

    def retranslateUi(self, Form_pa):
        Form_pa.setWindowTitle(QCoreApplication.translate("Form_pa", u"father", None))
        self.pushButton_open.setText(QCoreApplication.translate("Form_pa", u"open", None))
        self.pushButton_hide.setText(QCoreApplication.translate("Form_pa", u"hide", None))
        self.pushButton_close.setText(QCoreApplication.translate("Form_pa", u"close", None))
        self.pushButton_pa.setText(QCoreApplication.translate("Form_pa", u"send", None))
    # retranslateUi

