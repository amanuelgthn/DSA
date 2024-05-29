#!/usr/bin/env python3

merge = __import__('MergedSortedArray').merge


list1 = [1, 2 ,3]
list2 = [2, 5, 6]

m = 3 
n = 3

print(merge(list1, 3, list2, 3))