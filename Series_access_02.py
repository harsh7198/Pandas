import numpy as np 
import pandas as pd 

s = pd.Series(
    [85, 90, 75],
    index=["Amit", "Rahul", "Jay"]
)

print(s["Rahul"])

# access using position 

print(s.iloc[0]) # s.iloc[] : used to access position 
print(s.loc["Rahul"]) # access from labbelled 


# performing math's operation 
marks = pd.Series([50, 60, 70, 80])

print(marks + 10)
print(marks * 2)
print(marks / 10)