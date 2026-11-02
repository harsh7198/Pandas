import numpy as np 
import pandas as pd 

data = pd.Series([10,30,40,50,60,70], name="Data")
# give index
print(data.index)
#give actual data 
print(data.values)
# print data type
print(data.dtype)
# print size
print(data.size)
# print shape 
print(data.shape)
# print number of dimensions
print(data.ndim)
# print Series name
print(data.name)