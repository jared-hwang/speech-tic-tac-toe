import sys
import time
from PyQt5.Qt import QColor
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtGui import QPainter, QBrush, QPen
from PyQt5.QtCore import Qt
from game import Game

def main():
    app = QtWidgets.QApplication([])
 
    game = Game()
     
    game.show()
     
    sys.exit(app.exec())


if __name__ == '__main__':
    main()


