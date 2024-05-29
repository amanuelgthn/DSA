#!/usr/bin/env python3


compress1 = __import__('compressString').compress1

chars1 = ["a","b","b","b","b","b","b","b","b","b","b","b","b"]
chars2 = ["a","a","b","b","c","c","c"]
chars3 = ['a']

print(compress1(chars1))
print(compress1(chars2))
print(compress1(chars3))
