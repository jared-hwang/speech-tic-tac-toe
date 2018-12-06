import sys
from board import Board

def main():
    gameOver = False;
    myBoard = Board();

    while (not gameOver):
        row = int(input("Row:"));
        column = int(input("Column:"));

        winState = Board.doTurn(myBoard, row, column);
        board = Board.getBoard(myBoard);

        for i in range(9):
            if (i == 2 or i == 5 or i == 8):
                print(board[i]);
            else:
                print(board[i], end = '  ');

        if (winState == Board.AI_WINS):
            print("AI Wins!");
            gameOver = True;
        elif (winState == Board.PLAYER_WINS):
            print("Player Wins!");
            gameOver = True;
        elif (winState == Board.TIE):
            print("It's a Tie!");
            gameOver = True;
        elif (winState == Board.INVALID_INDEX):
            print("You can't play there!");

if __name__ == '__main__':
    main();
