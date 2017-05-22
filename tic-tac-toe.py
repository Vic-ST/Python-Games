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
    board[move] == letter

def isWinner(bo,le):
    # Returns true if the player has won
    #bo == board, le == letter
    return ((bo[7] == le and bo[8] == le and bo[9] == le) or # This is the top of the board
            (bo[4] == le and bo[5] == le and bo[6] == le) or # across the middle
            (bo[3] == le and bo[2] == le and bo[1] == le) or # across the bottom
            (bo[7] == le and bo[4] == le and bo[1] == le) or # down the left side
            (bo[9] == le and bo[6] == le and bo[3] == le) or # down the middle
            (bo[9] == le and bo[6] == le and bo[3] == le) or # down the right side
            (bo[7] == le and bo[5] == le and bo[3] == le) or # diagonal
            (bo[9] == le and bo[5] == le and bo[1] == le)) # diagonal

def getBoardCopy(board):
    # make a copy of the board list and return it
    boardCopy = []
    for i in board:
        boardCopy.append(i)
    return boardCopy

def isSpaceFree(board, move):
    # return true if free
    return board[move] == ' '

def getPlayerMove(board):
    # get player move
    move = ' '
    while move not in '1 2 3 4 5 6 7 8 9'.split() or not isSpaceFree(board, int(move)):
        print("Whats your next move?")
        move = input()
    return int(move)

def chooseRandomMoveFromList(board, movesList):
    # return valid move from board
    # return none if none
    possibleMoves = []
    for i in movesList:
        if isSpaceFree(board, i):
            possibleMoves.append(i)

    if len(possibleMoves) != 0:
        return random.choice(possibleMoves)
    else:
        return None

def getComputerMove(board,computerLetter):
    # Get computer move
    if computerLetter == "X":
        playerLetter == "O"
    else:
        playerLetter == "X"

    # Here is the first algorithm
    # Check if you can win on the next move
    for i in range(1,10):
        boardCopy = getBoardCopy(board)
        if isSpaceFree(boardCopy, i):
            makeMove(boardCopy, computerLetter)
            if isWinner(boardCopy, playerLetter):
                return i

    # Check if the player could win on there next turn and block them
    for i in range(1,10):
        boardCopy = getBoardCopy(board)
        if isSpaceFree(boardCopy, i):
            makeMove(boardCopy, computerLetter, i)
            if isWinner(boardCopy, playerLetter):
                return i

    # Try to take one of the corners, if they are free
    move = chooseRandomMoveFromList(board, [1,3,7,9])
    if move != None:
        return move

    # Try to take the center, if its free.
    if spaceIsFree(board, 5):
        return 5

    # Move on one of the sides
    return chooseRandomMoveFromList(board, [2,4,6,8])

def isBoardFull(board):
    # Return True if all spaces on the board are full. Otherwise, return False
    for i in range(1,10):
        if isSpaceFree(board, i):
            return False
    return True


print("Welcome to Tic-Tac-Toe!")

while True:
    # reset the board
    theBoard = [' '] * 10
    playerLetter, computerLetter = inputPlayerLetter()
    turn = whoGoesFirst
    print("The " + turn + " will go first.")
    gameIsPlaying = True

    while gameIsPlaying:
        
