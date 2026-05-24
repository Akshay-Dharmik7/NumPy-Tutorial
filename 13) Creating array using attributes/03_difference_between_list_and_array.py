import numpy as np

py_list = [1, 2, 3] # list wise multiplication
print("Python list multiplication ", py_list * 2)

np_array = np.array([1, 2, 3]) #element wise multiplication
print("Python array multiplication ", np_array * 2)

import time
start = time.time()
py_list = [i*2 for i in range(1000000)]
print("\n List operation time: ", time.time() - start)

start = time.time()
np_array = np.arange(1000000) * 2
print("\n Numpy operation time: ", time.time() - start)