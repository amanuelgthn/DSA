#!/usr/bin/env python3
"""returns te largest string x such that it will divide given
str1 and str2"""

def gcdOfStrings(str1, str2):
        """
        :type str1: str
        :type str2: str
        :rtype: str
        """
        check = ''
        gcd = ''
        iter = 0
        for i in range(len(str1) + len(str2)):
            if iter < len(str1) and iter < len(str2) and str1[iter] == str2[iter]:
                check += str1[iter]
                iter += 1
                if str2 == check * (len(str2)/len(check)) and str1 == check * (len(str1)/len(check)):
                    gcd = check
            else:
                return gcd