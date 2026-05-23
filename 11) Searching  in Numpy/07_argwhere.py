import numpy as np

arr = np.array([10, 20, 30, 40])

result = np.argwhere(arr > 20)
print(result)

# from 2D array

arr1 = np.array([[10, 20], [30, 40]])

result = np.argwhere(arr1 > 20)
print(result)

