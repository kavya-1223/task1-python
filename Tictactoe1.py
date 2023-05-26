# Create the board
board = [' ' for _ in range(9)]

# Define winning combinations
winning_combinations = [
    [0, 1, 2], [3, 4, 5], [6, 7, 8],  # Rows
    [0, 3, 6], [1, 4, 7], [2, 5, 8],  # Columns
    [0, 4, 8], [2, 4, 6]              # Diagonals
]

# Function to display the board
def display_board():
    for row in [board[i:i + 3] for i in range(0, 9, 3)]:
        print(' | '.join(row))
        print('-' * 9)

# Function to check for a win
def check_win(player):
    for combination in winning_combinations:
        if all(board[i] == player for i in combination):
            return True
    return False

# Function to play the game
def play_game():
    current_player = 'X'
    while True:
        display_board()

        # Get the current player's move
        while True:
            position = int(input("Enter a position (1-9): ")) - 1
            if position in range(9) and board[position] == ' ':
                break
            print("Invalid move. Try again.")

        # Update the board with the player's move
        board[position] = current_player

        # Check for a win
        if check_win(current_player):
            display_board()
            print("Player", current_player, "wins!")
            break

        # Check for a tie
        if ' ' not in board:
            display_board()
            print("It's a tie!")
            break

        # Switch to the other player
        current_player = 'O' if current_player == 'X' else 'X'

# Start the game
play_game()