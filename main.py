import sys
import time
from gameInput import gameInput
from canvas import Canvas
from PyQt5.Qt import QColor
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtGui import QPainter, QBrush, QPen
from PyQt5.QtCore import Qt


# app = QApplication(sys.argv)
# canvas = Canvas()
# canvas.show()

game = gameInput()

game.promptUser()
test = game.acceptInput()

# sys.exit(app.exec_())


