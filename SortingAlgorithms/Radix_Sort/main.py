#!/usr/bin/python3
"""main.py"""

RadixSort = __import__("RadixSort").RadixSort

array1 = [234, 3, 6, 1, 90, 45, 23, 11]
array2 = [1,2,3,4,5,6,7,8,9]
array3 = [1, 2, 3, 4, 5, 6, 2, 7]
RadixSort(array1)
RadixSort(array2)
RadixSort(array3)