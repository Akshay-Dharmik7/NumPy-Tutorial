import numpy as np

arr1 = np.array([[1, 2, 3], [4, 5, 6]])
arr2 = np.array([[5, 6, 7], [8, 9, 0]])
print(arr1)
print(arr2)

new_arr = np.concatenate((arr1, arr2), axis = 0) 
print(new_arr)

new_arr = np.concatenate((arr1, arr2), axis = 1) 
print(new_arr)

new_arr = np.concatenate((arr1, arr2), axis = None) 
print(new_arr)