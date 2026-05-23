import numpy as np

arr = np.array([10, 20, 30, 40])
result = np.where(arr > 20)

print(result)

# Using where() for Replacement
new_arr = np.where(arr > 20, 20, arr)
print(new_arr)

