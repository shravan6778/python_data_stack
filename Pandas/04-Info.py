import pandas as pd
# About info() method
# 1.Displays number of rows and columns
# 2.Columns name
# 3.Which type of data is stored
# 4.non null counts
# 5.memory usage of the dataframe

df_csv = pd.read_csv("sales_data_sample.csv", encoding="latin1")
print("CSV File:")
print(df_csv.info())

df_xlxs=pd.read_excel("SampleSuperstore.xlsx")
print("Excel File:")
print(df_xlxs.info())


df_json=pd.read_json("sample_Data.json")
print("JSON File:")
print(df_json.info())
