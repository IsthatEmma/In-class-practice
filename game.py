def print_board(board):
    """Prints the Tic-Tac-Toe board."""
    print("---------")
    for row in board:
        print(f"| {' '.join(row)} |")
    print("---------")

def check_winner(board, player):
    """Checks if the given player has won."""
    win_conditions = [
        # Check rows
        [board[0][0], board[0][1], board[0][2]],
        [board[1][0], board[1][1], board[1][2]],
        [board[2][0], board[2][1], board[2][2]],
        # Check columns
        [board[0][0], board[1][0], board[2][0]],
        [board[0][1], board[1][1], board[2][1]],
        [board[0][2], board[1][2], board[2][2]],
        # Check diagonals
        [board[0][0], board[1][1], board[2][2]],
        [board[0][2], board[1][1], board[2][0]]
    ]
    return [player, player, player] in win_conditions

def check_draw(board):
    """Checks if the board is full and no winner."""
    for row in board:
        if ' ' in row:
            return False
    return True

def is_valid_move(board, row, col):
    """Checks if the move is valid."""
    return board[row][col] == ' '

def tic_tac_toe():
    """Main function to play Tic-Tac-Toe."""
    board = [[' ' for _ in range(3)] for _ in range(3)]
    current_player = 'X'
    
    print("Welcome to Tic-Tac-Toe!")
    
    while True:
        print_board(board)
        
        # Get the move from the current player
        print(f"Player {current_player}, enter your move (row and column): ")
        row, col = map(int, input("Enter row and column numbers (0-2): ").split())
        
        if not (0 <= row < 3 and 0 <= col < 3):
            print("Invalid move. Please enter row and column numbers between 0 and 2.")
            continue
        
        if not is_valid_move(board, row, col):
            print("Invalid move. The cell is already occupied.")
            continue
        
        # Make the move
        board[row][col] = current_player
        
        # Check if the current player won
        if check_winner(board, current_player):
            print_board(board)
            print(f"Player {current_player} wins!")
            break
        
        # Check if it's a draw
        if check_draw(board):
            print_board(board)
            print("The game is a draw!")
            break
        
        # Switch player
        current_player = 'O' if current_player == 'X' else 'X'

if __name__ == "__main__":
    tic_tac_toe()
