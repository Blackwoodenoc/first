import sys
from random import randint
from PyQt6.QtCore import Qt, QRectF, QPointF
from PyQt6.QtGui import QPainter, QColor, QPolygonF
from PyQt6.QtWidgets import QWidget, QApplication, QPushButton
class Suprematism(QWidget):
    def __init__(self):
        super().__init__()
        self.setMouseTracking(True)
        self.coords_ = [350, 450]
        self.qp = QPainter()
        self.flag = False
        self.status = 1
        self.initUI()

    def initUI(self):
        self.btn = QPushButton('Нажми на меня', self)
        self.btn.clicked.connect(self.ion)
        self.btn.resize(100, 60)
        self.setGeometry(300, 300, 1000, 1000)
        self.setWindowTitle('Рисование')

    def drawf(self):
        self.flag = True
        self.update()

    def paintEvent(self, event):
        if self.flag:
            self.qp = QPainter()
            self.qp.begin(self)
            self.draw(self.status)
            self.qp.end()

    def draw(self, status):
        R = randint(40, 200)
        self.qp.setBrush(QColor(*[randint(0, 255) for _ in range(3)]))
        self.qp.drawEllipse(QPointF(self.coords_[0],
                                    self.coords_[1]), R, R)
    

    def ion(self, event):
        self.status = 1
        self.drawf()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Suprematism()
    ex.show()
    sys.exit(app.exec())  