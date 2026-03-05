import pandas as pd

df_employees = pd.DataFrame({
    "EmpID": [101, 102, 103, 104, 105],
    "Name": ["Amit", "Ravi", "Suresh", "Kiran", "Anjali"],
    "Age": [25, 28, 30, 27, 24],
    "Department": ["IT", "HR", "Finance", "IT", "HR"]
})

df_salary = pd.DataFrame({
    "EmpID": [103, 104, 105, 106, 107],
    "Salary": [50000, 55000, 48000, 60000, 62000],
    "PerformanceScore": [88, 90, 85, 92, 91]
})

print(df_employees)
print(df_salary)

#to merge 2 dataframes we use merge method 

df=pd.merge(df_employees, df_salary, on="EmpID", how="inner")

# pd.merge(df_employees, df_salary, on="EmpID", how="left")

# pd.merge(df_employees, df_salary, on="EmpID", how="right")

# pd.merge(df_employees, df_salary, on="EmpID", how="outer")

#pd.merge(df_employees, df_salary, on="EmpID", how="cross")

print(df)
