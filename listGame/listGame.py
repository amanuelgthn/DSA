#!/usr/bin/env python3
"""List game"""

if __name__ == '__main__':
    N = int(input())
    result = []
    for i in range(N):
        line = input()
        line = line.split()
        if line[0] == 'insert':
            result.insert(int(line[1]), int(line[2]))
        elif line[0] == 'append':
            result.append(int(line[1]))
        elif line[0] == 'remove':
            result.remove(int(line[1]))
        elif line[0] == 'print':
            print(result)
        elif line[0] == 'sort':
            result.sort()
        elif line[0] == 'pop':
            result.pop()
        elif line[0] == 'reverse':
            result = result[::-1]