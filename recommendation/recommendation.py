#!/usr/bin/python3
"""
recommendation program
"""



import sys
i = 0
item_dict = {}
score = {}
pref_score = []
for line in sys.stdin:
  line = line.split("\n")[0]
  item = line.split(":")
  if item[1]:
    item_dict[item[0]] = []
    item_dict[item[0]].append(item[1])
    if i == 0:
      base = item[0]
      length = len(item[1])
      j = 1
      count = 0
      for word in item[1].split(","):
        score[word] = j
        j += 1
    else:
      sum = 0
      weight = len(item[1].split(","))
      for word in item[1].split(","):
        sum += score[word] * weight
        weight -= 1
      item_dict[item[0]].append(sum)
      pref_score.append(sum)
    i += 1
result = []
for i in pref_score:
  for key, value in item_dict.items():
    if i == value[-1]:
      result.append(key)
length = len(result)
for i in result:
  if count != length - 1:
    print(i, end=",")
  else:
    print(i, end="")
  count += 1
