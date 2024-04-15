#!/usr/bin/python3
# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(N):
    # Implement your solution here
    num = DecimalToBinary(N)
    Start = False
    solution = [0]
    count = 0
    for i in num:
        print(i)
        if i == '1' and Start == False:
            Start = True
            # print("starting")
        elif Start == True and i == '0':
            # print("here")
            count += 1
        elif Start == True and i == '1':
            # print("there")
            solution.append(count)
            count = 0
    return max(solution)

    
def DecimalToBinary(num):
        if num > 1:
            # Recursively call the function and concatenate the result.
            return DecimalToBinary(num // 2) + str(num % 2)
        return str(num % 2)


print("328", DecimalToBinary(328), solution(328))