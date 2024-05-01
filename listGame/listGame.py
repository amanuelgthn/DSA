#!/usr/bin/env python3
"""List game"""

if __name__ == '__main__':
    N = int(input())
    result = []
    for i in range(12):
        line = input()
        line = line.split()
        if line[0] == 'insert':
            if len(result) < int(line[1]) + 1:
                result.append(line[2])
            result[int(line[1])] = line[2]
        elif line[0] == 'append':
            result.append(line[1])
        elif line[0] == 'remove':
            result.remove(line[1])
        elif line[0] == 'print':
            print(result)