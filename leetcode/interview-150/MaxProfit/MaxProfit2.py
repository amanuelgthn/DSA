#!/usr/bin/env python3
def MaxProfit(prices):
    """returns the maximum profit it can be achieved from
    a give prices list where decision hast to be made to sell
    and buy each day"""
    profit = 0
    for i in range(1, len(prices)):
        if prices[i] > prices[i - 1]:
            profit += prices[i] - prices[i - 1]
    return profit