#!/usr/bin/env python3

from typing import List

def moveZeroes(nums: List[int]) -> None:
    """
    Do not return anything, modify nums in-place instead.
    """
    length = len(nums)
    zero = 0
    non_zero = 1
    while non_zero < length and zero < length:
        if nums[zero] == 0:
            if nums[non_zero] != 0:
                nums[zero], nums[non_zero] = nums[non_zero], nums[zero]
            else:
                non_zero += 1
        elif nums[zero] != 0:
            zero += 1
            if zero >= non_zero:
                non_zero += 1


if __name__ == "__main__":
    nums = [4,2,4,0,0,3,0,5,1,0]
    exected = [4,2,4,3,5,1,0,0,0,0]
    moveZeroes(nums)
    print(nums)