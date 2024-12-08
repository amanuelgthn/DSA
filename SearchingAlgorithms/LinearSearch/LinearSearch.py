#!/bin/usr/python3
"""Linear Search Algorithm"""

def LinearSearch(Array: list, number: int):
    """function to return the index of the number being searched and 
    returns -1 if not found"""
    length = len(Array)
    for i in range(length):
        if number == Array[i]:
            return i
    return -1
