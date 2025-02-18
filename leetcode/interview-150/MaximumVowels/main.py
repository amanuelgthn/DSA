#!/usr/bin/env python3

MaxVowels = __import__("MaximumVowels").maxVowels


s1 = "abciiidef"
s2 = "aeiou"
s3 = "leetcode"


print(MaxVowels(s1, 3))
print(MaxVowels(s2, 2))
print(MaxVowels(s3, 3))