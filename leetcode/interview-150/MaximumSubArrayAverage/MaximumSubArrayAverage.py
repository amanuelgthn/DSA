#!/usr/bin/env python3

def findMaxAverage(nums: list, k: int)-> float:
    """
    :type nums: List[int]
    :type k: int
    :rtype: float
    """
    tot = 0.00000
    avg = 0.00000
    Maxavg = float("-inf")
    length = len(nums)
    tot = sum(nums[:k])
    print(tot)
    for i in range(length):
        print(nums[i:k+i])
        print(len(nums[i:k+i]))
        if i + k <= length:
            if i > 0:
                print("before {}".format(tot))
                print(nums[i], nums[i - 1], nums[k + i - 1])
                tot = tot - nums[i - 1] + nums[k + i - 1]
                print("After {}".format(tot))
            avg = float(tot / (k * 1.00000))
            print(avg)
            if avg > Maxavg:
                Maxavg = avg
            print(Maxavg)
    return Maxavg
        
        