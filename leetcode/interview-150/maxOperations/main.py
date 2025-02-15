#!/usr/bin/env python3


maxOperations = __import__("maxOperations").maxOperations
maxOperationsbest = __import__("maxOperationsbest").maxOperationsbest

nums1 = [4,4,1,3,1,3,2,2,5,5,1,5,2,1,2,3,5,4]
nums2 = [3,1,3,4,3]
nums3 = [1,2,3,4]
nums4 = [2,2,2,3,1,1,4,1]


print("Expected = 2, Output = {}".format(maxOperations(nums1, 2)))
print("Expected = 2, Output = {}".format(maxOperations(nums3, 5)))
print("Expected = 1, Output = {}".format(maxOperations(nums2, 6)))
print("Expected = 2, Output = {}".format(maxOperations(nums4, 4)))

print("Best Expected = 2, Output = {}".format(maxOperationsbest(nums1, 2)))
print("Best Expected = 2, Output = {}".format(maxOperationsbest(nums3, 5)))
print("Best Expected = 1, Output = {}".format(maxOperationsbest(nums2, 6)))
print("Best Expected = 2, Output = {}".format(maxOperationsbest(nums4, 4)))