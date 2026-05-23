import numpy as np

arr = np.array([40, 20, 10, 30])

result = np.sort(arr)
print(result)


# sorting 2d array:
twod_arr = np.array([[20, 40], [10, 30]])

result = np.sort(twod_arr)
print(result)

# specify sorting axis
twod_arr = np.array([[20, 40], [10, 30]])

result = np.sort(twod_arr, axis=0)
print(result)
result = np.sort(twod_arr, axis=1)
print(result)
result = np.sort(twod_arr, axis=None)
print(result)
