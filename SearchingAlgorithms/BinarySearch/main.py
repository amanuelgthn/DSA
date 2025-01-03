#!/usr/bin/python3
"""main.py"""


BinarySearch = __import__("BinarySearch").BinarySearch
BinarySearchRecursive = __import__("BinarySearchRecursive").BinarySearchRecursive
array1 = [1, 3, 5, 7, 9, 11, 13]
array2 = [100, 200, 300, 400, 500, 600, 700]
array3 = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50]

print(BinarySearch(array1, 11))
print(BinarySearch(array2, 400))
print(BinarySearch(array3, 65))

print(BinarySearchRecursive(array1, 11))
print(BinarySearchRecursive(array2, 400))
print(BinarySearchRecursive(array3, 65))