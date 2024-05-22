def removeDuplicates2(nums):
        """functino that removes duplicates in place such that 
        each unique element appears at most twice"""
        """
        :type nums: List[int]
        :rtype: int
        """
        k = 0
        for i in range(len(nums)):
            if nums.count(nums[i - k]) > 2:
                nums.remove(nums[i - k])
                k += 1
