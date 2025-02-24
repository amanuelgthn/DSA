#!/usr/bin/env python3

def longestOnes(nums, k):
    """
    :type nums: List[int]
    :type k: int
    :rtype: int
    """

    max = 0
    flip = 0
    length = len(nums)
    for i in range(length):
        if nums[i] == 1:
            max += 1
        elif nums[i] == 0 and flip <= k:
            max += 1
            flip += 1
        elif nums[i] == 0:
            max == 0
    return max


    