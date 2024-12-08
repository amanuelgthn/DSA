#!/bin/usr/python3
"""Radix Sort"""

def RadixSort(arr):
    #find the maximum number to know number of digits required to sort
    maximum = max(arr)
    digit = 1
    while maximum / digit > 1:
        radixsort(arr, digit)
        digit *= 10
    print(arr)
def radixsort(arr, digit):
    n = len(arr)
    Output = [0] * n # creating a list to hold final sorted array
    count = [0] * 10 # creating a list to store information about position of the numbers according to the digits
    for i in range(n):
        index = arr[i] // digit
        count[index % 10] += 1
    for i in range(1, 10):
        count[i] += count[i -1]
    i = n - 1
    while i >= 0:
        index = arr[i] // digit
        Output[count[index % 10] - 1] = arr[i]
        count[index % 10] -=1
        i -= 1
    for i in range(n):
        arr[i] = Output[i]