import mastermind as mastermind

count = 0
secret = [1, 2, 4, 5]
guess = []
board = {}

def test_check():
    guess = [1, 2, 4, 5]
    assert mastermind.check( secret, guess ) == True
    guess = [1, 1, 1, 1]
    assert mastermind.check( secret, guess ) == False
    