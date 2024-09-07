#!/usr/bin/python3
def calPoints(ops) -> int:
    """
    :type ops: List[str] - List of operations
    :rtype: int - Sum of scores after performing all operations
    """
    ans = []
    length = len(ops)
    for i in range(length):
        if ops[i].isdigit():
            ans.append(int(ops[i]))
            print(ops[i])
        elif ops[i] == "C" and ans:
            ans.pop()
        elif ops[i] == "D" and ans:
            ans.append(ans[-1] * 2)
        elif ops[i] == "+" and len(ans) >= 2:
            ans.append(ans[-1] + ans[-2])

    result = sum(ans)
    return result

