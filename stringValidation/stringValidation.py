#!/usr/bin/env python3
"""string Validation """

def stringValidation(String):
    str = list(String)
    result = [False] * 5
    for i in str:
        if i.isalnum():
            result[0] = True
        if i.isalpha():
            result[1] = True
        if i.isdigit():
            result[2] = True
        if i.islower():
            result[3] = True
        if i.isupper():
            result[4] = True
    for i in result:
        print('{}'.format(i), end='\n')