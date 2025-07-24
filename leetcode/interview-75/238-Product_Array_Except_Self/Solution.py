#!/usr/bin/python3

def productExceptSelf(nums):
    result = []
    left_product = 1
    right_product = 1
    length = len(nums)
    result = [1] * length
    for i in range(length):
        result[i] *= right_product
        right_product *= nums[i]
    for i in range(length - 1, -1, -1):
        result[i] *= left_product
        left_product *= nums[i]
    return result
    