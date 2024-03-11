#!/usr/bin/python3
"""Merge Sorted Array"""

class Solution:
    """Solution class to solve a """
    def merge(self, nums1, m, nums2, n):
        """
        Initialize the solution
        nums1: first list, with a len of m + n
        nums2: second list, with a len of n
        m: length of nums to merged from nums1
        n: length of nums2
        """
        self.nums1 = nums1
        self.nums2 = nums2
        self.m = m
        self.n = n

    def merge(nums1, m, nums2, n):
        """
        method to merge a two lists with sorted in an increasing order
        """
        for i in range(n):
            if nums1[m + i] >= nums2[i]:
                nums1[m + i] = nums2[i]
            nums1.sort()

            #Alternative solutoin on development
            # else:
            #     for j in range(1, n):
            #         if nums1(m - j + i) >= nums2(i):
            #             nums1[m - j + i + 1] = nums1(m + i)
            #             nums1[m - j + i ] = nums2(i)
