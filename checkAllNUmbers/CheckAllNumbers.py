#!/usr/bin/env python3
"""an nxn matrix is valid if every row and every column contains 
all the integers from 1 to n (inclusive)"""


def Solution(matrix):
    """returns true if the matrix is valid and false otherwise"""
    n = len(matrix[0])
    length = 0
    for i in matrix:
        i = sorted(i)
        print(i)
        counter = 1
        length += 1
        for j in i:
            if j != counter:
                return False
            counter += 1
    return length == n