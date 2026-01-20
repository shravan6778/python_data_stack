import pandas as pd
#read from CSV file
df_csv = pd.read_csv("sales_data_sample.csv", encoding="latin1")
print("CSV File:")
print(df_csv)

# Read from excel file
df_xlxs=pd.read_excel("SampleSuperstore.xlsx")
print("Excel File:")
print(df_xlxs)

# Read from json file
df_json=pd.read_json("sample_Data.json")
print("JSON File:")
print(df_json)