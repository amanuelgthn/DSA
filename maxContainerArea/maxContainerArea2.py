#!/usr/bin/python3
"""max area of water in container O(n) solution"""
from typing import List


def maxArea(height: List[int]) -> int:
    """
    :type height: List[int]
    :rtype: int
    """
    area = 0
    left = 0
    right = len(height) - 1

    while left < right:
        num1 = height[left]
        num2 = height[right]
        num = num1 if num1 < num2 else num2
        print("num1:{} num2:{} num:{}".format(num1, num2, num))
        temparea = num * (right - left)
        if area < temparea:
            area = temparea
        if num1 > num2:
            right -= 1
        else:
            left += 1
    return area
