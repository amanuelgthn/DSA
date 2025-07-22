#!/usr/bin/python3


from typing import List


def kidsWithCandies(candies: List[int], extraCandies: int) -> List[bool]:
    result = [False] * len(candies)
    for i in range(len(candies)):
        candies[i] = candies[i] + extraCandies
        if max(candies) <= candies[i]:
            result[i] = True
            candies[i] = candies[i] - extraCandies
    return result
            