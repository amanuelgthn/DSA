#!/usr/bin/env python3


def maxOperations(nums, k):
    """
    :type nums: List[int]
    :type k: int
    :rtype: int
    """
    length = len(nums)
    count = 0
    counted = []
    for i in range(length):
        if i not in counted:
            for j in range(i, length - 1):
                if j + 1 and i not in counted:
                    if nums[i] + nums[j + 1] == k:
                        count += 1
                        counted.append(i)
                        counted.append(j + 1)
    return count