import random

def print_board(board):
    print("   |   |")
    print(" " + board[0] + " | " + board[1] + " | " + board[2])
    print("   |   |")
    print("-----------")
    print("   |   |")
    print(" " + board[3] + " | " + board[4] + " | " + board[5])
    print("   |   |")
    print("-----------")
    print("   |   |")
    print(" " + board[6] + " | " + board[7] + " | " + board[8])
    print("   |   |")


def play_game():
    board = [" ", " ", " ", " ", " ", " ", " ", " ", " "]
    player = choose_first()
    game_over = False

    while not game_over:
        print_board(board)
        print("It's " + player + "'s turn.")

        move = input("Enter a position from 1-9: ")

        valid_move = False
        while not valid_move:
            while move not in ["1", "2", "3", "4", "5", "6", "7", "8", "9"]:
                move = input("Invalid input. Enter a position from 1-9: ")

            move = int(move) - 1

            if board[move] == " ":
                valid_move = True
            else:
                print("That position is already taken. Try again.")

        board[move] = player

        if check_win(board, player):
            print_board(board)
            print(player + " wins!")
            game_over = True
        elif check_tie(board):
            print_board(board)
            print("Tie game!")
            game_over = True
        else:
            if player == "X":
                player = "O"
            else:
                player = "X"

def choose_first():
    if random.randint(0, 1) == 0:
        return 'X'
    else:
        return 'O'

def check_win(board, player):
    if (board[0] == player and board[1] == player and board[2] == player) or \
            (board[3] == player and board[4] == player and board[5] == player) or \
            (board[6] == player and board[7] == player and board[8] == player) or \
            (board[0] == player and board[3] == player and board[6] == player) or \
            (board[1] == player and board[4] == player and board[7] == player) or \
            (board[2] == player and board[5] == player and board[8] == player) or \
            (board[0] == player and board[4] == player and board[8] == player) or \
            (board[2] == player and board[4] == player and board[6] == player):
        return True
    else:
        return False


def check_tie(board):
    if " " not in board:
        return True
    else:
        return False


play_game()
