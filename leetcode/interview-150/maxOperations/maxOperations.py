#!/usr/bin/env python3


def maxOperations(nums, k):
    """
    :type nums: List[int]
    :type k: int
    :rtype: int
    """
    """inefficient but logically correct solution"""
    nums.sort()
    print(nums, k)
    count = 0
    i = 0
    counted = []
    right = len(nums)- 1
    while i < right:
        sum = nums[i] + nums[right]
        if sum == k and i < right and right not in counted:
            print("sum == k i {} right {}".format(i, right))
            count += 1
            i += 1
            counted.append(right)
            right -= 1
            
        else:
            right -=1
            print("i {} right {}".format(i, right))
        if i == right:
            right = len(nums) - 1
            i += 1
    return count
