from gameInput import gameInput
from canvas import Canvas
from board import Board
import sys
import time
from PyQt5.Qt import QColor
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtGui import QPainter, QBrush, QPen
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QMainWindow, QApplication, QPushButton, QWidget, QAction, QTabWidget,QVBoxLayout
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtGui import QFont
import simpleaudio as sa

class Game(QtWidgets.QMainWindow):

    def __init__(self):
        super().__init__()

        self.left = 20
        self.top = 20
        self.width = 600
        self.height = 500

        self._microphone = gameInput()

        self.setWindowTitle("Speech run Tic Tac Toe!")
        self.setGeometry(self.left, self.top, self.width, self.height)

        self._canvas = Canvas(self)
        self.setCentralWidget(self._canvas) 

        self._gameBoard = Board()

        self._resultsScreen = QtWidgets.QWidget()
        self._resultLabel = QtWidgets.QLabel("It's a tie!", self._resultsScreen)
        self._resultLabel.setGeometry(100, 40, 330, 300)
        self._resultLabel.setFont(QFont('Comic Sans MS', 70))

        palette = self._resultsScreen.palette()
        palette.setColor(self._resultsScreen.backgroundRole(), QColor(0, 0, 0))

        self._gameActive = True

        self._colorKeys = {"red": 0, "yellow": 1, "blue": 2,
                           "purple": 3, "white":4 , "pink": 5,
                           "turquoise": 6, "green": 7, "orange": 8}

    def keyPressEvent(self, e):
        if e.key() == Qt.Key_Return:
            if (self._gameActive):
                self.acceptInput()
            else:
                self.resetGame()

        if e.key() == Qt.Key_Space:
                self.resetGame()

        
    def resetGame(self):
        #board clear
        self._gameBoard.clearBoard()

        board = self._gameBoard.getBoard()
        self._canvas.setBoard(board)
        self._canvas.repaint()

        self._resultsScreen.close()
        self._gameActive = True

        # self._canvas.close()
        # self._canvas = Canvas(self)
        # self.setCentralWidget(self._canvas)

        # board = self._gameBoard.getBoard()
        # self._canvas.setBoard(board)
        # self._canvas.repaint()


    def setPlayerIcon(self, icon):
        self._canvas._playerIcon = icon
        if (icon == 1):
            self._canvas._AIIcon = 0
        else:
            self._canvas._AIIcon = 1

    def tie(self):

        self._resultLabel.setGeometry(20, 40, 500, 400)
        self._resultLabel.setFont(QFont('Comic Sans MS', 40))
        self._resultLabel.setText("It's a tie!!\nGo back to main window and enter to play again")
        self._resultLabel.setWordWrap(True)
        self._resultLabel.setAlignment(Qt.AlignCenter)
        
        palette = self._resultsScreen.palette()
        palette.setColor(self._resultsScreen.backgroundRole(), QColor(87, 92, 255))

        self._resultLabel.setStyleSheet('color: #00FF00')
        self._resultsScreen.setPalette(palette)
        self._resultsScreen.show()

        self._gameActive = False


    def win(self):

        self._resultLabel.setGeometry(20, 40, 500, 400)
        self._resultLabel.setFont(QFont('Comic Sans MS', 40))
        self._resultLabel.setText("You win!!!\nGo back to main window and enter to play again")
        self._resultLabel.setWordWrap(True)
        self._resultLabel.setAlignment(Qt.AlignCenter)

        palette = self._resultsScreen.palette()
        palette.setColor(self._resultsScreen.backgroundRole(), QColor(87, 255, 98))

        self._resultLabel.setStyleSheet('color: blue')
        self._resultsScreen.setPalette(palette)
        self._resultsScreen.show()


        self._gameActive = False

    def lose(self):
        self._resultLabel.setGeometry(20, 40, 500, 400)
        self._resultLabel.setFont(QFont('Comic Sans MS', 40))

        self._resultLabel.setText("I don't know how... but you lose!\nGo back to main window and enter to play again")
        self._resultLabel.setWordWrap(True)
        self._resultLabel.setAlignment(Qt.AlignCenter)

        palette = self._resultsScreen.palette()
        palette.setColor(self._resultsScreen.backgroundRole(), QColor(0, 0, 0))

        self._resultLabel.setStyleSheet('color: #FF0000')
        self._resultsScreen.setPalette(palette)
        self._resultsScreen.show()

        self._gameActive = False


    def acceptInput(self):

        if (self._canvas._goLight == False):
            self._canvas.swapGoLight()

        userInput = self._microphone.acceptInput(self._canvas)
        
        if not userInput:
            self._canvas.swapGoLight()
            return

        turnResult = self._gameBoard.doPlayerTurn(self._colorKeys[userInput])

        if (turnResult == -1):
            print("You can't go there, it's already taken!")
            self._canvas.swapGoLight()
            return

        board = self._gameBoard.getBoard()
        self._canvas.setBoard(board)
        self._canvas.repaint()

        if (turnResult == 0):
            self.lose()
            return
        elif (turnResult == 1):
            self.win()
            return
        elif (turnResult == 2):
            self.tie()
            return

        turnResult = self._gameBoard.doAITurn()

        board = self._gameBoard.getBoard()
        self._canvas.setBoard(board)
        self._canvas.repaint()

        if (turnResult == 0):
            self.lose()
            return
        elif (turnResult == 1):
            self.win()
            return
        elif (turnResult == 2):
            self.tie()
            return

        # board = [-1,-1,-1,-1,-1,-1,-1,-1,-1]
        # board[self._colorKeys[userInput]] = 1
        # self._canvas.setBoard(board)

        # self._canvas.repaint()



        # self._canvas.swapGoLight()
        # self._canvas.repaint()

        
        # result = board(userInput)

        # if (result):
        #     self.win()
        #     exit(1)

        # elif (result == False):
        #     self.lose()
        #     exit(1)

        # elif ('''tie condition'''): 
        #     self.tie()
        #     exit(1)

        # else:








