"""
df["Column_name"].mean()
df["Column_name"].sum()
df["Column_name"].min()
df["Column_name"].max()
"""


import pandas as pd
employee_data = {
    "Name": [
        "Amit", "Ravi", "Suresh", "Kiran", "Anjali",
        "Pooja", "Rahul", "Sneha", "Vikram", "Neha",
        "Arjun", "Priya", "Manoj", "Divya", "Karthik",
        "Meena", "Nikhil", "Swathi", "Rohit", "Kavya",
        "Sanjay", "Ayesha", "Deepak", "Isha", "Varun",
        "Shreya", "Abhishek", "Ritika", "Harsha", "Nandini"
    ],
    
    "Age": [
        22, 25, 28, 30, 24,
        26, 29, 23, 31, 27,
        32, 24, 35, 28, 26,
        34, 29, 25, 33, 27,
        36, 26, 31, 23, 28,
        24, 30, 29, 35, 27
    ],
    
    "Salary": [
        30000, 35000, 42000, 50000, 38000,
        45000, 52000, 34000, 60000, 48000,
        65000, 37000, 70000, 46000, 43000,
        68000, 55000, 39000, 62000, 47000,
        75000, 41000, 58000, 33000, 49000,
        36000, 54000, 56000, 72000, 44000
    ],
    
    "Performance Score": [
        78, 82, 85, 90, 80,
        88, 92, 75, 89, 84,
        91, 79, 93, 86, 83,
        94, 88, 81, 90, 85,
        95, 82, 87, 74, 89,
        80, 91, 88, 96, 84
    ]
}

df= pd.DataFrame(employee_data)

avg_mean=df["Salary"].mean()
total_sum=df["Salary"].sum()
min_sal=df["Salary"].min()
max_sal=df["Salary"].max()
count_sal=df["Salary"].count()
std_sal=df["Salary"].std()
print(f"Salary Mean : {avg_mean}\nTotal Sum of Salary : {total_sum} \nMininmum Salary : {min_sal}\nMaximum Salary : {max_sal}\ncount salary : {count_sal}\nStandard deviation of Salary : {std_sal}")

print("Group by :\n")
grouped=df.groupby("Age")["Salary"].sum()
#Grouped multiple columns 
#grouped=df.groupby(["Age","Name"])["Salary"].sum()
print(f"Salary Grouped by : \n {grouped}")
