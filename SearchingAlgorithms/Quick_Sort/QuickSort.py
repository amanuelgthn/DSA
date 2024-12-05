#!/usr/bin/python3
"""Quick Sort"""


def QuickSort(array):
    left = 0
    right = len(array) - 1
    quicksort(array, left, right)
    print('Final sorted array {}'.format(array))
def quicksort(arr, left, right):
    index = partition(arr, left, right)
    if left < index -1:
        quicksort(arr, left, index -1)
    if index < right:
        quicksort(arr, index, right)

def partition(arr, left, right):
    pivot = arr[(left + right) // 2]
    while left <= right:
        while arr[left] < pivot:
            left += 1
        while arr[right] > pivot:
            right -= 1
        if left <= right:
            arr[left], arr[right] = arr[right], arr[left]
            left += 1
            right -= 1
            print('swapped {}'.format(arr))
    print('Final {}'.format(arr))
    return left