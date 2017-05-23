import random

NUM_DIGITS = 3
MAX_GUESS = 10

def getSecretNum():
    # return a string of numbers
    numbers = list(range(1,10))
    random.shuffle(numbers)
    secretNum = ' '
    for i in range(NUM_DIGITS):
        secretNum += str(numbers[i])
    return secretNum

def getClues(guess, secretNum):
    # Return a string with Pico, Fermi, & Bagels clues to the user.
    if guess == secretNum:
        return "You got it!"

    clues = []
    
