from PySide6.QtWidgets import QApplication, QWidget, QFileDialog
from imgblur_ui import Ui_Form
from PySide6.QtGui import QPixmap
from PIL import Image, ImageFilter, ImageQt

class MyWindow(QWidget, Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pushButton_open.setEnabled(False)
        self.pushButton_save.setEnabled(False)
        self.comboBox.addItems(["Guassian", "Median"])
        self.bind()

    def bind(self):
        self.comboBox.currentIndexChanged.connect(lambda: self.pushButton_open.setEnabled(True))
        self.pushButton_open.clicked.connect(self.getImg)
        self.pushButton_save.clicked.connect(self.saveImg)
        self.blurSlider.valueChanged.connect(self.blurChange)
    
    def getImg(self):
        self.img = Image.open(QFileDialog.getOpenFileName(self, 'Choose pic', './', 'pics(*.png *.jpg *.jpeg)')[0])
        pixmap = ImageQt.toqpixmap(self.img)
        self.picLabel.setPixmap(pixmap)
        self.picLabel.setFixedSize(pixmap.size())
        self.pushButton_save.setEnabled(False)
    
    def saveImg(self):
        path, _ = QFileDialog.getSaveFileName(self, 'Save pic', './', 'PNG (*.png);;JPEG (*.jpg);;')
        if path:
            if "JPEG" in path:
                self.blurPic.convert("RGB").save(path, "JPEG")
            else:
                self.blurPic.save(path)

    def blurChange(self, value):
        if self.comboBox.currentIndex == 0:
            self.blurPic = self.img.filter(ImageFilter.GaussianBlur(radius=value))
        else:
            self.blurPic = self.img.filter(ImageFilter.MedianFilter(size=value))
        self.picLabel.setPixmap(ImageQt.toqpixmap(self.blurPic))
        self.pushButton_save.setEnabled(True)
        print(value)


if __name__ == '__main__':
    app = QApplication([])
    window = MyWindow()
    window.show()
    app.exec()
