#!/usr/bin/python3
"""Insertion Sort"""

def InsertionSort(array: list) -> list:
    length = len(array)
    for i in range(1,length):
        temp = array[i]
        j = i
        while j > 0 and array[j -1] > temp:
            array[j] = array[j - 1]
            j -=1
            print(array)
        array[j] = temp