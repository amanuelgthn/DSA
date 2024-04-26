#!/usr/bin/env python3
def diagonalDifference(arr):
    # Write your code here
    sum1 = 0
    sum2 = 0
    length = len(arr)
    for i in range(length):
        for j in range(len(arr[i])):
            if i == j:
                print(arr[i][j])
                sum1 += arr[i][j]
                sum2 += arr[length-1 - i][j]
                
    return (abs(sum1 -sum2))


arra = [
       [11, 2, 4],
       [4, 5, 6],
       [10, 8, -12]]
print(diagonalDifference(arra))