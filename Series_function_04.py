import numpy as np 
import pandas as pd 

s = pd.Series([10, 20, 30, 40, 50])

print(s.sum())       # Total
print(s.mean())      # Average
print(s.median())    # Median
print(s.max())       # Maximum
print(s.min())       # Minimum
print(s.count())     # Non-missing values
print(s.describe())  # Statistical summary