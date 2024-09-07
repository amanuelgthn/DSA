#!/usr/bin/python3


calPoints = __import__('sumGame').calPoints

line = input()
ops = line.strip().split()
print(calPoints(ops))
