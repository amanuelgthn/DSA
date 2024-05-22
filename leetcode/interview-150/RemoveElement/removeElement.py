def removeElement(nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        index = [i for i in range(len(nums)) if nums[i] == val]
        perform = 0
        for i in index:
                ind = i - perform
                del nums[ind]
                perform += 1
        return nums