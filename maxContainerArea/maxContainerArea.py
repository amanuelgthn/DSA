#!/usr/bin/python3
"""max area of water in container O(n^2) solution"""


def maxArea(height):
    """
    :type height: List[int]
    :rtype: int
    """
    area = 0
    for i in range(len(height)):
        num1 = height[i]
        for j in range(i + 1, len(height)):
            temparea = 0
            num2 = height[j]
            temparea = min(num2 * (j - i), num1 * (j - i))
            if area < temparea:
                area = temparea
    return area
