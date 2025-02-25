#!/usr/bin/env python3

longestOnes = __import__("MaxConsecutive").longestOnes

nums1 = [1,1,1,0,0,0,1,1,1,1,0]

nums2 = [0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1]

print(longestOnes(nums1, 2))
print(longestOnes(nums2, 3))