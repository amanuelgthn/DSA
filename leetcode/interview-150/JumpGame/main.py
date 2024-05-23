#!/usr/bin/env python3
canJump = __import__('JumpGame').canJump

case1 = [2,3,1,1,4]
case2 = [3,2,1,0,4]
case3 = [1,2,3]
case4 = [3,0,8,2,0,0,1]

print(canJump(case1))
print(canJump(case2))
print(canJump(case3))
print(canJump(case4))