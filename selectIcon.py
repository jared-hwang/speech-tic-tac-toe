from PyQt5.Qt import QColor
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtGui import QPainter, QBrush, QPen
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import pyqtSlot
import time

class iconSelect(QtWidgets.QMainWindow):
    
    def __init__(self, game):
        super().__init__()
        
        self.icon = 0

        self._game = game
        
        self._clicked = False

    def initUI(self):               
        self.setGeometry(300, 300, 300, 140)
        self.setWindowTitle('Pick an Icon!')

        button = QPushButton('X', self)
        button.move(70,50) 
        button.setFixedSize(60, 50)
        button.clicked.connect(self.picked_x)

        button2 = QPushButton("O", self)
        button2.move(170,50) 
        button2.setFixedSize(60, 50)
        button2.clicked.connect(self.picked_o)

        self.show()



    def picked_x(self):

        self.icon = 1
        self.close()
        self._game.setPlayerIcon(self.icon)
        self._game.show()


    def picked_o(self):
        self.icon = 0
        self.close()
        self._game.setPlayerIcon(self.icon)
        self._game.show()