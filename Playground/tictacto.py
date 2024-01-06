def print_board(board):
    for row in board:
        print(" | ".join(row))
        if row != board[-1]:
            print("-----------")

def check_win(board, player):
    # Check rows, columns, and diagonals for a win
    for i in range(3):
        if all(board[i][j] == player for j in range(3)) or \
           all(board[j][i] == player for j in range(3)):
            return True
    if all(board[i][i] == player for i in range(3)) or \
       all(board[i][2 - i] == player for i in range(3)):
        return True
    return False

def is_full(board):
    return all(board[i][j] != " " for i in range(3) for j in range(3))

def main():
    board = [[" " for _ in range(3)] for _ in range(3)]
    current_player = "X"
    
    while True:
        print_board(board)
        print(f"Player {current_player}, it's your turn.")
        
        row = int(input("Enter the row (1, 2, or 3): ") ) - 1
        col = int(input("Enter the column (1, 2, or 3): ") ) - 1

        if row in range(3) and col in range(3) and board[row][col] == " ":
            board[row][col] = current_player
            if check_win(board, current_player):
                print_board(board)
                print(f"Player {current_player} wins! Congratulations!")
                break
            elif is_full(board):
                print_board(board)
                print("It's a draw! The game is over.")
                break
            else:
                current_player = "O" if current_player == "X" else "X"
        else:
            print("Invalid move. Please try again.")

if __name__ == "__main__":
    main()
