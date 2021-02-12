import os
import sys
import api
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5 import QtCore, uic

SCREEN_SIZE = [600, 450]


class Example(QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi('ui.ui', self)
        self.setWindowTitle('Отображение карты')

        self.z = 14
        self.coords = '76.564993,60.938296'
        self.map_file = "map.png"
        self.getImage()

    def getImage(self):
        res = api.get_img(self.coords, str(self.z))
        self.pixmap = QPixmap(self.map_file)
        self.image.setPixmap(self.pixmap)
        # print(res.url)

    def closeEvent(self, event):
        """При закрытии формы подчищаем за собой"""
        os.remove(self.map_file)

    def keyPressEvent(self, e):
        if e.key() == QtCore.Qt.Key_PageUp:
            self.z += 1
            self.getImage()
        elif e.key() == QtCore.Qt.Key_PageDown:
            self.z -= 1
            self.getImage()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec())
