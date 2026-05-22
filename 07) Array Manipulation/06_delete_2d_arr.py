import numpy as np

arr = np.array([[1,2], [3,4]])
print(arr)

new_arr = np.delete(arr, 1, axis = 0)
print(new_arr)
print(new_arr.shape)

new_arr = np.delete(arr, 1, axis = 1)
print(new_arr)
print(new_arr.shape)

new_arr = np.delete(arr, 1, axis = None) #convert into 1d array
print(new_arr)
print(new_arr.shape)