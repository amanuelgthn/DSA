#!/usr/bin/env python3

import numpy as np

my_arry = np.arange(10)
my_arry1 = np.arange(10)
my_arry2 = np.arange(10)

print(my_arry * 4)
print(my_arry)

simple_array = np.array([my_arry,
                         my_arry1,
                         my_arry2])

print(" simple array \n {}".format(simple_array))
print("Shape of array: {}".format(simple_array.shape))
print("Rank of the array is {}".format(simple_array.ndim))
print("the type of the array is {}".format(simple_array.dtype))