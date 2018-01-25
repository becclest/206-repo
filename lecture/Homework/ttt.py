python ttt.py

def generateBoard(board)
#Generates 3 x 3 matrix of board that is passed
# Uses a list of 9 strings
    print ('    |   |   ')
    print ('' +board[6]+ '    | ' +board[7]+ '  |   ' +board[8] )
    print ('    |   |   ')
    print ('-----------')
    print ('    |   |   ')
    print ('' +board[3]+ '    | ' +board[4]+ '  | ' +board[5] )
    print ('    |   |   ')
    print ('-----------')
    print ('    |   |   ')
    print ('' +board[0]+ '    | ' +board[1]+ '  |' +board[2] )
    print ('    |   |   ')

    board = [SW, SC, SE, CW, C, CE, NW, NC, NE]

# The player decides whether to be X or O
# Returns a list with the player's selection first, other as the second
# Needs to be able to confirm player's selection using verification below
def inputPlayerType

    letter = str(input("Would you like to be X or O? ")).upper()
    valid_letters = ['X', 'O']
    if letter != 'X' or letter != 'O':
        letter = input("Please type the right symbol (X or O): ")
    if letter == 'X':
        return valid_letters
    else:
        return valid_letters[::-1]


#Checks to see if list element is a valid move and if there's no one in that
# place.
# Given the board and player's moves, returns True if the player has won.

def winning_moves(board, letter):

    #Across the top row
    (board[6] == letter and board[7] == letter and board[8] == letter)

    #Across the middle row
    (board[3] == letter and board[4] == letter and board[5] == letter)

    #Across the bottom row
    (board[0] == letter and board[1] == letter and board[2] == letter)

    #Down the left column
    (board[6] == letter and board[3] == letter and board[0] == letter)

    #Down the middle column
    (board[7] == letter and board[4] == letter and board[1] == letter)

    #Down the right column
    (board[8] == letter and board[5] == letter and board[2] == letter)

    #Across the left top corner to the bottom right
    (board[6] == letter and board[4] == letter and board[2] == letter)

    # Across the right top corner to the bottom left corner
    (board[8] == letter and board[4] == letter and board[0] == letter)


# Make a duplicate of the board list and return it the duplicate.
# Allows players to view the board as the game is being played
def getBoardCopy(board):

    duplicateBoard = []

    for i in board:
        duplicateBoard.append(i)
    print "CURRENT BOARD: "
    return duplicateBoard

# User input to allow moves on the board
def makeMove (Board, Coordinate, Letter):
    Board[Coordinate] = Letter


# Checks if the matrix element is open or if there's a letter at that Coordinate
def check_free_space(Board, Coordinate):
    return Board[Coordinate] == ' '

#Lets the player type in their move based on the coordiante
def getPlayerMove(Board):
    Move = ' '
    while Move not in board[].split() or not check_free_space(board, int(move)):
        print ("Please select your next move: ")
        Move = Input()
    return int(move)
