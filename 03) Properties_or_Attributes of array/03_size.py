import numpy as np

num_arr_0d = np.array(45)
print(num_arr_0d.size)

num_arr_1d = np.array([1, 2, 3, 4, 5, 6])
print(num_arr_1d.size)

num_arr_2d = np.array([[1, 2, 3], [4, 5, 6]])
print(num_arr_2d.size)

num_arr_3d = np.array([[[1, 2, 3], [4, 5, 6]], [[3, 6, 4], [1, 5, 3]]])
print(num_arr_3d.size)