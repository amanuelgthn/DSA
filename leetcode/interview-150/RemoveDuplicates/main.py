#!/usr/bin/env python3

RemoveDuplicates = __import__("RemoveDuplicates").removeDuplicates

nums = [0,0,1,1,1,2,2,3,3,4]
nums1 = [1,1,1,1]

print(RemoveDuplicates(nums))
print(RemoveDuplicates(nums1))