import numpy as np

num_arr_0d = np.array(45)
print(num_arr_0d.dtype)

num_arr_1d = np.array([1, 2, 3, 4, 5, 6])
print(num_arr_1d.dtype)

num_arr_2d = np.array([['a', 'b', 'c'], ['d', 'e', 'f']])
print(num_arr_2d.dtype)

num_arr_3d = np.array([[[1, 2, 3], ['o', 5, 6]], [['a', 6, 'c'], [1, 5, 3]]])
print(num_arr_3d.dtype)

# Creating Arrays With a Defined Data Type

num_arr_1d = np.array([1, 2, 3, 4, 5, 6], dtype= 'S')
print(num_arr_1d.dtype)

num_arr_1d = np.array(['1', '2', '3', '4', '5', '6'], dtype= 'i')
print(num_arr_1d.dtype)