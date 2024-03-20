#!/usr/bin/python3
"""main function to test the baseball_gamescore.py"""


calPoints = __import__('baseball_gamescore').calPoints

list1 = [5, 2, "C", "D", "+"]
print("list1", list1, calPoints(list1))
list2 = [5, -2, 4, "C", "D", 9, "+", "+"]
print("list2",list2, calPoints(list2))
