import numpy as np

arr = np.array([1, 2, np.nan, 4, np.nan, 6])
print(arr)

# Detect Missing Values
# np.isnan()

print(np.isnan(arr))

# Remove Missing Values
new_arr = arr[~np.isnan(arr)]
print(new_arr)

# Replace Missing Values wiyh 0
new_arr2 = arr
new_arr2[np.isnan(new_arr2)] = 0
print(new_arr2)

# Replace with Mean Value
new_arr3 = arr
mean = np.nanmean(arr)
new_arr3[np.isnan(new_arr3)] = mean
print(new_arr3)

