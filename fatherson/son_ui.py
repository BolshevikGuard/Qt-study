# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'son.ui'
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
from PySide6.QtWidgets import (QApplication, QPushButton, QSizePolicy, QTextEdit,
    QVBoxLayout, QWidget)

class Ui_Form_son(object):
    def setupUi(self, Form_son):
        if not Form_son.objectName():
            Form_son.setObjectName(u"Form_son")
        Form_son.resize(400, 300)
        self.verticalLayout = QVBoxLayout(Form_son)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.textEdit_son = QTextEdit(Form_son)
        self.textEdit_son.setObjectName(u"textEdit_son")

        self.verticalLayout.addWidget(self.textEdit_son)

        self.pushButton_son = QPushButton(Form_son)
        self.pushButton_son.setObjectName(u"pushButton_son")

        self.verticalLayout.addWidget(self.pushButton_son)


        self.retranslateUi(Form_son)

        QMetaObject.connectSlotsByName(Form_son)
    # setupUi

    def retranslateUi(self, Form_son):
        Form_son.setWindowTitle(QCoreApplication.translate("Form_son", u"son", None))
        self.pushButton_son.setText(QCoreApplication.translate("Form_son", u"send to pa", None))
    # retranslateUi

