# Changing datatype of array
import numpy as np

num_arr_1d = np.array([1, 2, 3, 4, 5, 6])
print(num_arr_1d.dtype)
new_num_arr_1d = num_arr_1d.astype('S')
print(new_num_arr_1d.dtype)

num_arr_1d = np.array(['1', '2', '3', '4', '5', '6'])
print(num_arr_1d.dtype)
new_num_arr_1d = num_arr_1d.astype('i')
print(new_num_arr_1d.dtype)

