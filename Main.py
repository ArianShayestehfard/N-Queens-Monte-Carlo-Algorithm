import random

def safe(board, row, col):
    for i in range(row):
        if board[i] == col or abs(board[i]-col) == row-i:
            return False
    return True

def exact_nodes(board, row, n):
    if row == n:
        return 1
    total = 0
    for col in range(n):
        if safe(board, row, col):
            board[row] = col
            total += exact_nodes(board, row+1, n)
    return total

def monte_carlo_nodes(n, trials):
    total = 0
    for _ in range(trials):
        board = [-1]*n
        row = 0
        nodes = 0
        while True:
            nodes += 1
            if row == n:
                total += nodes
                break
            cols = [c for c in range(n) if safe(board, row, c)]
            if not cols:
                break
            board[row] = random.choice(cols)
            row += 1
    return total/trials