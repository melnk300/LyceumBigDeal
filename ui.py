import os
import sys

import requests
import api
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QApplication, QWidget, QLabel
from PyQt5 import QtCore

SCREEN_SIZE = [600, 450]
class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.getImage()
        self.initUI()
        self.spn = 0.05

    def initUI(self):
        self.setGeometry(100, 100, *SCREEN_SIZE)
        self.setWindowTitle('Отображение карты')
        self.spn = 0.05
        self.pixmap = QPixmap(self.map_file)
        self.image = QLabel(self)
        self.image.move(0, 0)
        self.image.resize(600, 450)
        self.image.setPixmap(self.pixmap)

    def getImage(self):
        res = api.get_img('76.564993,60.938296', spn=','.join(list(map(str, [self.spn, self.spn]))))
        print(res.url)
        self.map_file = "map.png"
        self.repaint()

    def closeEvent(self, event):
        """При закрытии формы подчищаем за собой"""
        os.remove(self.map_file)

    def pqup(self):
        spn += 0.01
        print(spn)
        self.getImage()

    def pqdown(self):
        spn -= 0.01
        print(spn)
        self.getImage()

    def keyPressEvent(self, e):
        if e.key() == QtCore.Qt.Key_Up:
            self.pqup()
        elif e.key() == QtCore.Qt.Key_Down:
            self.pqdown()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec())
