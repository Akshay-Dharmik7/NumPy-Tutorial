import numpy as np

arr = np.array([10, 20, 30, 40])

result = np.extract(arr > 20, arr)
print(result)

# Using Multiple Conditions
result = np.extract((arr > 20) & (arr < 40), arr)
print(result)