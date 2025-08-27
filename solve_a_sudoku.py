# Linked Learning - Python Code Challenges
# 27 Aug, 2025
# solve a sudoku
from itertools import product

puzzle = [[5, 3, 0, 0, 7, 0, 0, 0, 0],
          [6, 0, 0, 1, 9, 5, 0, 0, 0],
          [0, 9, 8, 0, 0, 0, 0, 6, 0],
          [8, 0, 0, 0, 6, 0, 0, 0, 3],
          [4, 0, 0, 8, 0, 3, 0, 0, 1],
          [7, 0, 0, 0, 2, 0, 0, 0, 6],
          [0, 6, 0, 0, 0, 0, 2, 8, 0],
          [0, 0, 0, 4, 1, 9, 0, 0, 5],
          [0, 0, 0, 0, 8, 0, 0, 7, 9]]


def find_empty(n):
    for r in range(9):
        for c in range(9):
            if n[r][c] == 0:
                return r, c


def is_valid(board, row, col, num):
    if num in board[row]:
        return False

    if num in [board[r][col] for r in range(9)]:
        return False

    # check 3x3
    box_r, box_c = row // 3, col // 3

    for r in range(box_r * 3, box_r * 3 + 3):
        for c in range(box_c * 3, box_c * 3 + 3):
            if board[r][c] == num:
                return False

    return True


def solve(n):
    empty = find_empty(n)

    if not empty:
        return True

    row, col = empty

    for num in range(1, 10):
        if is_valid(n, row, col, num):
            n[row][col] = num

            if solve(n):
                return True

            n[row][col] = 0
    return False







solve(puzzle)
