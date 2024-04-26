#!/usr/bin/env python3
"""Comparision Soring"""

import math
import os
import random
import re
import sys

#
# Complete the 'countingSort' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY arr as parameter.
#

def countingSort(arr):
    # Write your code here
    result = [0] * 100
    print (result)
    for i in arr:
        result[i] += 1
    return result


arr = [1]
print(countingSort(arr))