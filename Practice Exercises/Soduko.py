def is_valid_sudoku(board):
    rows = [set() for _ in range(9)]
    cols = [set() for _ in range(9)]
    boxes = [set() for _ in range(9)]

    for i in range(9):
        for j in range(9):
            cell = board[i][j]
            if cell == ".":
                continue
            if cell in rows[i] or cell in cols[j] or cell in boxes[i // 3 * 3 + j // 3]:
                return False
            rows[i].add(cell)
            cols[j].add(cell)
            boxes[i // 3 * 3 + j // 3].add(cell)

    return True

# Example usage
sudoku_board = [
    ["5","3",".",".","7",".",".",".","."],
    ["6",".",".","1","9","5",".",".","."],
    [".","9","8",".",".",".",".","6","."],
    ["8",".",".",".","6",".",".",".","3"],
    ["4",".",".","8",".","3",".",".","1"],
    ["7",".",".",".","2",".",".",".","6"],
    [".","6",".",".",".",".","2","8","."],
    [".",".",".","4","1","9",".",".","5"],
    [".",".",".",".","8",".",".","7","9"]
]
result = is_valid_sudoku(sudoku_board)
