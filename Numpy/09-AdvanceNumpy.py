import numpy as np

#insert(array_name, index, value, axis=0(row wise) =1(column wise)) method is used to add element some specific position
arr1=np.array([1,2,3,4])
new_arr1=np.insert(arr1, 2, 100)
print(new_arr1)

arr2=np.array([[1,2],[3,4]])
arr2=np.insert(arr2, 1, [100,200], axis=0)
#np.insert(arr1, 1, [100,200], axis=1)
print(arr2)
# append(array_name, [])
new_arr3=np.append(arr1,[200,300])
print(new_arr3)

#concatenate((arr1,arr2), axis = 0(vertical stacking) and 1(horizontal stacking))
arr4=np.array([1,2,3])
arr5=np.array([4,5,6])
new_arr6=np.concatenate((arr4,arr5), axis=0)
print(new_arr6)

# delete(array_name, index, axis=None)
new_arr7=np.delete(new_arr6,2)
print(new_arr7)
new_arr8=np.delete(arr2,0,axis=1)
print(new_arr8)

#Stacking
arr9=np.array([1,2,3])
arr10=np.array([4,5,6])
print("vs",np.vstack((arr9,arr10))) # Vertically Stack -- row wise
print(np.hstack((arr9,arr10))) # Horizontal Stack -- column wise

#Splitting -- hsplit or vsplit

arr_new11=np.array([1,2,3,4,5,6])
print(np.split(arr_new11,2))