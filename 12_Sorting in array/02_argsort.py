import numpy as np

arr = np.array([40, 20, 10, 30])

result = np.argsort(arr)
print(result)


# argsorting 2d array:
twod_arr = np.array([[20, 40], [10, 30]])

result = np.argsort(twod_arr)
print(result)

# specify argsorting axis
twod_arr = np.array([[20, 40], [10, 30]])

result = np.argsort(twod_arr, axis=0)
print(result)
result = np.argsort(twod_arr, axis=1)
print(result)
result = np.argsort(twod_arr, axis=None)
print(result)