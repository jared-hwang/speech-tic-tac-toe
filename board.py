import sys
import random

class Board(object):
    # Constants
    UNPLAYED_SPACE = -1;
    AI_MOVE        =  0;
    PLAYER_MOVE    =  1;

    INVALID_INDEX = -1;
    AI_WINS       =  0;
    PLAYER_WINS   =  1;
    TIE           =  2;
    CONTINUE_GAME =  3;

    def __init__(self):
        self._board = [];
        self._availableMoves = [];

        for i in range(9):
            self._board.append(-1);

        for i in range(9):
            self._availableMoves.append(i);

    def doPlayerTurn(self, index):
        # check to see if the input is legal
        if (self._board[index] != self.UNPLAYED_SPACE):
            return self.INVALID_INDEX;

        self.playerMove(index);
        winState = self.checkWinState(self.PLAYER_MOVE);
        return winState;

    def doAITurn(self):
        self.counterMove();
        winState = self.checkWinState(self.AI_MOVE);
        return winState;

    def playerMove(self, index):
        self._board[index] = self.PLAYER_MOVE;
        self._availableMoves.remove(index);

    def aiMove(self, index):
        self._board[index] = self.AI_MOVE;
        self._availableMoves.remove(index);

    def checkWinState(self, symbol):
        if (self.checkColumnForWin(symbol) or
            self.checkRowForWin(symbol)    or
            self.checkDiagonalForWin(symbol)):
            return symbol;
        elif (len(self._availableMoves) == 0):
            return self.TIE;
        else:
            return self.CONTINUE_GAME;

    def checkColumnForWin(self, symbol):
        board = self._board;
        if ((board[0] == symbol and board[3] == symbol and board[6] == symbol)
            or
            (board[1] == symbol and board[4] == symbol and board[7] == symbol)
            or
            (board[2] == symbol and board[5] == symbol and board[8] == symbol)):
            return True;
        else:
            return False;

    def checkRowForWin(self, symbol):
        board = self._board;
        if ((board[0] == symbol and board[1] == symbol and board[2] == symbol)
            or
            (board[3] == symbol and board[4] == symbol and board[5] == symbol)
            or
            (board[6] == symbol and board[7] == symbol and board[8] == symbol)):
            return True;
        else:
            return False;

    def checkDiagonalForWin(self, symbol):
        board = self._board;
        if ((board[0] == symbol and board[4] == symbol and board[8] == symbol)
            or
            (board[2] == symbol and board[4] == symbol and board[6] == symbol)):
            return True;
        else:
            return False;

    def counterMove(self):
        if (not self.checkForPossibleWin(self.AI_MOVE)):
            if (not self.checkForPossibleWin(self.PLAYER_MOVE)):
                self.makeRegularMove();

    def checkForPossibleWin(self, symbol):
        for space in self._availableMoves:
            if (self.checkColumnForPossibleWin(space, symbol) or
                self.checkRowForPossibleWin(space, symbol)):
                self.aiMove(space);
                return True;
            elif (space == 4):
                if (self.checkLeftDiagonalForPossibleWin(space, symbol) or
                    self.checkRightDiagonalForPossibleWin(space, symbol)):
                    self.aiMove(space);
                    return True;
            elif (space % 4 == 0):
                if (self.checkLeftDiagonalForPossibleWin(space, symbol)):
                    self.aiMove(space);
                    return True;
            elif (space % 4 == 2):
                if (self.checkRightDiagonalForPossibleWin(space, symbol)):
                    self.aiMove(space);
                    return True;

        return False;

    def checkColumnForPossibleWin(self, space, symbol):
        otherTwoSpaces = [];

        if (space - 6 > -1):
            otherTwoSpaces.append(self._board[space - 6]);
        if (space - 3 > -1):
            otherTwoSpaces.append(self._board[space - 3]);
        if (space + 3 < 9):
            otherTwoSpaces.append(self._board[space + 3]);
        if (space + 6 < 9):
            otherTwoSpaces.append(self._board[space + 6]);

        if (otherTwoSpaces[0] == symbol and otherTwoSpaces[1] == symbol):
            return True;
        else:
            return False;

    def checkRowForPossibleWin(self, space, symbol):
        otherTwoSpaces = [];

        lowerLimit = 0;
        upperLimit = 0;
        spaceQuotient = space // 3;

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
            otherTwoSpaces.append(self._board[space - 2]);
        if (space - 1 > lowerLimit):
            otherTwoSpaces.append(self._board[space - 1]);
        if (space + 1 < upperLimit):
            otherTwoSpaces.append(self._board[space + 1]);
        if (space + 2 < upperLimit):
            otherTwoSpaces.append(self._board[space + 2]);

        if (otherTwoSpaces[0] == symbol and otherTwoSpaces[1] == symbol):
            return True;
        else:
            return False;

    def checkLeftDiagonalForPossibleWin(self, space, symbol):
        otherTwoSpaces = [];

        if (space - 8 > -1):
            otherTwoSpaces.append(self._board[space - 8]);
        if (space - 4 > -1):
            otherTwoSpaces.append(self._board[space - 4]);
        if (space + 4 < 9):
            otherTwoSpaces.append(self._board[space + 4]);
        if (space + 8 < 9):
            otherTwoSpaces.append(self._board[space + 8]);

        if (otherTwoSpaces[0] == symbol and otherTwoSpaces[1] == symbol):
            return True;
        else:
            return False;

    def checkRightDiagonalForPossibleWin(self, space, symbol):
        otherTwoSpaces = [];

        if (space - 4 > 1):
            otherTwoSpaces.append(self._board[space - 4]);
        if (space - 2 > 1):
            otherTwoSpaces.append(self._board[space - 2]);
        if (space + 2 < 7):
            otherTwoSpaces.append(self._board[space + 2]);
        if (space + 4 < 7):
            otherTwoSpaces.append(self._board[space + 4]);

        if (otherTwoSpaces[0] == symbol and otherTwoSpaces[1] == symbol):
            return True;
        else:
            return False;

    def makeRegularMove(self):
        playSpace = random.choice(self._availableMoves);
        self.aiMove(playSpace);

    def getBoard(self):
        return self._board;

    def clearBoard(self):
        for space in self._board:
            space = self.UNPLAYED_SPACE;

        self._availableMoves = [];
        for i in range(9):
            self._availableMoves.append(i);
