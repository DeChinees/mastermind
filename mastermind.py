import random

count = 0
secret = []
guess = []
board = {}

def showSecret( secret ):
    print ('secret: ', secret)
    return

def printBoard( board ):
    if (len(board) != 0):
        print(f"Your board looks like this:")
        for k, v in board.items():
            print(k, v)
    else:
        print(f"Board is empty!")
    return

def check( secret, playersGuess ):
    i = 0
    x = 0
    for p, s in zip(playersGuess, secret):
        if ((p in secret) & (p !=s)):
            i += 1    
        if (p == s):
            x += 1
    print(f"found {i} correct number(s) in the wrong place")
    print(f"found {x} correct numbers(s) in the right position")

    if (x == 4):
        print(f"Congratulations, You broke the code!")
        return True
    else:    
        return False

def userInput():
    a = 0
    c = []
    i = -1
    while (a <= 3):
        i = input("number:")
        if (i == 666):
            exit()
        # take only the first character.    
        if (int(i[0]) >= 0) & (int(i[0]) <= 9):
            c.append(int(i[0]))
            a += 1
        else:
            print(f"The number {int(i[0])} is invalid. Need to between 0 and 9")
    return c

## To the batmobile
def mastermind():
    secret = [int(item) for item in str(random.randrange(1000,9999))]
    while (check( secret, guess ) != True):
        print(f"To exit game enter the number 666.")
        #showSecret(secret)
        count += 1
        guess = userInput()
        board[f'Guess-{count}'] = guess
        printBoard(board)
## All villans are in Arkham