from gameInput import gameInput
from canvas import Canvas
import sys
from PyQt5.Qt import QColor
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtGui import QPainter, QBrush, QPen
from PyQt5.QtCore import Qt

class Game(QtWidgets.QMainWindow):

    def __init__(self):
        super().__init__()
        self._canvas = Canvas()
        self._canvas.show()


