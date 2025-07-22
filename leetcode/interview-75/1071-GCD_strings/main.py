#!/usr/bin/python3
# NOTE THIS IS NOT THE REAL SOLUTION

def gcdOfStrings(str1: str, str2: str) -> str:
    answer = ""
    initial = str2 if len(str2) <= len(str1) else str1
    for i in range(len(initial)):
        if str1.count(initial[:i + 1]) > 0 and str2.count(initial[:i + 1]) > 0:
            answer = initial[:i+1]
    return answer



#testing
str1 = "ABCABC"
str2 = "ABC"
str3 = gcdOfStrings(str1, str2)

print("gcd of {} & {} is {}".format(str1, str2, str3))

### while this code works for some strings the operator count
# only returns the number of times that the substring appears in the
# larger string, for ABABAB and ABAB it returns 1
# The required answer should be 0 because ABAB is not the perfect divisor
#  