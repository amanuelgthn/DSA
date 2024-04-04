#!/usr/bin/env python3
"""
minimum difference from the sume of subdivion of a list
"""


def solution(A):
    # Implement your solution here
    length = len(A)
    min = float('inf')
    left_sum = 0
    right_sum = sum(A)
    if length == 1:
        return A[0]
    if length == 2:
        return A[1] - A[0]
    for i in range(1, length - 1):
        left_sum += A[i - 1]
        right_sum -= A[i - 1]
        diff = abs(left_sum - right_sum)
        if diff < min:
            min = diff
        i += 1
    return int(min)

print(solution([0,1000]))