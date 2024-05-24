#!/usr/bin/env python3
"""
return the minumum number of candies needed to have to distribute to tthe children

"""


def candy(ratings):
    """
    :type ratings: List[int]
    :rtype: int
    """
    candies = [1] * len(ratings)

    for i in range(1, len(ratings)):
        if ratings[i] > ratings[i - 1]:
            candies[i] = candies[i - 1] + 1
    for i in range(len(ratings) - 2, -1, -1):
        if ratings[i] > ratings[i + 1]:
            candies[i] = max(candies[i], candies[i + 1] + 1)
    return sum(candies)


