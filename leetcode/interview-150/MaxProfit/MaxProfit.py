#!/usr/bin/env python3
"""return the maximum profit you can achieve from this transaction"""

def maxProfit(prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        profit = 0
        min = prices[0]
        for i in range(1, len(prices)):
                if min > prices[i]:
                        min = prices[i]
                else:
                        if profit < prices[i] - min:
                                profit = prices[i] - min
        return profit