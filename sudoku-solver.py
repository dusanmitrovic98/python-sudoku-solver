def solve_sudoku(board):
    if not find_empty_cell(board):
        return True

    row, col = find_empty_cell(board)

    for num in range(1, 10):
        if is_valid(board, num, row, col):
            board[row][col] = num

            if solve_sudoku(board):
                return True

            board[row][col] = 0

    return False


def find_empty_cell(board):
    for i in range(9):
        for j in range(9):
            if board[i][j] == 0:
                return i, j
    return None


def is_valid(board, num, row, col):
    # Check row
    for i in range(9):
        if board[row][i] == num:
            return False

    # Check column
    for i in range(9):
        if board[i][col] == num:
            return False

    # Check 3x3 box
    start_row = (row // 3) * 3
    start_col = (col // 3) * 3

    for i in range(3):
        for j in range(3):
            if board[start_row + i][start_col + j] == num:
                return False

    return True


def print_board(board):
    for i in range(9):
        if i % 3 == 0 and i != 0:
            print("- - - - - - - - - - - -")

        for j in range(9):
            if j % 3 == 0 and j != 0:
                print(" | ", end="")

            if j == 8:
                print(board[i][j])
            else:
                print(str(board[i][j]) + " ", end="")


# Example Sudoku board (0 represents empty cells)
# board = [
#    [5, 3, 0, 0, 7, 0, 0, 0, 0],
#    [6, 0, 0, 1, 9, 5, 0, 0, 0],
#    [0, 9, 8, 0, 0, 0, 0, 6, 0],
#    [8, 0, 0, 0, 6, 0, 0, 0, 3],
#    [4, 0, 0, 8, 0, 3, 0, 0, 1],
#    [7, 0, 0, 0, 2, 0, 0, 0, 6],
#    [0, 6, 0, 0, 0, 0, 2, 8, 0],
#    [0, 0, 0, 4, 1, 9, 0, 0, 5],
#    [0, 0, 0, 0, 8, 0, 0, 7, 9]
#]

board = [
    [0, 0, 0, 0, 0, 0, 0, 1, 0],
    [0, 2, 0, 0, 5, 6, 0, 0, 0],
    [7, 0, 0, 0, 0, 0, 0, 0, 8],
    [0, 0, 8, 0, 0, 4, 0, 0, 2],
    [6, 0, 4, 0, 0, 0, 5, 0, 3],
    [2, 0, 0, 8, 0, 0, 7, 0, 0],
    [3, 0, 0, 0, 0, 0, 0, 0, 1],
    [0, 0, 0, 7, 8, 0, 0, 6, 0],
    [0, 4, 0, 0, 0, 0, 0, 0, 0]
]

if solve_sudoku(board):
    print("Sudoku Solved:")
