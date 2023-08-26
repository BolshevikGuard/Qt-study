from PySide6.QtWidgets import QApplication, QMainWindow, QFontDialog, QFileDialog
from menutoolbox_ui import Ui_MainWindow

class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.move(200, 200)

        self.bind()
    
    def bind(self):
        self.actionOpen.triggered.connect(self.openFile)
        self.actionClose.triggered.connect(self.closeFile)
        self.actionExit.triggered.connect(lambda: self.close())
        self.pushButton.clicked.connect(self.send2Three)
        self.pushButton_2.clicked.connect(self.changeFont)
    
    def openFile(self):
        path = QFileDialog.getOpenFileName(self, 'Choose Text', './', "TXT (*.txt)")[0]
        if path :
            with open(path, "r") as file:
                file_content = file.read()
                self.textEdit.setPlainText(file_content)
    
    def closeFile(self):
        self.textEdit.clear()
    
    def send2Three(self):
        self.label.setText(self.textEdit_2.toPlainText())
        font = self.label.font()
        font.setPointSize(24)
        self.label.setFont(font)

    def changeFont(self):
        ok, font = QFontDialog.getFont()
        if not ok: return
        self.label.setFont(font)


if __name__ == '__main__':
    app = QApplication([])
    window = MainWindow()
    window.show()
    app.exec()