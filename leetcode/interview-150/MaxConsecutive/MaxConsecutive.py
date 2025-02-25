#!/usr/bin/env python3

def longestOnes(nums, k):
    """
    :type nums: List[int]
    :type k: int
    :rtype: int
    """
    i = j = 0
    length = len(nums)
    while j < length:
        if nums[j] == 0:
            k -=1
        j += 1
        if k < 0:
            if nums[i] == 0:
                k += 1
            i += 1    
    return j - i