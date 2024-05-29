#!/usr/bin/env python3
"""Given an integer array flowerbed containing 0's and 1's, where 0 means empty and 1 means not empty, and an integer n, return true if n new flowers can be planted in the flowerbed without violating the no-adjacent-flowers rule and false otherwise."""

def canPlaceFlowers(flowerbed, n):
        """
        :type flowerbed: List[int]
        :type n: int
        :rtype: bool
        """
        Planted = False
        for i in range(len(flowerbed)):
            if flowerbed[i] == 1:
                Planted = True
            elif flowerbed[i] == 0 and Planted:
                Planted = False
            elif flowerbed[i] == 0 and not Planted and (i + 1 < len(flowerbed) and flowerbed[i + 1] == 0 or i == len(flowerbed) - 1):
                n -= 1
                if n < 1:
                    break
                Planted = True
        return n < 1
