def print_board(board):
    print("\nSudoku Grid:")
    for row in board:
        print(" ".join(str(num) if num != 0 else '.' for num in row))


def is_valid(board, row, col, num):
    # Row check
    if num in board[row]:
        return False

    # Column check
    for i in range(9):
        if board[i][col] == num:
            return False

    # Subgrid check
    start_row, start_col = row - row % 3, col - col % 3
    for i in range(3):
        for j in range(3):
            if board[start_row + i][start_col + j] == num:
                return False

    return True


def solve_sudoku(board):
    for row in range(9):
        for col in range(9):
            if board[row][col] == 0:

                for num in range(1, 10):
                    if is_valid(board, row, col, num):
                        board[row][col] = num

                        if solve_sudoku(board):
                            return True

                        board[row][col] = 0  # Backtrack

                return False

    return True


def input_board():
    print("Enter Sudoku (use 0 for empty cells):")
    board = []
    for _ in range(9):
        row = list(map(int, input().split()))
        board.append(row)
    return board


def main():
    board = []

    while True:
        print("\n--- MENU ---")
        print("1. Enter Sudoku")
        print("2. Solve Sudoku")
        print("3. Display Sudoku")
        print("4. Exit")

        choice = int(input("Enter choice: "))

        if choice == 1:
            board = input_board()

        elif choice == 2:
            if board:
                if solve_sudoku(board):
                    print("Sudoku solved successfully.")
                else:
                    print("No solution exists.")
            else:
                print("Enter Sudoku first.")

        elif choice == 3:
            if board:
                print_board(board)
            else:
                print("No Sudoku available.")

        elif choice == 4:
            break

        else:
            print("Invalid choice.")


if __name__ == "__main__":
    main()