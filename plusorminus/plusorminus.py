#!/usr/bin/env python3
"""Plusorminus"""


#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'plusMinus' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def plusMinus(arr):
    # Write your code here
    length = len(arr)
    pos = 0
    neg = 0
    zer = 0
    for i in arr:
        if i > 0:
            pos += 1
        if i == 0:
            zer += 1
        if i < 0:
            neg += 1
    print("{:.6f}".format(pos/length))
    print("{:.6f}".format(neg/length))
    print("{:.6f}".format(zer/length))

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
