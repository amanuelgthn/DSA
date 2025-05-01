#!/usr/bin/env python3
#solution for if the question was to find the sum of minimum 
# any collective numbers in the array
from typing import List

def minSubArrayLen(target: int, nums: List[int]) -> int:
    if sum(nums) < target:
        return 0
    nums.sort(reverse = True)
    subtotal = 0
    count = 0
    for i in nums:
        subtotal += i
        count += 1
        if subtotal >= target:
            break
    return count

if __name__ == "__main__":
    nums1 = [2,3,1,2,4,3]
    target1 =  7
    nums2 = [1,4,4]
    target2 = 4
    nums3 = [1,1,1,1,1,1,1,1]
    target3 = 11
    nums4 = [12,28,83,4,25,26,25,2,25,25,25,12]
    target4 = 213
    print("{} \n {} \n {}".format(nums1, target1, minSubArrayLen(target1, nums1)))
    print("{} \n {} \n {}".format(nums2, target2, minSubArrayLen(target2, nums2)))
    print("{} \n {} \n {}".format(nums3, target3, minSubArrayLen(target3, nums3)))
    print("{} \n {} \n {}".format(nums4, target4, minSubArrayLen(target4, nums4)))
