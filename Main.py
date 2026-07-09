import random

def safe(board, row, col):
    for i in range(row):
        if board[i] == col or abs(board[i]-col) == row-i:
            return False
    return True