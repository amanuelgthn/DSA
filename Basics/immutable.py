#!/usr/bin/env python3

def modify_number(n):
    # Reassign n to a new value; this creates a new object locally
    n = n + 10
    print("Inside function:", n)

# Create an immutable integer
x = 5
modify_number(x)
print("Outside function:", x)  # Output: 5


result = [i for i in range(5) if i % 2 == 0]

print("result is {}".format(result))