import sys
from random import randrange
from PyQt5.QtGui import QBrush, QColor, QPainter
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5 import uic

SCREEN_SIZE = [500, 500]


class Example(QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi('ui.ui', self)
        self.setGeometry(300, 300, *SCREEN_SIZE)
        self.do_paint = False
        self.button.clicked.connect(self.draw_on)

    def paintEvent(self, event):
        if self.do_paint:
            qp = QPainter()
            qp.begin(self)
            self.draw(qp)
            qp.end()

    def draw_on(self):
        self.do_paint = True
        self.repaint()

    def draw(self, qp):
        brush = QBrush(QColor('yellow'))
        r = randrange(1, SCREEN_SIZE[0] * 0.5)
        x, y = 250, 200
        qp.setBrush(brush)
        qp.drawEllipse(x - r // 2, y - r // 2, r, r)
        self.do_paint = False


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec())
