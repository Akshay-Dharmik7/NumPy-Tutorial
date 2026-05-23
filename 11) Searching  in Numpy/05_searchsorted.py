import numpy as np

arr = np.array([10, 20, 30, 40])

result = np.searchsorted(arr, 20)
print(result)

result = np.searchsorted(arr, 25)
print(result)

result = np.searchsorted(arr, 20, side = 'left')
print(result)
result = np.searchsorted(arr, 25, side = 'left')
print(result)

result = np.searchsorted(arr, 20, side = 'right')
print(result)
result = np.searchsorted(arr, 25, side = 'right')
print(result)
