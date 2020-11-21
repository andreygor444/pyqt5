from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QCheckBox, QPlainTextEdit, QPushButton
from PyQt5 import uic
import sys


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi('interface.ui', self)
        self.can_draw = False
        self.initUI()

    def initUI(self):
        self.button.clicked.connect(self.draw)

    def draw(self):
        self.can_draw = True
        pass

    def paintEvent(self, e):
        pass


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main_window = MainWindow()
    main_window.show()
    sys.exit(app.exec())