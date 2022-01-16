# solver.py
import numpy as np

#=============solving sudoku board================
board = [[5, 3, 0, 0, 7, 0, 0, 0, 0],
        [6, 0, 0, 1, 9, 5, 0, 0, 0],
        [0, 9, 8, 0, 0, 0, 0, 6, 0],
        [8, 0, 0, 0, 6, 0, 0, 0, 3],
        [4, 0, 0, 8, 0, 3, 0, 0, 1],
        [7, 0, 0, 0, 2, 0, 0, 0, 6],
        [0, 6, 0, 0, 0, 0, 2, 8, 0],
        [0, 0, 0, 4, 1, 9, 0, 0, 5],
        [0, 0, 0, 0, 8, 0, 0, 7, 9]]

def possible(y, x, n):
        for i in range(0, 9):
                if board[y][i] == n:
                        return False
        for i in range (0, 9):
                if board[i][x] == n:
                        return False
        x0 = (x // 3) * 3
        y0 = (y // 3) * 3
 
        for i in range (0, 3):
                for j in range(0, 3):
                        if board[y0 + i][x0 + j] == n:
                                return False
        return True
    
def solvee ():
        for y in range(9):
                for x in range(9):
                        if board[y][x] == 0:
                                for n in range(1, 10):
                                        if possible(y, x, n):
                                                board[y][x] = n
                                                solvee()
                                                board[y][x] = 0
                                                
                                return
        print("\n")
        print("solving...\nsudoku solved!")
        print(np.matrix(board))

#===========================Main=======================================

def solve(sdk):
    find = find_empty(sdk)
    if not find:
        return True
    else:
        row, col = find

    for i in range(1, 10):
        if valid(sdk, i, (row, col)):
            sdk[row][col] = i

            if solve(sdk):
                return True

            sdk[row][col] = 0

    return False

def valid(sdk, num, pos):
    # Check row
    for i in range(len(sdk[0])):
        if sdk[pos[0]][i] == num and pos[1] != i:
            return False

    # Check column
    for i in range(len(sdk)):
        if sdk[i][pos[1]] == num and pos[0] != i:
            return False

    # Check box
    box_x = pos[1] // 3
    box_y = pos[0] // 3

    for i in range(box_y * 3, box_y * 3 + 3):
        for j in range(box_x * 3, box_x * 3 + 3):
            if sdk[i][j] == num and (i,j) != pos:
                return False

    return True

def print_board(sdk):
    for i in range(len(sdk)):
        if i % 3 == 0 and i != 0:
            print("- - - - - - - - - - - - - ")

        for j in range(len(sdk[0])):
            if j % 3 == 0 and j != 0:
                print(" | ", end="")

            if j == 8:
                print(sdk[i][j])
            else:
                print(str(sdk[i][j]) + " ", end="")


def find_empty(sdk):
    for i in range(len(sdk)):
        for j in range(len(sdk[0])): 
            if sdk[i][j] == 0:
                return (i, j)  # row, col

    return None





