#!/usr/bin/env python3

def stringencoding(string: str) -> str:
    coded = {}
    result = ""
    for char in string:
        if char in coded.keys():
            coded[char] += 1
        else:
            coded[char] = 1
    for key, value in coded.items():
        kv = key + str(value)
        result += "".join(kv)
    return result




if __name__ == "__main__":
    string1 = "aabbaacndmnm"
    print(stringencoding(string1))
    