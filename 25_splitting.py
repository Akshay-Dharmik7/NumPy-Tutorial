import numpy as np

arr1 = np.array([1, 2, 3, 4, 5, 6, 7, 6])
print(arr1)

# split
print(np.split(arr1, 2))

arr2 = np.array([[1, 2], [4, 5]])
# vsplit
print(np.vsplit(arr2, 2))

# hsplit
print(np.hsplit(arr2, 2))
