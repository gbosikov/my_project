def init_board():
    board = [['' for _ in range(1, 4)] for _ in range(1, 4)]
    pos = 1
    for row in range(3):
        for col in range(3):
            board[row][col] = pos
            pos += 1
    board[1][1] = 'X'

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
    turn_ok = False
    while not turn_ok:
        user_inp = input('Enter some digit from 1 to 9: \n')
        if len(user_inp) != 1 or user_inp <= '0' or user_inp > '9':
            print("Your move isn't correct, retry please ")
            continue
        for row in range(3):
            for col in range(3):
                if int(user_inp) == board[row][col] and board[row][col] in ['X', 'O']:
                    print("Your move isn't correct, this square is occupied, please retry again !")

                elif int(user_inp) == board[row][col]:
                    board[row][col] = 'O'

        turn_ok = not turn_ok
    return board


some_lsr = [[1, 2, 3], [4, 'X', 6], [7, 8, 9]]


print(enter_move(some_lsr))


def make_list_of_free_fields(board):
    # The function browses the board and builds a list of all the free squares;
    # the list consists of tuples, while each tuple is a pair of row and column numbers.
    free_fields = []
    for row in range(3):
        for col in range(3):
            if board[row][col] not in ['O', 'X']:
                free_fields.append(board[row][col])
    return free_fields


print(make_list_of_free_fields(some_lsr))

def victory_for(board, sign):
    # The function analyzes the board's status in order to check if
    # the player using 'O's or 'X's has won the game

    return


def draw_move(board):
    # The function draws the computer's move and updates the board.
    return
