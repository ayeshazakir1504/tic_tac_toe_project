import random

# Board
board = [" " for _ in range(9)]

# Print board
def print_board():
    print("\n")
    for i in range(3):
        print(" | ".join(board[i*3:(i+1)*3]))
        if i < 2:
            print("--+---+--")
    print("\n")

# Check winner
def check_winner(player):
    win_cond = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],  # rows
        [0, 3, 6], [1, 4, 7], [2, 5, 8],  # columns
        [0, 4, 8], [2, 4, 6]              # diagonals
    ]
    for cond in win_cond:
        if board[cond[0]] == board[cond[1]] == board[cond[2]] == player:
            return True
    return False

# Get available moves
def available_moves():
    return [i for i in range(9) if board[i] == " "]

# Game loop
def play_game():
    human = "X"
    computer = "O"
    current_player = human

    for turn in range(9):
        print_board()

        if current_player == human:
            move = int(input("Your move (1-9): ")) - 1
            if board[move] != " ":
                print("Invalid move, try again!")
                continue
        else:
            move = random.choice(available_moves())
            print(f"Computer chooses {move+1}")

        board[move] = current_player

        if check_winner(current_player):
            print_board()
            if current_player == human:
                print("🎉 You win!")
            else:
                print("💻 Computer wins!")
            return

        current_player = computer if current_player == human else human

    print_board()
    print("It's a draw!")

# Start
play_game()
