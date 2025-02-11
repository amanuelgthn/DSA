#!/usr/bin/env python3


def TwoPointer(nums, k):
    count = 0
    right = len(nums)- 1
    for i in range(len(nums)-1):
        if nums[i] + nums[right] == k and i < right:
            count += 1
            i += 1
            right -= 1
    return count
