
import numpy as np
arr = np.array([1, 2, 3])

# Example 1: Scalar Broadcasting
print("------ Scalar Broadcasting ------")
result = arr + 10
print(result)

# Example 2: Array Broadcasting
print("------ Array Broadcasting ------")
result = arr + [40, 50, 60]
print(result)

### Example 3: Different Shape Broadcasting
print("------ Different Shape Broadcasting ------")
arr = np.array([[1], [2], [3]])   # row * column
result = arr + [10, 20, 30]  
print(result) 

# Example 4: Matrix + Vector
print("------ Matrix + Vector Broadcasting ------")
arr = np.array([[1, 2, 3], [4, 5, 6]])   # row * column
result = arr + [10, 20, 30]  
print(result) 

# Broadcasting Error Example
# below example gives error due to incompatible shape of arrays
arr1 = np.array([[1, 2],
                 [3, 4]])

result = arr1 + [5, 6, 7]
print(result)



