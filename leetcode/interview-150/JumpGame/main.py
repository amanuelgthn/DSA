#!/usr/bin/env python3
canJump = __import__('JumpGame').canJump
jump = __import__('JumpGame2').jump

case1 = [2,3,1,1,4]
case2 = [3,2,1,0,4]
case3 = [1,2,3]
case4 = [3,0,8,2,0,0,1]
case5 = [1]
case6 = [1,2,1,1,1]

print(canJump(case1))
print(canJump(case2))
print(canJump(case3))
print(canJump(case4))
print(jump(case1))
print(jump(case2))
print(jump(case3))
print(jump(case4))
print(jump(case5))
print(jump(case6))