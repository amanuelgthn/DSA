#!/usr/bin/env python3
"""return a merged string of two given strings"""

def mergeAlternately(word1, word2):
    """
    :type word1: str
    :type word2: str
    :rtype: str
    """
    alternate = False
    merged = ''
    len1 = len(word1)
    len2 = len(word2)
    w1 = w2 = 0
    for i in range(len1 + len2):
        if alternate == False and w1 < len1 or w2 == len2:
            merged += word1[w1]
            w1 += 1
        elif alternate == True and w2 < len2 or w1 == len1:
            merged += word2[w2]
            w2 += 1
        alternate = not alternate
    return merged