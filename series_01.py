import numpy as np 
import pandas as pd 

marks = [99,87,56,84,74,65]
# making a index table using pd.Series
S = pd.Series(marks)
print(S)

# using tuple also 
A = pd.Series((10,20,30,40))
print(A)
#using dictionary
data = {
    "marks" : 98,
    "name"  : "Rahul" ,
    "Mo"    : 6354248157 
}
print(pd.Series(data))

# custom indexing
Marks = [85, 90, 75]

s = pd.Series(
    Marks,
    index=["Amit", "Rahul", "Jay"]
)

print(s)