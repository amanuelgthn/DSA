#!/usr/bin/env python3


def maxVowels(s, k):
    """
    :type s: str
    :type k: int
    :rtype: int
    """

    max = 0
    vowels = [ 'a', 'e', 'i', 'o', 'u']
    current = s[:k]
    init = 0
    for i in current:
        if i in vowels:
            init += 1
    print("init {}".format(init))
    length = len(s)
    for i in range(length):
        print("current", init, "i", i)
        if i > 0 and i + k - 1< length:
            print("char", s[i - 1])
            if s[i - 1] in vowels:
                print("prev", s[i - 1])
                init -= 1
            if s[i + k - 1] in vowels:
                print("current", s[i + k - 1])
                print(s[i + k - 1])
                init += 1
        print(init)
        if init > max:
            max = init
    return max

