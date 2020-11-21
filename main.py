from PyQt5.QtWidgets import QMainWindow, QApplication
from PyQt5 import uic
from PyQt5.QtGui import QPainter, QColor
from random import  randint
import sys


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('UI.ui', self)
        self.circles = []
        self.can_draw = False
        self.initUI()

    def initUI(self):
        self.pushButton.clicked.connect(self.draw)

    def draw(self):
        self.can_draw = True
        self.repaint()
        self.can_draw = False

    def paintEvent(self, e):
        if self.can_draw:
            qp = QPainter()
            qp.begin(self)
            qp.setBrush(QColor(255, 255, 0))
            radius = randint(10, 500)
            self.circles.append((randint(0, 400), randint(0, 400), radius, radius))
            for circle in self.circles:
                qp.drawEllipse(*circle)
            qp.end()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main_window = MainWindow()
    main_window.show()
    sys.exit(app.exec())