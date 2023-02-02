def init_board():
    board = [['' for _ in range(1, 4)] for _ in range(1, 4)]
    pos = 1
    for row in range(3):
        for col in range(3):
            board[row][col] = pos
            pos += 1

    return board


print(init_board())



def display_board(board):
    # The function accepts one parameter containing the board's current status
    # and prints it out to the console.
    print('+-------' * 3, '+', sep='')
    for row in range(3):
        print('|       ' * 3, '|', sep='')
        for col in range(3):
            print('|  ', board[row][col], '  ', end='')
        print('|')
        print('|       ' * 3, '|', sep='')
        print('+-------' * 3, '+', sep='')
    return


print(display_board(init_board()))



def enter_move(board):
    # The function accepts the board's current status, asks the user about their move,
    # checks the input, and updates the board according to the user's decision.

    while True:
        user_inp = input('Enter some digit from 1 to 9: \n')
        if len(user_inp) != 0 or int(user_inp) <= 0 or int(user_inp) > 9:
            print("Your move isn't correct, retry please ")
            continue
    return


def make_list_of_free_fields(board):
    # The function browses the board and builds a list of all the free squares;
    # the list consists of tuples, while each tuple is a pair of row and column numbers.
    return


def victory_for(board, sign):
    # The function analyzes the board's status in order to check if
    # the player using 'O's or 'X's has won the game
    return


def draw_move(board):
    # The function draws the computer's move and updates the board.
    return
