#!/usr/bin/python3
# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A):
    # Implement your solution here
    max = 1
    for i in range(len(A)):
        for j in range(0, len(A) - 1):
            if(A[j] > A[j + 1]):
                A[j],A[j + 1] = A[j + 1],A[j] 
    for i in A:
        if i >= 1 and i == max:
            max += 1
        else:
            continue
    return max
