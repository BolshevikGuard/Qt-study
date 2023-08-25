from PySide6.QtWidgets import QApplication, QWidget
from loadingWin_ui import Ui_LoadingWin
from mainWin_ui import Ui_MainWin
from PySide6.QtCore import Qt, QTimer

class LoadingWindow(QWidget, Ui_LoadingWin):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.timer = QTimer(self)
        self.timer.start(30)
        self.timeCount = 0
        self.timer.timeout.connect(self.updateProgress)

    def updateProgress(self):
        self.timeCount += 1
        self.progressBar.setValue(self.timeCount)

        if self.progressBar.value() >= 100:
            self.timer.stop()
            self.openMainWindow()
    
    def openMainWindow(self):
        self.close()
        self.mainWindow = MainWindow()
        self.mainWindow.move(20, 20)
        self.mainWindow.show()

class MainWindow(QWidget, Ui_MainWin):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

if __name__ == '__main__':
    app = QApplication([])
    window = LoadingWindow()
    window.show()
    app.exec()