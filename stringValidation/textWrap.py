#!/usr/bin/env python3
"""string: a single string with newline characters ('\n') where the breaks should be"""


import textwrap


def wrap(string, max_width):
    # without using impor textwrap
    # count = 0
    # str1 = ''
    # for i in string:
    #     if count == max_width:
    #         count = 0
    #         str1 += '\n'
    #     str1 += i
    #     count += 1
    # return str1
    
    # using the import textwrap
    return textwrap.fill(string, max_width)
            

if __name__ == '__main__':