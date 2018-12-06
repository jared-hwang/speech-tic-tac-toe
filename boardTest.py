import sys
from board import Board

def main():
    myBoard = Board();

    while (True):
        index = int(input("index:"));

        winState = Board.doPlayerTurn(myBoard, index);
        if (winState == Board.AI_WINS):
            print("AI Wins!");
            break;
        elif (winState == Board.PLAYER_WINS):
            print("Player Wins!");
            break;
        elif (winState == Board.TIE):
            print("It's a Tie!");
            break;
        elif (winState == Board.INVALID_INDEX):
            print("You can't play there!");

        winState = Board.doAITurn(myBoard);
        if (winState == Board.AI_WINS):
            print("AI Wins!");
            break;
        elif (winState == Board.PLAYER_WINS):
            print("Player Wins!");
            break;
        elif (winState == Board.TIE):
            print("It's a Tie!");
            break;
        elif (winState == Board.INVALID_INDEX):
            print("You can't play there!");

        board = Board.getBoard(myBoard);
        for i in range(9):
            if (i == 2 or i == 5 or i == 8):
                print(board[i]);
            else:
                print(board[i], end = '  ');

    board = Board.getBoard(myBoard);
    for i in range(9):
        if (i == 2 or i == 5 or i == 8):
            print(board[i]);
        else:
            print(board[i], end = '  ');

if __name__ == '__main__':
    main();
