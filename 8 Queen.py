def solve(board, row):
    if row == 8:
        print(board)
        return True

    for col in range(8):
        if safe(board, row, col):
            board[row] = col
            if solve(board, row + 1):
                return True
    return False

def safe(board, row, col):
    for r in range(row):
        if board[r] == col or abs(board[r] - col) == abs(r - row):
            return False
    return True

board = [-1] * 8
solve(board, 0)
