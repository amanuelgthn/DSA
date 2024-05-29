#!/usr/bin/env python3

check = __import__('CheckAllNumbers').Solution

matrix1 = [[1, 2, 3],
           [1, 2, 3],
           [1, 2, 3]]
matrix2 = [[1, 3, 2],
           [3, 2, 1],
           [1, 2, 3]]
matrix3 = [[1, 2, 6, 5],
           [3, 4 , 6, 3],
           [3, 4 , 6, 3],
           [3, 4 , 6, 3]]
matrix4 = [[1, 3, 2],
           [3, 2, 1],]

print(check(matrix1))
print(check(matrix2))
print(check(matrix3))
print(check(matrix4))