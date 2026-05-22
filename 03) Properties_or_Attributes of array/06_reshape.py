import numpy as np

arr = np.array([1, 2, 3, 4, 5, 6])
print(arr.shape)

new_arr = arr.reshape(2, 3)
print(f'Array: {new_arr},\n\nShape: {new_arr.shape}')