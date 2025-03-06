#!/usr/bin/env python3


def divide(a, b):
    try:
        result = a / b
    except ZeroDivisionError as e:
        print("Error {}".format(e))
        return None
    else:
        print("Division Successful")
        return result
    finally:
        print("Execution of the divide function is complete")




print(divide(10, 2))
print(divide(10, 0))