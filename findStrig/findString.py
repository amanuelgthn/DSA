#!/usr/bin/env python3
"""Output the integer number indicating the total number of occurrences of the substring in the original string."""

def count_substring(string, subString):
    count = 0
    check = False
    
    str1 = list(string)
    str2 = list(subString)
    for i in range(len(str1)):
        n = len(subString)
        for j in range(0, len(str2)):
            if i + j < len(str1):
                if str2[j] == str1[i + j]:
                    n -= 1
                    if n == 0:
                        check = True
                else:
                    check = False
                    break
        if check:
            count += 1
            check = False
    return count
