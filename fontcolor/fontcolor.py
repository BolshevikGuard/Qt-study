from PySide6.QtWidgets import QApplication, QWidget, QColorDialog, QFontDialog
from fontcolor_ui import Ui_Form

class MyWindow(QWidget, Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        
        self.bind()
    
    def bind(self):
        self.pushButton_font.clicked.connect(self.changeFont)
        self.pushButton_color.clicked.connect(self.changeColor)
    
    def changeFont(self):
        ok, font = QFontDialog.getFont()
        if not ok: return
        self.textEdit.setFont(font)
    
    def changeColor(self):
        color = QColorDialog.getColor()
        self.textEdit.setTextColor(color)

if __name__ == '__main__':
    app = QApplication([])
    window = MyWindow()
    window.show()
    app.exec()