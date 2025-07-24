#!/usr/bin/python3

increasingTriplet = __import__('Solution').increasingTriplet

nums1 = [1, 2, 3, 4, 5]
answer1 = True
nums2 = [5, 4, 3, 2, 1]
answer2 = False

print(increasingTriplet(nums1), answer1)
print(increasingTriplet(nums2), answer2)