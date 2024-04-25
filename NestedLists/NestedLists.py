#!/usr/bin/env python3


if __name__ == '__main__':
    records = []
    scores = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        pair = []
        pair.append(name)
        pair.append(score)
        records.append(pair)
        scores.append(score)
    scores = list(sorted(scores, reverse=True))
    print(scores)
    lowest = min(scores)
    secondLowest = scores[-2]
    if lowest == secondLowest:
        for value in scores:
            if value > lowest:
                secondLowest = value
    result = []
    for pairs in records:
        if secondLowest in pairs:
            result.append(pairs[0])
    result = sorted(result, reverse=False)
    for name in result:
        print("res: {}".format(name))
