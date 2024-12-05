#!/usr/bin/python3
"""MergeSort"""

def MergeSort(Array: list) -> list:
    length = len(Array)
    if length < 2:
        return
    mid = length // 2
    arr1 = Array[0:mid]
    arr2 = Array[mid: length]
    MergeSort(arr1)
    MergeSort(arr2)
    Merge(Array, arr1, arr2)
    print('Final Array {}'.format(Array))
def Merge(Array, arr1, arr2):
    i = j = 0
    while i + j < len(Array):
        if j == len(arr2) or (i < len(arr1) and arr1[i] < arr2[j]):
            Array[i + j] = arr1[i]
            i += 1
            print(Array)
        else:
            Array[i + j] = arr2[j]
            j += 1
            print(Array)