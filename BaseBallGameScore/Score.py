#!/usr/bin/env python3


def calPoints(ops) -> int:
    """
    :type ops: List[str] - List of operations
    :rtype: int - Sum of scores after performing all operations
    """
    # print((ops))
    result = None
    solution = []
    n = 0
    for i in ops:
        n += 1
    for i in range(n):
        if ops[i] == "C":
            solution.pop()
        elif ops[i] == "D":
            solution.append(2 * int(solution[- 1]))
        elif ops[i] == "+":
            solution.append(int(solution[- 1]) + int(solution[- 2]))
        else:
            solution.append(int(ops[i]))
    result = sum(solution)
    # print(solution)
    return result

if __name__ == '__main__':
    line = input()
    ops = line.strip().split()

    print(calPoints(ops))