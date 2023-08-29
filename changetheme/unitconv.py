from PySide6.QtWidgets import QApplication, QWidget
from unitconv_ui import Ui_Form
from qtmodern import styles, windows

class MyWindow(QWidget, Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.comboBox_type.addItems(["length","weight","area","volume"])
        self.items = [["m","cm","mm","km","mile","ft","yd","in","n mile"],
                      ["kg","g","t","lb","oz"],
                      ["m2","cm2","ha","ac","mile2","ft2","yd2","mile2"]]
        self.times = [[1, 0.01, 0.001, 1000, 1609, 0.3048, 0.9144, 0.0254, 1852],
                      [1, 0.001, 1000, 0.453, 0.02834],
                      [1, 0.0001, 10000, 4046.86, 2589988.11, 0.0929, 0.836, 2589988.11]]
        self.num_up = ''
        self.num_down = ''
        self.udStatus = 0
        self.bind()
        self.buttonStatus(False)
    
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
        self.pushButton_dot.clicked.connect(lambda: self.addNum('.'))

        self.pushButton_del.clicked.connect(self.delNum)
        self.pushButton_clr.clicked.connect(self.clear)

        self.comboBox_type.currentIndexChanged.connect(self.decideType)
        self.comboBox_up.currentIndexChanged.connect(self.changeUnit)
        self.comboBox_down.currentIndexChanged.connect(self.changeUnit)

        self.radioButton_up.pressed.connect(lambda: self.changeUd(0))
        self.radioButton_down.pressed.connect(lambda: self.changeUd(1))
    
    def addNum(self, num):
        if self.udStatus == 0 and len(self.num_up) < 9:
            self.num_up += num
            self.up2down()
        elif self.udStatus == 1 and len(self.num_down) < 9:
            self.num_down += num
            self.down2up()
    
    def up2down(self):
        self.num_down = str(self.conv(eval(self.num_up)))
        self.lcdNumber_up.display(eval(self.num_up))
        self.num_down = self.num_down[:min(10, len(self.num_down))]
        self.lcdNumber_down.display(eval(self.num_down))
    
    def down2up(self):
        self.num_up = str(self.conv(eval(self.num_down)))
        self.lcdNumber_down.display(eval(self.num_down))
        self.num_up = self.num_up[:min(10, len(self.num_up))]
        self.lcdNumber_up.display(eval(self.num_up))
    
    def conv(self, input) -> float:
        if self.udStatus == 0:
            return min(input * self.times[self.comboBox_type.currentIndex()][self.comboBox_up.currentIndex()] / self.times[self.comboBox_type.currentIndex()][self.comboBox_down.currentIndex()], 999999999)
        else:
            return min(input * self.times[self.comboBox_type.currentIndex()][self.comboBox_down.currentIndex()] / self.times[self.comboBox_type.currentIndex()][self.comboBox_up.currentIndex()], 999999999)

    def delNum(self):
        if self.udStatus == 0:
            if len(self.num_up) == 1:
                self.clear()
            else:
                self.num_up = self.num_up[:-1]
                self.up2down()
        else:
            if len(self.num_down) == 1:
                self.clear()
            else:
                self.num_down = self.num_down[:-1]
                self.down2up()
    
    def clear(self):
        self.num_up = '0'
        self.up2down()
        self.num_up = ''
        self.num_down = ''
    
    def decideType(self):
        self.comboBox_up.clear()
        self.comboBox_down.clear()
        self.comboBox_up.addItems(self.items[self.comboBox_type.currentIndex()])
        self.comboBox_down.addItems(self.items[self.comboBox_type.currentIndex()])
        self.buttonStatus(True)
        self.clear()

    def changeUd(self, flag):
        self.udStatus = flag
    
    def buttonStatus(self, flag):
        self.pushButton_0.setEnabled(flag)
        self.pushButton_1.setEnabled(flag)
        self.pushButton_2.setEnabled(flag)
        self.pushButton_3.setEnabled(flag)
        self.pushButton_4.setEnabled(flag)
        self.pushButton_5.setEnabled(flag)
        self.pushButton_6.setEnabled(flag)
        self.pushButton_7.setEnabled(flag)
        self.pushButton_8.setEnabled(flag)
        self.pushButton_9.setEnabled(flag)
        self.pushButton_dot.setEnabled(flag)
        self.pushButton_del.setEnabled(flag)
        self.pushButton_clr.setEnabled(flag)
    
    def changeUnit(self):
        if self.num_up != '':
            if self.udStatus == 0:
                self.up2down()
            else:
                self.down2up()

if __name__ == '__main__':
    app = QApplication([])
    window = MyWindow()
    styles.light(app)
    mw = windows.ModernWindow(window)
    mw.show()
    app.exec()