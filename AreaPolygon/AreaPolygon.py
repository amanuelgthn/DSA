#!/usr/bin/python3
"""
function that return the area of a polygon as described in the
readme file
"""

def AreaPolygon(n):
    """
    functon that returns the area of a polygon n 
    """
    if n == 1:
        return 1
    if n == 2:
        return 5
    else:
        return(n + 2*(n - 1) + (n - 2) + AreaPolygon(n -1))