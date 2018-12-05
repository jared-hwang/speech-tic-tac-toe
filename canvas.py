import sys
from PyQt5.Qt import QColor
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtGui import QPainter, QBrush, QPen
from PyQt5.QtCore import Qt

class Canvas(QWidget):

    def __init__(self, parent):        
        super(Canvas, self).__init__(parent)

        self._board = [-1,-1,-1,
                       -1,-1,-1,
                       -1,-1,-1]

        self._iconWidth = 120
        self._playerIcon = 0
        self._AIIcon = 1
        self._game = parent

        self._game_started = False

        self._goLight = False

    def paintEvent(self, event):
        painter = QPainter(self)
        
        # self.draw_board(painter)

        if (not self._goLight):
            painter.setBrush(Qt.red)
        else:
            painter.setBrush(Qt.green)

        painter.drawEllipse(520, 50, 40, 40)

        painter.setPen(QPen(Qt.black, 12, Qt.SolidLine));

        painter.drawLine(166, 20, 166, 480)
        painter.drawLine(333, 20, 333, 480)

        painter.drawLine(20, 166, 480, 166)
        painter.drawLine(20, 333, 480, 333)


        painter.setPen(QPen(Qt.black, 4, Qt.SolidLine));
        painter.setBrush(QColor(255, 0, 0))
        painter.drawRect(30, 30, 120, 120)

        painter.setBrush(QColor(255, 255, 0))
        painter.drawRect(190, 30, 120, 120)

        painter.setBrush(QColor(0, 0, 255))
        painter.drawRect(350, 30, 120, 120)

        painter.setBrush(QColor(148, 0, 211))
        painter.drawRect(30, 190, 120, 120)

        painter.setBrush(QColor(255, 255, 255))
        painter.drawRect(190, 190, 120, 120)

        painter.setBrush(QColor(255, 105, 180))
        painter.drawRect(350, 190, 120, 120)

        painter.setBrush(QColor(64, 224, 208))
        painter.drawRect(30, 350, 120, 120)

        painter.setBrush(QColor(0, 255, 0))
        painter.drawRect(190, 350, 120, 120)

        painter.setBrush(QColor(255, 165, 0))
        painter.drawRect(350, 350, 120, 120)

        painter.setPen(QPen(Qt.black, 12, Qt.SolidLine));
        
        for i in range(0, 9):
            if (self._board[i] == 1):
                self.draw_icon(painter, i, self._playerIcon)
            elif(self._board[i] == 0):
                self.draw_icon(painter, i, self._AIIcon)
            else:
                self.draw_icon(painter, i, self._board[i])



        # painter.setRenderHint(QPainter.Antialiasing, True);

        # painter.setPen(QPen(Qt.black, 12, Qt.SolidLine));
        # painter.setBrush(QBrush(Qt.green, Qt.SolidPattern));
        # painter.drawEllipse(100, 100, 400, 200);

    # def draw_board(self, painter):

    def draw_icon(self, painter, position, icon):

        xpos = 0
        ypos = 0

        if (position == 0) or (position == 3) or (position == 6):
            xpos = 30
        elif (position == 1) or (position == 4) or (position == 7):
            xpos = 30 + 40 + 120
        elif (position == 2) or (position == 5) or (position == 8):    
            xpos = 30 + 40 + 120 + 40 + 120

        if (position == 0) or (position == 1) or (position == 2):
            ypos = 30
        elif (position == 3) or (position == 4) or (position == 5):
            ypos = 30 + 40 + 120
        elif (position == 6) or (position == 7) or (position == 8):    
            ypos = 30 + 40 + 120 + 40 + 120

        if (icon == 1):
            painter.drawLine(xpos, ypos, xpos + self._iconWidth, ypos + self._iconWidth)
            painter.drawLine(xpos + self._iconWidth, ypos, xpos, ypos + self._iconWidth)
        elif (icon == 0):
            painter.drawArc(xpos, ypos, self._iconWidth, self._iconWidth, 0, 5760)

    def setBoard(self, board):
        self._board = board

    def swapGoLight(self):
        self._goLight = not (self._goLight)
        self.repaint()
