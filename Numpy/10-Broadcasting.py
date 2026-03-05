#Broadcasting a mechanism that allows arithmetic operations between arrays of different shapes by implicitly stretching or replicating the smaller array to match the larger one, without making unnecessary data copies

#For to determine discount pf prices on an array
import numpy as np
prices=np.array([150,170,270,100])
discount=10
final_prices=prices-(prices*(discount/100))
print(final_prices)



# 1D to 2D array
arr2=np.array([[1,2,3],[4,5,6]])
arr3=np.array([10,10,10])
res1=arr2+arr3
print(res1)


#1.Matching Dimension -- same dimension of both arrays [1,2,3] + [4,5,6]
#Single element Broadcasting
arr1=np.array([9,8,7])
res=arr1*10
print(res)

#2.Expanding single elements -- like [1,2,3] + 10
# 1D to 2D array
arr2=np.array([[1,2,3],[4,5,6]])
arr3=np.array([10,10,10])
res1=arr2+arr3
print(res1)

#3.Icompatible shapes --- like [1,2,3] + [1,2]
# 1D to 2D array
arr2=np.array([[1,2,3],[4,5,6]])
arr3=np.array([10,10])
res1=arr2+arr3 
print(res1) # error