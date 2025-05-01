#!/usr/bin/env python3


def find_second_largest(nums):
    if len(nums) < 2:
        return None  # Edge case: too few elements
    
    unique = sorted(set(nums))  # Remove duplicates and sort
    return unique[-2] if len(unique) >= 2 else nums[0]




lst = [45,5,5,26,45,44, 89]

print(find_second_largest(lst))