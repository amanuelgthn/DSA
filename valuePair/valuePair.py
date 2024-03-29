#!/usr/bin/python3

def solution(A):
    # Implement your solution here
    repeated = []
    for i in A:
        if i not in repeated:
            repeated.append(i)
        elif(i in repeated):
            repeated.remove(i)
    return(repeated[0])
