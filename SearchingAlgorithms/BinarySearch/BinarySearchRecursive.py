#!/usr/bin/python3
"""Binary Search recursive approach"""


def BinarySearchRecursive(Array: list, target: int) -> int:
    low = 0
    high = len(Array) - 1
    return BinarySearch(Array, low, high, target)

def BinarySearch(Array: list, low: int, high: int, target: int) -> int:
    if low > high:
        return -1 
    mid = (low + high) // 2
    if Array[mid] < target:
        return BinarySearch(Array, mid + 1, high, target)
    elif Array[mid] > target:
        return BinarySearch(Array, low, mid - 1, target)
    else:
        return mid