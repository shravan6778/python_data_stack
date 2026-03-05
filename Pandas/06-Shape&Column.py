import pandas as pd

"""
1.How big is our dataset is ?
Shape is an attribute that returns number of rows & columns in a tuple 
2.What are the names of Column ?
Column is also an attribute where it returns the names of each column of a dataset
"""

df_csv = pd.read_csv("sales_data_sample.csv", encoding="latin1")
print(f"Shape : {df_csv.shape}")
print(f"Column Names : {df_csv.columns}")

# To display single Column
print("display single Column")
print(df_csv['ORDERNUMBER'])
print("display multiple Columns")
print(df_csv[['ORDERNUMBER','QUANTITYORDERED']])