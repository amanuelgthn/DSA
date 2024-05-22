#!/usr/bin/python3
def majorityElement(nums):
        """function that returns the majority element in a list"""
        """
        :type nums: List[int]
        :rtype: int
        """
        hash = {}
        res = nums[0]
        for i in nums:
            if i not in hash.keys():
                hash[i] = nums.count(i)
                if hash[res] < hash[i]:
                    res = i
        return res
