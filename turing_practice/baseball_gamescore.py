#!/usr/bin/python3
"""program to calculate baseball points from given list"""



def calPoints(ops) -> int:
    """
    function to calculate baseball points from given list
    :type ops: list[str] List of operations
    :rtype: int - Sum of scores after performing all Operations
    """
    result = None
    validated = []
    for i in range(0, len(ops)):
        try:
            if type(int(ops[i])) == int:
                validated.append(ops[i])
        except ValueError:
            pass
        if ((ops[i])) == "C":
            validated.pop()
        elif ops[i] == "D":
            validated.append(validated[-1] * 2)
        elif ops[i] == "+":
            validated.append(validated[-1] + validated[-2])
    result = sum(validated)
    return result
    