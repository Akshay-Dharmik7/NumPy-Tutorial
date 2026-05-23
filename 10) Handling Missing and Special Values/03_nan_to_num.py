import numpy as np


# replacing missing(nan) value
new_arr = np.nan_to_num([1, np.nan, 3])
print(new_arr)

# replacing infinite(nan) value
new_arr = np.nan_to_num([1, np.inf, -np.inf])
print(new_arr)

# Custom Replacement Values
arr = np.array([1, np.nan, np.inf, -np.inf])

new_arr = np.nan_to_num(arr, nan=0, posinf=100, neginf=-100)
print(new_arr)