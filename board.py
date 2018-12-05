import sys
from random import *

class Board:
    # Constants
    UNPLAYED_SPACE = -1;
    AI_MOVE        =  0;
    PLAYER_MOVE    =  1;

    INVALID_INDEX = -1;
    AI_WINS       =  0;
    PLAYER_WINS   =  1;
    TIE           =  2;
    CONTINUE_GAME =  3;

    # Attributes
    _board[9];
    _availableMoves[9];

    def __init__(self):
        for space in self._board:
            space = -1;

        for i in range(9):
            self._availableMoves[i] = i;

    def doTurn(self, row, column):
        index = 3 * row + column;

        # check to see if the input is legal
        if (self._board[index] != self.UNPLAYED_SPACE):
            return self.INVALID_INDEX;

        self.playerMove(index);
        winState = checkWinState(PLAYER_MOVE);
        if (winState != self.CONTINUE_GAME):
            return winState;

        self.counterMove();
        winState = checkWinState(AI_MOVE);
        return winState;

    def playerMove(self, index):
        self._board[index] = self.PLAYER_MOVE;
        self._availableMoves.remove(index);

    def aiMove(self, index):
        self._board[index] = AI_MOVE;
        self._availableMoves.remove(index);

    def checkWinState(self, symbol):
        if (self.checkColumnForWin(symbol) ||
            self.checkRowForWin(symbol)    ||
            self.checkDiagonalForWin(symbol)):
            return symbol;
        elif (len(self._availableMoves) == 0):
            return self.TIE;
        else:
            return self.CONTINUE_GAME;

    def checkColumnForWin(self, symbol):
        board = self._board;
        if ((board[0] == symbol && board[3] == symbol && board[6] == symbol) ||
            (board[1] == symbol && board[4] == symbol && board[7] == symbol) ||
            (board[2] == symbol && board[5] == symbol && board[8] == symbol)):
            return True;
        else:
            return False;

    def checkRowForWin(self, symbol):
        board = self._board;
        if ((board[0] == symbol && board[1] == symbol && board[2] == symbol) ||
            (board[3] == symbol && board[4] == symbol && board[5] == symbol) ||
            (board[6] == symbol && board[7] == symbol && board[8] == symbol)):
            return True;
        else:
            return False;

    def checkDiagonalForWin(self, symbol):
        board = self._board;
        if ((board[0] == symbol && board[4] == symbol && board[8] == symbol) ||
            (board[2] == symbol && board[4] == symbol && board[6] == symbol)):
            return True;
        else:
            return False;

    def counterMove(self):
        if (!self.checkForPossibleWin()):
            self.makeRegularMove();

    def checkForPossibleWin(self):
        for space in self._availableMoves:
            if (self.checkColumnForPossibleWin(space) ||
                self.checkRowForPossibleWin(space)):
                self.aiMove(space);
                return True;
            elif (space % 4 == 0):
                if (self.checkLeftDiagonalForPossibleWin(space)):
                    self.aiMove(space);
                    return True;
            elif (space % 4 == 2):
                if (self.checkRightDiagonalForPossibleWin(space)):
                    self.aiMove(space);
                    return True;

        return False;

    def checkColumnForPossibleWin(self, space):
        otherTwoSpaces[2];
        i = 0;

        if (space - 6 > -1):
            otherTwoSpaces[i] = self._board[space - 6];
            i++;
        if (space - 3 > -1):
            otherTwoSpaces[i] = self._board[space - 3];
            i++;
        if (space + 3 < 9):
            otherTwoSpaces[i] = self._board[space + 3];
            i++;
        if (space + 6 < 9):
            otherTwoSpaces[i] = self._board[space + 6];

        if (otherTwoSpaces[0] == otherTwoSpaces[1]):
            return True;
        else:
            return False;

    def checkRowForPossibleWin(self, space):
        otherTwoSpaces[2];
        i = 0;

        lowerLimit = 0;
        upperLimit = 0;
        spaceQuotient = space / 3;

        if (spaceQuotient == 0):
            lowerLimit = -1;
            upperLimit = 3;
        elif (spaceQuotient == 1):
            lowerLimit = 2;
            upperLimit = 6;
        else:
            lowerLimit = 5;
            upperLimit = 9;

        if (space - 2 > lowerLimit):
            otherTwoSpaces[i] = self._board[space - 2];
            i++;
        if (space - 1 > lowerLimit):
            otherTwoSpaces[i] = self._board[space - 1];
            i++;
        if (space + 1 < upperLimit):
            otherTwoSpaces[i] = self._board[space + 1];
            i++;
        if (space + 2 < upperLimit):
            otherTwoSpaces[i] = self._board[space + 2];

        if (otherTwoSpaces[0] == otherTwoSpaces[1]):
            return True;
        else:
            return False;

    def checkLeftDiagonalForPossibleWin(self, space):
        otherTwoSpaces[2];
        i = 0;

        if (space - 8 > -1):
            otherTwoSpaces[i] = self._board[space - 8];
            i++;
        if (space - 4 > -1):
            otherTwoSpaces[i] = self._board[space - 4];
            i++;
        if (space + 4 < 9):
            otherTwoSpaces[i] = self._board[space + 4];
            i++;
        if (space + 8 < 9):
            otherTwoSpaces[i] = self._board[space + 8];

        if (otherTwoSpaces[0] == otherTwoSpaces[1]):
            return True;
        else:
            return False;

    def checkRightDiagonalForPossibleWin(self, space):
        otherTwoSpaces[2];
        i = 0;

        if (space - 4 > -1):
            otherTwoSpaces[i] = self._board[space - 4];
            i++;
        if (space - 2 > -1):
            otherTwoSpaces[i] = self._board[space - 2];
            i++;
        if (space + 2 < 9):
            otherTwoSpaces[i] = self._board[space + 2];
            i++;
        if (space + 4 < 9):
            otherTwoSpaces[i] = self._board[space + 4];

        if (otherTwoSpaces[0] == otherTwoSpaces[1]):
            return True;
        else:
            return False;

    def makeRegularMove(self):
        playSpace = random.choice(self._availableMoves);
        self.aiMove(playSpace);

    def getBoard(self):
        return self._board;
