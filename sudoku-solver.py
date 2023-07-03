def solve_sudoku(board):
    if not find_empty_cell(board):
        return True

    row, col = find_empty_cell(board)
