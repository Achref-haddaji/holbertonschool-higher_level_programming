#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    elements = len(matrix)
    lines = len(matrix[0])
    for i in range(elements):
        j = 0
        for j in range(lines):
            print("{:d}".format(matrix[i][j]), end='')
            if j < (lines - 1):
                print(" ", end='')
        print()
