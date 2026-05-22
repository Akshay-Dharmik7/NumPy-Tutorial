import numpy as np

arr1 = np.array([1, 2, 3, 4, 5, 6, 7, 6])
arr2 = np.array([[1, 2], [4, 5]])
arr3 = np.array([[[1, 2], [4, 5]]])

# split- not allow unequal splitting
# splitting 1d array
print(np.split(arr1, 2))
print(np.split(arr2, 2, axis=0))
print(np.split(arr2, 2, axis=1))

# splitting array using index position
print(np.split(arr1, [3]))

# array_split()
print(np.array_split(arr1, 3))  #allow unequal splitting


# vsplit and hsplit work on 2d array
# vsplit
print(np.vsplit(arr2, 2))

# hsplit
print(np.hsplit(arr2, 2))

# dsplit
print(np.dsplit(arr3, 2))

