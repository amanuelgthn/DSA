#!/usr/bin/env python3
from typing import List

def productExceptSelf(nums: List[int]) -> List[int]:
    n = len(nums)
    result = [1] * n
    #calculating the product to the left side of the number at it's place
    left_product = 1
    for i in range(n):
        result[i] *= left_product
        left_product *= nums[i]
    #calcuuulatingn the produuct to the righht side of thhe nnuuummber at it's place
    #annd takinng the commmuulative
    right_product = 1
    for i in range(n - 1, -1, -1):
        result[i] *= right_product
        right_product *= nums[i]
    return result



if __name__ == "__main__":
    nums1 = [1,2,3,4]
    nums2 = [-1,1,0,-3,3]
    nums3 = [5,0,4,2,6,7,3]
    print("{}\nProduct {}".format(nums1,productExceptSelf(nums1)))
    print("{}\nProduct {}".format(nums2,productExceptSelf(nums2)))
    print("{}\nProduct {}".format(nums3,productExceptSelf(nums3)))