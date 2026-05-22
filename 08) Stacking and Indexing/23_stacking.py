import numpy as np

arr1 = np.array([1, 2, 3, 4])
arr2 = np.array([5, 6, 7, 8])
print(arr1)
print(arr2)

# vstack((a,b))
print(np.vstack((arr1, arr2)))

# hstack((a,b))
print(np.hstack((arr1, arr2)))

#dstack((a,b))
print(np.dstack((arr1, arr2)))

# column_stack((a, b))
print(np.column_stack((arr1, arr2))) #same as dstack

# row_stack((a, b))
print(np.row_stack((arr1, arr2))) #same as vstack (deprecated)