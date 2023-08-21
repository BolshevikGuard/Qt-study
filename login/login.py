from PySide6.QtWidgets import QApplication, QDialog
from login_ui import Ui_Dialog

class MyWindow(QDialog, Ui_Dialog):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.pushButton.clicked.connect(self.loginFun)

    def loginFun(self):
        account = self.lineEdit.text()
        password = self.lineEdit_2.text()

        if account == '123' and password == '456':
            print('Login Succeeded!')
        else:
            print('Login Failed!')


if __name__ == '__main__':
    app = QApplication([])
    window = MyWindow()
    window.show()
    app.exec()