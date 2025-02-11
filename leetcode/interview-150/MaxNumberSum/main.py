#!/usr/bin/env python3

MaxNumberSum = __import__("MaxNumberSum").maxOperations
MaxNumberTwo = __import__("MaxNumberSum2pointer").TwoPointer

nums1 = [3,1,3,4,3]

nums2 = [1,2,3,4]

print(MaxNumberSum((nums1), 6))

print(MaxNumberSum((nums2), 5))

print("Two Pointers {}".format(MaxNumberTwo((nums1), 6)))

print("Two Pointers {}".format(MaxNumberTwo((nums2), 5)))