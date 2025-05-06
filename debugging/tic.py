def print_board(board):
    """Prints the Tic Tac Toe board."""
    for row in board:
        print(" | ".join(row))
        print("-" * 5)

def check_winner(board):
    """Checks if there is a winner."""
    # Check rows, columns, and diagonals for a winner
    for row in board:
        if row.count(row[0]) == len(row) and row[0] != " ":
            return row[0]

    for col in range(len(board[0])):
        if board[0][col] == board[1][col] == board[2][col] and board[0][col] != " ":
            return board[0][col]

    if board[0][0] == board[1][1] == board[2][2] and board[0][0] != " ":
        return board[0][0]

    if board[0][2] == board[1][1] == board[2][0] and board[0][2] != " ":
        return board[0][2]

    return None

def board_full(board):
    """Checks if the board is full."""
    return all(cell != " " for row in board for cell in row)

def tic_tac_toe():
    """Main function to play Tic Tac Toe."""
    board = [[" "]*3 for _ in range(3)]
    player = "X"
    while True:
        print_board(board)
        while True:
            try:
                row, col = map(int, input(f"Enter row and column (0, 1, or 2) for player {player}: ").split())
                if row not in range(3) or col not in range(3):
                    print("Out of bounds! Please enter 0, 1, or 2.")
                elif board[row][col] != " ":
                    print("That spot is already taken! Try again.")
                else:
                    break
            except ValueError:
                print("Invalid input! Please enter two numbers separated by a space.")
        board[row][col] = player
        winner = check_winner(board)
        if winner:
            print_board(board)
            print("Player " + winner + " wins!")
            break
        if board_full(board):
            print_board(board)
            print("It's a draw!")
            break
        player = "X" if player == "O" else "O"
tic_tac_toe()
