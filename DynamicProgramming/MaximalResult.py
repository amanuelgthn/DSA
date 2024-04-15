#!/usr/bin/python3
# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A):
    ##Initializing the solution game starts at the first squeare
    result = []
    result[0] = A[0]
    for i in range(1, len(A)):
        for j in range(max(0, i-6), i):
            result[i] = max(result[i], result[j]) + A[i]


    return result[-1]
    

print(solution([1, -2, 0, 9, -1, -2]))
