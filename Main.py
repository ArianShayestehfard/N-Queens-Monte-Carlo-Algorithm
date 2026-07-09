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