from PyQt5.QtWidgets import QMainWindow, QApplication
from PyQt5.QtGui import QPainter, QColor
from random import randint
from UI import Ui_MainWindow
import sys


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.circles = []
        self.can_draw = False
        self.setupUi(self)
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

            radius = randint(10, 500)
            self.circles.append(((randint(50, 255), randint(50, 255), randint(50, 255)),
                                 (randint(0, 400), randint(0, 400), radius, radius)))
            for color, circle in self.circles:
                qp.setBrush(QColor(*color))
                qp.drawEllipse(*circle)
            qp.end()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main_window = MainWindow()
    main_window.show()
    sys.exit(app.exec())