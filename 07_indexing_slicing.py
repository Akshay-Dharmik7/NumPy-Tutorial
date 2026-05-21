import numpy as np

num_arr = np.array([1, 2, 3, 4, 5, 6])
print(num_arr)

# Indexing
print("---------- Indexing --------------")
print(f'Element: {num_arr[0]}, Index: 0')
print(f'Element: {num_arr[1]}, Index: 1')
print(f'Element: {num_arr[2]}, Index: 2')
print(f'Element: {num_arr[3]}, Index: 3')
print(f'Element: {num_arr[4]}, Index: 4')
print(f'Element: {num_arr[5]}, Index: 5')

# Slicing
print('-------------- Slicing ---------------')
print(num_arr[1:])
print(num_arr[:-1])
print(num_arr[1:5:1])
print(num_arr[-5:-1:2])

# Fancy Indexing
print('------- Fancy Indexing ------------')
print(num_arr[[1, 3, 5]])

# Boolean Masking (Conditional Filtering)
print('-------- Boolean Masking -------------')
print(num_arr[num_arr > 4])


num_arr_2d = np.array([[1, 2, 3], [4, 5, 6]])

# Indexing 2D array
print('--------- Indexing 2D array --------')
print(num_arr_2d[0][1])
# or
print(num_arr_2d[0, 1])
 
# Slicing 2D array
print('--------- Slicing 2D array --------')
print(num_arr_2d[1:, 1:])
