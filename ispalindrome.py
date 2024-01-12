#!/usr/bin/python3
"""check if a string is palindrome"""


def solution(inputString):
    length = len(inputString)
    for i in range(length):
        if inputString[i] == inputString[length - i - 1]:
            continue
        else:
            return False
    return True
