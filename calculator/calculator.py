from PySide6.QtWidgets import QApplication, QDialog
from calculator_ui import Ui_Dialog

class MyWindow(QDialog, Ui_Dialog):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.expr = ''
        self.dispNum = ''
        self.isFinal = False
        self.symStatus(False)
        self.bind()

    def bind(self):
        self.pushButton_0.clicked.connect(lambda: self.addNum('0'))
        self.pushButton_1.clicked.connect(lambda: self.addNum('1'))
        self.pushButton_2.clicked.connect(lambda: self.addNum('2'))
        self.pushButton_3.clicked.connect(lambda: self.addNum('3'))
        self.pushButton_4.clicked.connect(lambda: self.addNum('4'))
        self.pushButton_5.clicked.connect(lambda: self.addNum('5'))
        self.pushButton_6.clicked.connect(lambda: self.addNum('6'))
        self.pushButton_7.clicked.connect(lambda: self.addNum('7'))
        self.pushButton_8.clicked.connect(lambda: self.addNum('8'))
        self.pushButton_9.clicked.connect(lambda: self.addNum('9'))
        self.pushButton_Dot.clicked.connect(lambda: self.addNum('.'))

        self.pushButton_Plu.clicked.connect(lambda: self.addSym('+'))
        self.pushButton_Min.clicked.connect(lambda: self.addSym('-'))
        self.pushButton_Tim.clicked.connect(lambda: self.addSym('*'))
        self.pushButton_Div.clicked.connect(lambda: self.addSym('/'))

        self.pushButton_Del.clicked.connect(self.delNum)
        self.pushButton_Clr.clicked.connect(self.clear)
        self.pushButton_Eql.clicked.connect(self.equal)

    def addNum(self, number):
        self.dispNum += number
        if self.isFinal == True:
            self.expr = number
            self.isFinal = False
        else:
            self.expr += number

        self.lcdNumber.display(eval(self.dispNum))
        self.symStatus(True)
        self.pushButton_Del.setEnabled(True)
        self.isFinal = False        
    
    def addSym(self, symbol):
        if self.isFinal == False:
            self.lcdNumber.display(eval(self.expr))
            self.dispNum = ''
            self.expr += symbol
            self.symStatus(False)
        else:
            self.expr += symbol
            self.symStatus(False)
            self.isFinal = False
        self.pushButton_Del.setEnabled(False)
    
    def delNum(self):
        self.dispNum = self.dispNum[:-1]
        self.expr = self.expr[:-1]
        
        if self.expr == '' or self.expr[-1] =='-' or self.expr[-1] =='*' or self.expr[-1] =='/' or self.expr[-1] == '+':
            self.symStatus(False)
            self.lcdNumber.display(0)
            self.pushButton_Del.setEnabled(False)
        else:
            self.symStatus(True)
            self.lcdNumber.display(eval(self.dispNum))

    def symStatus(self, isenabled):
        self.pushButton_Div.setEnabled(isenabled)
        self.pushButton_Min.setEnabled(isenabled)
        self.pushButton_Plu.setEnabled(isenabled)
        self.pushButton_Tim.setEnabled(isenabled)
        self.pushButton_Eql.setEnabled(isenabled)
        self.pushButton_Dot.setEnabled(isenabled)

    def equal(self):
        self.lcdNumber.display(eval(self.expr))
        self.expr = str(self.lcdNumber.value())
        self.dispNum = ''
        self.isFinal = True
        self.pushButton_Del.setEnabled(False)
    
    def clear(self):
        self.lcdNumber.display(0)
        self.symStatus(False)
        self.expr = ''
        self.dispNum = ''


if __name__ == '__main__':
    app = QApplication([])
    window = MyWindow()
    window.show()
    app.exec()