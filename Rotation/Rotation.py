#!/usr/bin/python3
def solution(A, K):
    # Implement your solution here
    if A is None or A == []:
        return A
    num = 0
    for i in range(1, K + 1):
        num = A[-1]
        A = [num] + A[:-1]
    return A

print(solution([3, 8, 9, 7, 6], 3))