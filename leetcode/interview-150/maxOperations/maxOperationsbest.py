#!/usr/bin/env python3


def maxOperationsbest(nums, k):
    """
    :type nums: List[int]
    :type k: int
    :rtype: int
    """
    """best solution"""
    nums.sort()
    print(nums, k)
    count = 0
    i = 0
    right = len(nums)- 1
    while i < right:
        sum = nums[i] + nums[right]
        if sum == k:
            print("sum == k i {} right {}".format(i, right))
            count += 1
            i += 1
            right -= 1   
        elif sum < k:
            i += 1
        else:
            right -= 1
    return count
