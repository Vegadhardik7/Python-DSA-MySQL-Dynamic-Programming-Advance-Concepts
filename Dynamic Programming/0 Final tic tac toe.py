# tic tac toe

print("tic tac toe")

'''
tic tac toe
[
    [-,-,-],
    [-,-,-],
    [-,-,-]
]

user_input = 1-9
if they enter anything else: tell them to go again
check if the user_input is already taken
add it to the board
check if user won: checking rows, columns, and diagonals
toggle between user upon successful moves


- Important Functions

* Board
* Display
* Play Game
    * Handle Turn
* Check Win
    * Check rows
    * Check col
    * Check diagonals
* Check tie
* Flip Player

'''

# Creating board an 2d array
board =     ["-","-","-",
             "-","-","-",
             "-","-","-"]

game_still_going = True

# Who Won or Tie?
winner = None

# Whos Turn is it?
current_player = "X"

# Play a game of tic tac toe
def play_game():
    display_board()  # Display Board

    # While the game is still going
    while game_still_going:

        # Handle a single turn of an arbitrary player
        handle_turn(current_player)

        # check if the game has ended
        check_if_game_over()

        # Flip to the other player
        flip_player()

    if winner == 'X' or winner == "O":
        print(winner + " Won.")
    elif winner == None:
        print("Tie.")


# Display board
def display_board():
    print(board[0] + " | " + board[1] + " | " + board[2])
    print(board[3] + " | " + board[4] + " | " + board[5])
    print(board[6] + " | " + board[7] + " | " + board[8])

# Handle a single turn of an arbitary player
def handle_turn(player):

    print(player + "'s turn.")
    position = input("Choose a position from 1 to 9: ")

    valid = False
    while not valid:
        while position not in ["1","2","3","4","5","6","7","8","9"] or 0>int(position)>9:
            position = input("Please choose a position from 1 to 9: ")

        position = int(position) - 1        # Position 1 means index 0 and so on

        if board[position] == "-":
            valid = True
        else:
            print("You can't place there")



    board[position] = player               # Inputing the X at the position
    display_board()

def check_if_game_over():
    check_if_win()
    check_if_tie()



def check_if_win():

    # Setting up global variable
    global winner

    # check_row
    row_winner = check_row()

    # check_col
    col_winner = check_col()

    # check_diagonal
    diag_winner = check_diagonals()

    if row_winner:
        # win
        winner = row_winner
    elif col_winner:
        # win
        winner = col_winner
    elif diag_winner:
        #win
        winner = diag_winner
    else:
        # no win
        winner = None


def check_row():
    global game_still_going
    row_1 = board[0] == board[1] == board[2] != "-" # all are equal but not equal to - than win
    row_2 = board[3] == board[4] == board[5] != "-"
    row_3 = board[6] == board[7] == board[8] != "-"

    # If any row has match than win
    if row_1 or row_2 or row_3:
        game_still_going = False

    # Return winner X or O
    if row_1:
        return board[0]
    elif row_2:
        return board[3]
    elif row_3:
        return board[6]
    return

def check_col():
    global game_still_going
    col_1 = board[0] == board[3] == board[6] != "-"  # all are equal but not equal to - than win
    col_2 = board[1] == board[4] == board[7] != "-"
    col_3 = board[2] == board[5] == board[8] != "-"

    # If any col has match than win
    if col_1 or col_2 or col_3:
        game_still_going = False

    # Return winner X or O
    if col_1:
        return board[0]
    elif col_2:
        return board[1]
    elif col_3:
        return board[2]
    return


def check_diagonals():
    global game_still_going
    diag_1 = board[0] == board[4] == board[8] != "-"  # all are equal but not equal to - than win
    diag_2 = board[2] == board[4] == board[6] != "-"

    # If any diag has match than win
    if diag_1 or diag_2:
        game_still_going = False

    # Return winner X or O
    if diag_1:
        return board[0]
    elif diag_2:
        return board[2]

    return

def check_if_tie():

    global game_still_going

    if "-" not in board:
        game_still_going = False
    return


def flip_player():

    global current_player

    if current_player == "X":
        current_player = "O"
    elif current_player == "O":
        current_player = "X"
    return

play_game()


