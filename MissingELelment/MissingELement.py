#!/usr/bin/env python3
"""Finging the missing elemnt in an array"""


def solution(A):
    """ function that reutrn s the value of the missing
    elemnt in an array"""
    if A == []:
        return 1
    A = sorted(A)
    print(A)
    count = 1
    for i in A:
        if i != count:
            return count
        count += 1
    return count

print(solution([1,2,6,4,3]))