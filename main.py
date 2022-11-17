from random import randrange
import sys

from PyQt5.QtCore import QPoint
from PyQt5.QtGui import QPainter, QColor
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QWidget


class MyWidget(QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi('main.ui', self)
        self.button.clicked.connect(self.draw)
        self.paint = False

    def paintEvent(self, e):
        if self.paint:
            qp = QPainter()
            qp.begin(self)
            self.draw(qp)
            qp.end()
            self.paint = -self.paint
    def draw(self, qp):
        self.paint = True
        qp.setBrush(QColor(255, 255, 0))
        point = QPoint(randrange(0, self.width()), randrange(0, self.height()))
        r = randrange(10, self.height() // 2)
        qp.drawEllipse(point, r,  r)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec())