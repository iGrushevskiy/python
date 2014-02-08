#importing random function for further random column and row index generation
from random import randint

#creating empty parent list 
board = []

'''populating the parent list with 5 child lists
in order to create multidimensial matrix playing desk
'''
for x in range(5):
    board.append(["O"] * 5)

def print_board(board):
    '''function used for removing 'O' mask and joining
    one row values together
    '''
    for row in board:
        print " ".join(row)

print "Let's play Battleship!"
print_board(board)

def random_row(board):
    #generating random row index
    return randint(0, len(board) - 1)

def random_col(board):
    #generating random column index
    return randint(0, len(board[0]) - 1)

#assigning random col and random row vaues to our ship
ship_row = random_row(board)
ship_col = random_col(board)

#below code is used for debugging reasons
print ship_row
print ship_col

# Everything from here on should go in your for loop used for counting turns!
# Be sure to indent four spaces!
for turn in range(4):
    guess_row = int(raw_input("Guess Row:"))
    guess_col = int(raw_input("Guess Col:"))
    
    
    if guess_row == ship_row and guess_col == ship_col:
        print "Congratulations! You sunk my battleship!"
        break
    else:
        if turn==3:
            print "Game Over"
        elif (guess_row < 0 or guess_row > 4) or (guess_col < 0 or guess_col > 4):
            print "Oops, that's not even in the ocean."
        elif(board[guess_row][guess_col] == "X"):
            print "You guessed that one already."
        else:
            print "You missed my battleship!"
            board[guess_row][guess_col] = "X"
            print_board(board)
        # Print (turn + 1) here!
        print "You made %d turn"%(turn+1)
