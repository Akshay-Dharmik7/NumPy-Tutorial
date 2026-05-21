import numpy as np

arr = np.array([1, 2, 3, 4])
print(arr)

new_arr = np.insert( arr, 3 , [5, 6]) #array, index, value
print(new_arr)