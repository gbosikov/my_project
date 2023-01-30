from random import randrange



def init_borad():
    board = [['' for row in range(1, 4)] for column in range(1, 4)]
    pos = 1
    for row in range(3):
        for column in range(3):
            board[row][column] = pos
            pos += 1

    return board


print(init_borad())

def display_board(board):
    print('+-------' * 3, '+', sep='')
    for row in range(1, 4):
        for column in range(1, 4):
            print('|       ' * 3, '|', sep='')



    print('+-------' * 3, '+', sep='')
    return


print(display_board(init_borad()))

def enter_move(board):
    # The function accepts the board's current status, asks the user about their move, 
    # checks the input, and updates the board according to the user's decision.
    pass


def make_list_of_free_fields(board):
    # The function browses the board and builds a list of all the free squares; 
    # the list consists of tuples, while each tuple is a pair of row and column numbers.
    pass


def victory_for(board, sign):
    # The function analyzes the board's status in order to check if 
    # the player using 'O's or 'X's has won the game
    pass


def draw_move(board):
    # The function draws the computer's move and updates the board.
    pass


some_list = [
    '+-------+-------+-------+',
    '|       |       |       |',
    '|   1   |   2   |   3   |',
    '|       |       |       |',
    '+-------+-------+-------+',
    '|       |       |       |',
    '|   4   |   X   |   6   |',
    '|       |       |       |',
    '+-------+-------+-------+',
    '|       |       |       |',
    '|   7   |   8   |   9   |',
    '|       |       |       |',
    '+-------+-------+-------+'

]


# def init_borad():
#     global current_player
#     board = [['' for x in range(3)] for i in range(3)]
#     pos = 1
#     for row in range(3):
#         for column in range(3):
#             board[row][column] = pos
#             pos += 1
#
#     board[1][1] = 'X'
#     current_player = 'O'
#     return board
#
# print(init_borad())

