#!/usr/bin/env python3

candy = __import__('minCandy').candy

case1 = [1,0,2]
case2 =  [1,2,2]
case3 =  [1,0,2, 3, 4]
case4 = [1,3,2,2,1]
print(candy(case1))
print(candy(case2))
print(candy(case3))
print(candy(case4))