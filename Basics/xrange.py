#!/usr/bin/env python3

# obj = object()
# obj.x = 10

my_list = [0,23,4,2,234,5,667]
my_list.sort(reverse=False)

print(reversed(my_list))
count = 0
for i in reversed(my_list):
    count += 1
    print("number {} {} ".format(count,i), end="\n")