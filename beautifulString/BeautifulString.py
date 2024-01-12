#!/usr/bin/pythonn3
"""Beautiful String"""


def BeautifulString(inputString):
    stringArranged = {}
    index = 0
    asciiValues = list(range(97, 123, 1))
    for i in range(97, 123, 1):
        stringArranged[i] = 0
        for char in inputString:
            if ord(char) in stringArranged.keys() and ord(char) == i:
                stringArranged[ord(char)] += 1
        i += 1
    value = list(stringArranged.values())
    keys = list(stringArranged.keys())
    for i in range(len(keys)):
        for j in range(0, len(keys) - 1):
            if keys[j] > keys[j + 1]:
                keys[j],keys[j + 1] = keys[j + 1], keys[j]
            j += 1
        i += 1
    sortedArray = []
    for i in keys:
        sortedArray.append(stringArranged[i])
    for i in range(len(sortedArray)):
        for j in range(0, len(sortedArray) - 1):
            if sortedArray[j] < sortedArray[j + 1]:
                sortedArray[j],sortedArray[j + 1] = sortedArray[j + 1], sortedArray[j]
            j += 1
        i += 1
    if value == sortedArray:
        return True
    return False