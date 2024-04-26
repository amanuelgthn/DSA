#!/usr/bin/env python3
"""Time conversion"""


#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'timeConversion' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def timeConversion(s):
    # Write your code here
    timeformat = re.findall(r'[a-zA-Z]', s)
    timeformat = "".join(timeformat)
    time = re.findall(r'[0-9]+', s)
    num = 0
    if timeformat == "PM":
        if time[0] != '12':
            num = int(time[0])
            num += 12
            time[0] = str(num)
        return ":".join(time)
    if timeformat == "AM":
        if time[0] == '12':
            time[0] = '00'
        return ":".join(time)

print(timeConversion('12:40:22AM'))