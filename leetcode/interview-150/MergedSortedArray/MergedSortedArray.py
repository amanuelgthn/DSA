#!/usr/bin/python3
"""Merge Sorted Array"""

def merge(nums1, m, nums2, n):
    """
    Initialize the solution
    nums1: first list, with a len of m + n
    nums2: second list, with a len of n
    m: length of nums to merged from nums1
    n: length of nums2
    """
    for i in range(n):
            nums1[m + i] = nums2[i]
    nums1.sort() # the list should be sorted in place 
                # if we use nums1= nums1[:m] nums2
                # the above means that we are createing a new list rather than doing an inplace list updating 
    return nums1
    