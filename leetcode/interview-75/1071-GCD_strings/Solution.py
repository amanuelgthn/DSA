#!/usr/bin/python3

def gcdOfStrings(str1: str, str2: str) -> str:
    #placeholder for the result 
    answer = ""

    #ensuring str1 is always the shorter str
    if len(str2) < len(str1):
        str1, str2 = str2, str1
    
    for partition in range(1, len(str1) + 1):
        #checking firsthand if the substring divides the strings in the argument
        if len(str1) % partition or len(str2) % partition:
            continue

        candidate = str1[:partition]
        if candidate * (len(str1) // partition) == str1 and candidate * (len(str2) // partition):
            answer = candidate
    return answer
    