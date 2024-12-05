#!/usr/bin/python3
"BubbleSort"

def BubbleSort(array: list) -> list:
    length = len(array)
    for i in range(length - 1):
        Swapped = False
        for j in range(length - 1):
            if(array[j+1]<= array[j]):
                array[j],array[j+1] = array[j+1],array[j]
                print(array)
                Swapped = True
        if Swapped == False:
            break
    print(array)