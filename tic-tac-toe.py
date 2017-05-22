# Tic-Tac-Toe

import random

def drawBoard(board):
    # this function prints the board

    # "board" is a list of strings
    print(board[7] + '|' + board[8] + '|' + board[9])
    print('-+-+-')
    print(board[4] + '|' + board[5] + '|' + board[6])
    print('-+-+-')
    print(board[3] + '|' + board[2] + '|' + board[1])

def inputPlayerLetter():
    #player choose letter(X or O)

    letter = ''
    while not (letter == "X" or letter == "O"):
        print("Do you want to be X or O")
        letter = input().upper()

        #first element players letter; second computers letter
        if letter == "X":
            return ["X", "O"]
        else:
            return ["O", "X"]

def whoGoesFirst():
    # rand choose who goes first
    if random.randint(0,1) == 0:
        return "computer"
    else:
        return "player"

def makeMove(board, letter, move):
    
