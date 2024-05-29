#!/usr/bin/env python3
"""
You are given a 0-indexed array of integers nums of length n. You are initially positioned at nums[0].

Each element nums[i] represents the maximum length of a forward jump from index i. In other words, if you are at nums[i], you can jump to any nums[i + j] where:

0 <= j <= nums[i] and
i + j < n
Return the minimum number of jumps to reach nums[n - 1]. The test cases are generated such that you can reach nums[n - 1].
"""

def jump(nums):
    count = 0
    num = 0
    left = right = 0
    while right < len(nums) - 1:
        num += 1
        print("calculating {}".format(num))
        farthest = 0
        for i in range(left, right + 1):
            print("innermost")
            farthest = max(farthest, i + nums[i])
        left = right + 1
        right = farthest
        count += 1
    return count 