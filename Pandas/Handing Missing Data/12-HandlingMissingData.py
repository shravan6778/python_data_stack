# dropna() method is used to delete the missing data if wwe think deleting missing data does not affect the entire data if axis=0 means it deletes rows missing data and axis = 1 means deletes columns missing data

import pandas as pd
employee_data = {
    "Name": [
        "Amit", None, "Suresh", "Kiran", "Anjali",
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
        30000, None, 42000, 50000, 38000,
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

df.dropna(axis=0, inplace=True)
print(df)