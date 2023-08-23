from PySide6.QtWidgets import QApplication, QWidget
from pa_ui import Ui_Form_pa
from son_ui import Ui_Form_son
from PySide6.QtCore import Signal

class PaWindow(QWidget, Ui_Form_pa):
    send2son = Signal(str)
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.sonWindow = SonWindow(self)
        self.bind()
    
    def bind(self):
        self.send2son.connect(self.sonWindow.textEdit_son.setText)
        self.pushButton_open.clicked.connect(lambda: self.sonWindow.show())
        self.pushButton_hide.clicked.connect(lambda: self.sonWindow.hide())
        self.pushButton_close.clicked.connect(lambda: self.sonWindow.close())
        self.pushButton_pa.clicked.connect(self.sendAction)
    
    def sendAction(self):
        self.send2son.emit(self.textEdit_pa.toPlainText())

class SonWindow(QWidget, Ui_Form_son):
    send2pa = Signal(str)
    def __init__(self, parent=None):
        super().__init__()
        self.setupUi(self)
        self.parent = parent
        self.bind()
    
    def bind(self):
        self.send2pa.connect(self.parent.textEdit_pa.setText)
        self.pushButton_son.clicked.connect(self.sendAction)
       
    
    def sendAction(self):
        self.send2pa.emit(self.textEdit_son.toPlainText())
    
if __name__ == '__main__':
    app = QApplication([])
    window = PaWindow()
    window.show()
    app.exec()