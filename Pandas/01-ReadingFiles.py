'''Pandas is an open-source Python library specifically designed for data analysis and manipulation.
Data Analysis is the process of extracting meaningful insights, trends and patterns from the data to solve the problems

Data Manipulation is the changing, organizing, and preparing the data to make it useful and easier to understand.

Why Do We Use It?
Before Pandas, Python wasn't great for data analysis. Developers had to use complex lists and dictionaries to handle rows and columns, which was slow and tedious.

We use Pandas because it introduces the DataFrame—which is essentially an Excel spreadsheet inside your Python environment.

A DataFrame is a two-dimensional, spreadsheet-like data structure in Pandas that organizes data into rows and columns. It is the primary tool used in Python for storing, filtering, and manipulating tabular data efficiently.

Here is what makes it so popular:

Handles Massive Data: It can easily load, clean, and analyze millions of rows that would cause Microsoft Excel to crash.

Data Cleaning Made Easy: It has built-in tools to handle missing data (NaN values), fix formatting errors, and filter out noise.

Reads Almost Anything: You can pull data into Pandas from CSV files, Excel sheets, SQL databases, JSON files, and even webpage URLs with just one line of code.

Speed: Because it's built on NumPy (which is written in C), it executes complex data operations incredibly fast.'''


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

#Read from database

from sqlalchemy import create_engine
import pandas as pd

# 1. Create the MySQL connection string
# Format: mysql+pymysql://user:password@host:port/database_name
engine = create_engine('mysql+pymysql://root:MYSQL123@localhost:3306/btd_platform')
# 2. Run your query and load it straight into a DataFrame
df = pd.read_sql("select * from users", con=engine)
print(f"Database users table:\n{df}")