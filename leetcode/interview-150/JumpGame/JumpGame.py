#!/usr/bin/env python3
"""
program to return true if it can reach the last index
or flase if it can not
"""

def canJump(nums):
    jumped = 0
    for i in range(len(nums)):
        if i > jumped:
            return False
        jumped = max(jumped, nums[i] + i) 
        if jumped >= len(nums) - 1:
            return True
    return False