#InterPolate Method(method,axis,inplace=True) ---> linear, polynomial, time
# It preserves data integrity, smooth trends, avoid data loss
"""
1.time series data 
2.numeric data with trends
3.avoid dropping rows
"""
import pandas as pd

data={
    "Time":[1,2,3,4,5],
    "Value":[15,None,30,None,50]
}

df=pd.DataFrame(data)
print(df)

df['Value']=df['Value'].interpolate(method="linear")
print(f"After InterPolation \n {df}")