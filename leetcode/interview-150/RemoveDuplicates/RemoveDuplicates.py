#!/usr/bin/env python3
def removeDuplicates(nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        first = 0
        for i in range(1, len(nums)):
                if nums[i] !=  nums[first]:
                        first += 1
                        nums[first] = nums[i]
                        
        return nums[:first + 1]
        # print(nums)
        # k = 0
        # for i in range(len(nums)):
        #     if nums.count(nums[i - k]) > 1:
        #         print("i - k {} count {} nums {}".format(nums[i - k], nums.count(nums[i - k]), nums))
        #         nums.remove(nums[i - k])
        #         k += 1
        # return nums



    # def removeDuplicates(nums):
    #     """
    #     :type nums: List[int]
    #     :rtype: int
    #     """
    #     k = 0
    #     for i in range(len(nums)):
    #         num = nums[i - k]
    #         if i - k + 1 < len(nums):
    #             if num == nums[i  - k + 1]:
    #                 nums.pop(num)
    #                 k += 1

    # num = nums[i - k]
    #         j = i - k + 1
    #         if num in nums[j:]:
    #             nums.remove(num)
    #             k += 1
    #     return len(nums)