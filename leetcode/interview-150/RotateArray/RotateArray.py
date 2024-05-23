#!/usr/bin/env python3
def rotate(nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        print(nums[:])
        k = k % len(nums)
        # if k is above n we need to avoid a possible unnecessary round reversing
        nums[:] = nums[-k:] + nums[:-k]
        return nums