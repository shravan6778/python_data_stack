# To find to the missing numbers in an array use isnan(array_name) method
import numpy as np
arr=np.array([1,np.nan,3,np.nan,5])
print(np.isnan(arr))
#To replace missing values use nan_to_num() method
arr_1=np.nan_to_num(arr,nan=100)
print(arr_1)

# To find any large inf values use isinf() method
arr2=np.array([1,np.inf,3,-np.inf,5])
print(np.isinf(arr2))
#To handle inf values use nan_to_num() method
arr3=np.nan_to_num(arr2,posinf=1000,neginf=-1000)
print(arr3)