#!/usr/bin/python3
"""main function to test the AreaPolygon.py"""


AreaPolygon = __import__('AreaPolygon').AreaPolygon


print('Area of n = {} is {}'.format(2, AreaPolygon(2)))
print('Area of n = {} is {}'.format(4, AreaPolygon(4)))
print('Area of n = {} is {}'.format(3, AreaPolygon(3)))
print('Area of n = {} is {}'.format(5, AreaPolygon(5)))
print('Area of n = {} is {}'.format(6, AreaPolygon(6)))
