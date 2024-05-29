#!/usr/bin/env python3
"""Given an array of characters chars, compress it and return it's length"""

def compress1(chars):
    if len(chars):
        return len(chars)
    char = chars[0]
    count = index = i = 1
    chars1 = [chars[0]]
    while i < len(chars):
        if char == chars[i]:
            count += 1
        else:
            char = chars[i]
            if count > 1:
                for j in str(count):
                    chars1.append(j)
            chars1.append(chars[i])
            count = 1
        i += 1
    if count > 1:
        for j in str(count):
            chars1.append(j)
    chars[:] = chars1
    return 1