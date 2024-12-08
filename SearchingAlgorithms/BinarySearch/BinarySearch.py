#!/bin/usr/python3
"""Binary Search"""

def BinarySearch(Array: list, target: int) -> int:
    low = 0
    high = len(Array) - 1
    while low <= high:
        mid = (low + high) // 2
        print(mid)
        if Array[mid] > target:
            high = mid - 1
        elif Array[mid] < target:
            low =  mid + 1
        else:
            return  mid
    return -1