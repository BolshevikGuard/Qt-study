# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'loadingWin.ui'
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
from PySide6.QtWidgets import (QApplication, QLabel, QProgressBar, QSizePolicy,
    QVBoxLayout, QWidget)

class Ui_LoadingWin(object):
    def setupUi(self, LoadingWin):
        if not LoadingWin.objectName():
            LoadingWin.setObjectName(u"LoadingWin")
        LoadingWin.resize(400, 300)
        self.verticalLayout = QVBoxLayout(LoadingWin)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label = QLabel(LoadingWin)
        self.label.setObjectName(u"label")
        self.label.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.label)

        self.progressBar = QProgressBar(LoadingWin)
        self.progressBar.setObjectName(u"progressBar")
        self.progressBar.setValue(0)
        self.progressBar.setTextDirection(QProgressBar.TopToBottom)

        self.verticalLayout.addWidget(self.progressBar)


        self.retranslateUi(LoadingWin)

        QMetaObject.connectSlotsByName(LoadingWin)
    # setupUi

    def retranslateUi(self, LoadingWin):
        LoadingWin.setWindowTitle(QCoreApplication.translate("LoadingWin", u"Loading Window", None))
        self.label.setText(QCoreApplication.translate("LoadingWin", u"Loading...", None))
    # retranslateUi

