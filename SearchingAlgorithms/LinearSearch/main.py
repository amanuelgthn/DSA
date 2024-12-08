#!/usr/bin/python3
"""main.py"""

LinearSearch = __import__('LinearSearch').LinearSearch

# Define the array and target value
Array1 = [10, 20, 30, 40, 50, 60]
target = 30

# Perform the search
result = LinearSearch(Array1, target)

# Print the result
if result != -1:
    print(f"Target {target} found at index {result}.")
else:
    print(f"Target {target} not found in the array.")

