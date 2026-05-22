import numpy as np

arr = np.array([1, 2, np.inf, 4, -np.inf, 6])
print(arr)

# Detect Infinite Values
# np.isinf()

print(np.isinf(arr))

# Remove Missing Values
new_arr = arr[~np.isinf(arr)]
print(new_arr)

# Replace Missing Values with 0
new_arr2 = arr
new_arr2[np.isinf(new_arr2)] = 0
print(new_arr2)


