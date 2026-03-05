import pandas as pd
data={
    "Name":['Shravan','Sandy','Ceo Of India'],
    "Age":[21,20,100],
    "City":['Hyderabad','Hyd','Hyd']
}
df=pd.DataFrame(data)
print(df)
df.to_csv("02-Output.csv", index=False)