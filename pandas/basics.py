#!/usr/bin/env python3

import pandas as pd
import numpy as np


#creating empty series

ser = pd.Series()
print("Pandas Series: ", ser)

data = np.array(['g', 'e', 'a','d', 'y'])

ser = pd.Series(data)
print("Pandas Series:\n", ser)
