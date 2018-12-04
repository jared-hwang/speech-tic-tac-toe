import sys
from PyQt5.Qt import QColor
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtGui import QPainter, QBrush, QPen
from PyQt5.QtCore import Qt

class Canvas(QWidget):

    def __init__(self):
        super().__init__()
        self.resize(1000, 400)

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing, True);
        painter.setPen(QPen(Qt.black, 12, Qt.SolidLine));
        painter.setBrush(QBrush(Qt.green, Qt.SolidPattern));
        painter.drawEllipse(100, 100, 400, 200);