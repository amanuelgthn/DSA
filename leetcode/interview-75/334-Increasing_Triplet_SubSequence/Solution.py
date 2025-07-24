#!/usr/bin/python3

from typing import List


def increasingTriplet(nums: List[int]) -> bool:
    first = second = float('inf')
    for num in nums:
        if num < first:
            first = num
        elif num < second:
            second = num
        else:
            return True
    return False