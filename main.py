import sys
from gameInput import gameInput
from canvas import Canvas
from PyQt5.Qt import QColor
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtGui import QPainter, QBrush, QPen
from PyQt5.QtCore import Qt

# game = gameInput()

# game.promptUser()
# test = game.acceptInput()


app = QApplication(sys.argv)
canvas = Canvas()
canvas.show()
sys.exit(app.exec_())