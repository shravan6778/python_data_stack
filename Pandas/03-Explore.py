# 1.Explore the dataset to understand the data
# 2.Identify the problems in the dataset
# 3.Then Plan the dataset

import pandas as pd

df=pd.read_csv("sales_data_sample.csv", encoding="latin1")

print("Display first 10 rows from the dataset:")
#head(n) displays n number of starting rows, if n is not given then it will return first 5 rows 
print(df.head(10))
#tail(n) displays n number of last rows, if n is not given then it will return last 5 rows 
print("Display last 10 rows from the dataset:")
print(df.tail(10))