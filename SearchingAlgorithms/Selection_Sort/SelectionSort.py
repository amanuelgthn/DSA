#!/bin/usr/python3
"Selection Sort"


def SelectionSort(array: list)-> list:
    length = len(array)
    for i in range(length):
        min = i
        for j in range(i + 1, length-1):
            if array[j] < array[min]:
                min = j
                print(array[min], array[j])
        array[i],array[min] = array[min],array[i]
        print(array)