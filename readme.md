#NumPy Notes

## Array:

An array in NumPy is a data structure used to store multiple values in a single variable in an organized way.
###It is similar to a Python list, but:

- Faster
- Uses less memory
- Supports mathematical operations easily

### Types of Array:

- 1. 0-D Array (Scalar) Stores a single value as an array.  
     Example: np.array(5)
- 2. 1-D Array Stores elements in a single row/list.
     Example: np.array([1, 2, 3])
- 3. 2-D Array Stores data in rows and columns (matrix form).  
     Example: np.array([[1,2],[3,4]])
- 4. 3-D Array Stores multiple 2-D arrays together.  
     Example: np.array([[[1,2]], [[3,4]]])

## Attributes/Properties of Array

| Property   | Meaning                         | Example        |
| ---------- | ------------------------------- | -------------- |
| `ndim`     | Number of dimensions            | `arr.ndim`     |
| `shape`    | Size of array in each dimension | `arr.shape`    |
| `size`     | Total number of elements        | `arr.size`     |
| `dtype`    | Data type of elements           | `arr.dtype`    |
| `itemsize` | Size of one element in bytes    | `arr.itemsize` |
| `nbytes`   | Total memory used by array      | `arr.nbytes`   |
| `T`        | Transpose of array              | `arr.T`        |

## Aggregate Function of array

| Function   | Purpose                       | Example          |
| ---------- | ----------------------------- | ---------------- |
| `sum()`    | Adds all elements             | `np.sum(arr)`    |
| `mean()`   | Finds average value           | `np.mean(arr)`   |
| `min()`    | Finds smallest value          | `np.min(arr)`    |
| `max()`    | Finds largest value           | `np.max(arr)`    |
| `std()`    | Calculates standard deviation | `np.std(arr)`    |
| `var()`    | Calculates variance           | `np.var(arr)`    |
| `prod()`   | Multiplies all elements       | `np.prod(arr)`   |
| `argmin()` | Index of minimum value        | `np.argmin(arr)` |
| `argmax()` | Index of maximum value        | `np.argmax(arr)` |
| `median()` | Finds middle value            | `np.median(arr)` |

## Flattening in NumPy Arrays

- Flattening means converting a multi-dimensional array (2D, 3D, etc.) into a one-dimensional (1D) array.

### Methods for Flattening

| Method      | Description                            | Example         |
| ----------- | -------------------------------------- | --------------- |
| `flatten()` | Returns a flattened copy of the array  | `arr.flatten()` |
| `ravel()`   | Returns a flattened view (if possible) | `arr.ravel()`   |

## Insert Elements into NumPy Arrays

- In NumPy, elements can be inserted into an array using the np.insert() function.

### Syntax:

- np.insert(array, index, value)

| Parameter | Meaning                          |
| --------- | -------------------------------- |
| `array`   | Original array                   |
| `index`   | Position where value is inserted |
| `value`   | Element to insert                |

### Insert into 2-D Array

### Syntax:

- np.insert(array, index, value, axis)

| Parameter | Meaning                          |
| --------- | -------------------------------- |
| `array`   | Original array                   |
| `index`   | Position where value is inserted |
| `value`   | Element to insert                |
| `axis`    | set axis(row/column)             |

#### Example:

arr = np.array([[1, 2], [4, 5]])

new_arr = np.insert(arr, 1, [3, 3], axis=0)  
print(new_arr)

- axis=0 → insert row
- axis=1 → insert column

## Appending Elements in NumPy Arrays

- Appending means adding elements at the end of an array. In NumPy, this is done using np.append().

### Syntax:

- np.append(array, values, axis=None)

| Parameter | Meaning                               |
| --------- | ------------------------------------- |
| `array`   | Original array                        |
| `values`  | Value(s) to add                       |
| `axis`    | Where to add (optional for 1d arrray) |

## Removing Elements from NumPy Arrays

- In NumPy, elements are removed using functions like np.delete() because arrays have fixed size (unlike Python lists).

### 1. Using np.delete():

#### Syntax:

- np.delete(array, index)

| Parameter | Meaning                       |
| --------- | ----------------------------- |
| `array`   | Original array                |
| `index`   | Position of element to remove |

### 2. Removing from 2-D Array

#### Example:

arr = np.array([[1, 2, 3], [4, 5, 6]])

new_arr = np.delete(arr, 1, axis=0)  
print(new_arr)

#### Explanation:

- axis=0 → row removal
- axis=1 → column removal

## Concatenate array

- The concatenate() function in NumPy is used to join two or more arrays together along a specified axis.

### Syntax:

- numpy.concatenate((array1, array2, ...), axis=0)

| Parameter | Description                        |
| --------- | ---------------------------------- |
| `arrays`  | Tuple or list of arrays to join    |
| `axis`    | Axis along which arrays are joined |

### 1) Concatenate 1d array

#### Example:

arr1 = np.array([1, 2, 3, 4])  
arr2 = np.array([5, 6, 7, 8])

new_arr = np.concatenate((arr1, arr2))  
print(new_arr)

### 2) Concatenate 2d array

#### Example:

arr1 = np.array([[1, 2, 3], [4, 5, 6]])  
arr2 = np.array([[5, 6, 7], [8, 9, 0]])

new_arr = np.concatenate((arr1, arr2), axis = 0)  
print(new_arr)

## Stacking in numpy

- Stacking in NumPy means combining multiple arrays together either vertically, horizontally, or along a new axis.
- NumPy provides several stacking functions:

| Function         | Purpose                           |
| ---------------- | --------------------------------- |
| `stack()`        | Join arrays along a new axis      |
| `vstack()`       | Vertical stacking (row-wise)      |
| `hstack()`       | Horizontal stacking (column-wise) |
| `dstack()`       | Depth-wise stacking               |
| `column_stack()` | Stack 1D arrays as columns        |
| `row_stack()`    | Stack arrays row-wise             |

#### 1. stack() Function:

- Creates a new dimension while joining arrays.
- np.stack((a, b), axis=0)

#### 2. vstack() → Vertical Stack:

- Stacks arrays row-wise.
- result = np.vstack((a, b))

#### 3. hstack() → Horizontal Stack

- Stacks arrays column-wise.
- result = np.hstack((a, b))

#### 4. dstack() → Depth Stack

- Stacks arrays along the third dimension.
- result = np.dstack((a, b))

#### 5. column_stack()

- Stacks 1D arrays as columns.
- result = np.column_stack((a, b))

#### 6. row_stack():

- Stacks arrays row-wise.
- result = np.row_stack((a, b))

## Splitting in NumPy means dividing an array into multiple smaller arrays.

- NumPy provides several functions for splitting arrays.

### Types of Splitting Functions:

| Function        | Purpose                                      |
| --------------- | -------------------------------------------- |
| `split()`       | General splitting                            |
| `array_split()` | Split even if equal division is not possible |
| `hsplit()`      | Horizontal split                             |
| `vsplit()`      | Vertical split                               |
| `dsplit()`      | Depth split                                  |

### 1. split() Function:

- Splits an array into equal parts.
- np.split(array, sections, axis=0)

| Parameter  | Description                         |
| ---------- | ----------------------------------- |
| `array`    | Input array                         |
| `sections` | Number of splits or index positions |
| `axis`     | Axis to split                       |

#### Example 1: Split 1D Array:

arr = np.array([1, 2, 3, 4, 5, 6])  
result = np.split(arr, 3)  
print(result)

#### Example 2: Split Using Index Positions:

arr = np.array([1, 2, 3, 4, 5, 6])  
result = np.split(arr, [2, 4])  
print(result)

### 2. array_split() Function

- Used when equal division is NOT possible.

#### Example:

arr = np.array([1, 2, 3, 4, 5])  
result = np.array_split(arr, 3)  
print(result)

### Difference:

- split() → requires equal division
- array_split() → allows unequal division

### 3. hsplit() → Horizontal Split

- Splits columns.

#### Example:

arr = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])  
result = np.hsplit(arr, 2)  
print(result)

### 4. vsplit() → Vertical Split

- Splits rows.

#### Example:

arr = np.array([[1, 2], [3, 4], [5, 6], [7, 8]])  
result = np.vsplit(arr, 2)  
print(result)

### 5. dsplit() → Depth Split

- Splits along third axis.

#### Example:

arr = np.array([[[1, 2], [3, 4]]])  
result = np.dsplit(arr, 2)  
print(result)

## Broadcasting in NumPy

- Broadcasting in NumPy is a technique that allows NumPy to perform arithmetic operations on arrays of different shapes automatically.
- It avoids writing loops and makes operations faster and simpler.

### What is Broadcasting?

- Broadcasting means: Smaller array is automatically expanded to match the shape of larger array.

### Example 1: Scalar Broadcasting

arr = np.array([1, 2, 3])  
result = arr + 10  
print(result)

- (NumPy automatically broadcasts 10).

# Example 2: Array Broadcasting

arr = np.array([1, 2, 3])  
result = arr + [40, 50, 60]  
print(result)

- (Same shape → direct operation).

### Example 3: Different Shape Broadcasting

arr = np.array([[1], [2], [3]]) #(row \* column)  
result = arr + [10, 20, 30]  
print(result)

### Broadcasting Rules

- Two dimensions are compatible when:
  - They are equal.
  - One of them is 1

#### Rule Checking Example

Compatible:  
(3,1)  
(1,3)

Compatible → Result shape: (3, 3)

Not Compatible:  
(2,3)  
(3,2)

Error occurs.

### Example 4: Matrix + Vector

arr = np.array([[1, 2, 3], [4, 5, 6]]) # row \* column  
result = arr + [10, 20, 30]  
print(result)

- (Vector is broadcast to each row).

### Broadcasting Error Example
- Below example gives error due to incompatible shape of arrays.     

arr1 = np.array([[1, 2], [3, 4]])  
result = arr1 + [5, 6, 7]  
print(result)  

## Vectorization in NumPy:
- Vectorization in NumPy means performing operations on entire arrays at once instead of using loops.
- It makes code:
     - Faster
     - Shorter
     - More memory efficient

### What is Vectorization?
Instead of using for loop element by element NumPy performs operations directly on arrays internally using optimized C code.  

### Why Vectorization is Fast
- NumPy arrays are:
     - Stored in contiguous memory
     - Implemented in optimized C
     - Processed using SIMD/internal optimizations
- So operations are much faster than Python loops.

### Common Vectorized Operations
- Addition: a+b
- Subtraction: a-b
- Multiplication: a*b
- Division: a/b
- Power: a**b

### Important Vectorized Functions
| Function       | Purpose              |
| -------------- | -------------------- |
| `np.sqrt()`    | Square root          |
| `np.exp()`     | Exponential          |
| `np.log()`     | Logarithm            |
| `np.sin()`     | Sine                 |
| `np.cos()`     | Cosine               |
| `np.maximum()` | Element-wise maximum |
| `np.minimum()` | Element-wise minimum |


## Handling missing and incorrect values:
- Handling missing and incorrect values in NumPy is important in data processing and analysis.
- NumPy mainly handles:
     - Missing values (NaN)
     - Infinite values (inf)
     - replace missing value to number (nan_to_num)
     - Incorrect/invalid values
     - Null-like values

### 1. Missing Values in NumPy
- NumPy represents missing values using:  `np.nan`  
- NaN means - Not a Number


### 2. Handling Infinite Values
- NumPy may represent infinite values using: `np.inf` and `-np.inf`

### 3. Replacing Missing/Infinite values
#### nan_to_num():

- nan_to_num() in NumPy is used to replace:
     - NaN values
     - Positive infinity (inf)
     - Negative infinity (-inf)
- with numeric values.
- nan_to_num() in NumPy is used to replace NaN and infinite values with finite numeric values to clean and stabilize numerical computations
- Syntax:
     - `np.nan_to_num(array, nan=0.0, posinf=None, neginf=None)`

| Parameter | Description             |
| --------- | ----------------------- |
| `array`   | Input array             |
| `nan`     | Value to replace `NaN`  |
| `posinf`  | Value to replace `+inf` |
| `neginf`  | Value to replace `-inf` |


## Searching in NumPy
### Searching in NumPy means finding:
- Specific values
- Index positions
- Maximum/minimum values
- Conditions inside arrays  

- NumPy provides many searching functions.

### Common Searching Functions
| Function         | Purpose                           |
| ---------------- | --------------------------------- |
| `where()`        | Find elements based on condition  |
| `argmax()`       | Index of maximum value            |
| `argmin()`       | Index of minimum value            |
| `nonzero()`      | Find non-zero elements            |
| `searchsorted()` | Find insertion index              |
| `extract()`      | Extract elements using condition  |
| `argwhere()`     | Find indices satisfying condition |

### 1. where() Function:  
- Find elements matching a condition.
- Syntax: 
     - np.where(condition)

### 2. argmax() Function:
- Returns index of maximum value.
- Syntax:
     - np.argmax(array)

### 3. argmin() Function:
- Returns index of minimum value.
- Syntax:
     - np.argmin(array)

### 4. nonzero() Function:
- Finds non-zero elements and return their indexes.
- Syntax:
     - np.nonzero(array)

### 5. searchsorted():
- searchsorted() in NumPy is used to find the position where an element should be inserted in a sorted array to maintain the sorted order.
- Syntax:
     - np.searchsorted(array, value, side='left')

| Parameter | Description           |
| --------- | --------------------- |
| `array`   | Sorted input array    |
| `value`   | Value to search       |
| `side`    | `'left'` or `'right'` |

### 6. extract():
- extract() in NumPy is used to extract elements from an array that satisfy a given condition.
- It works similar to boolean masking.
- Syntax:
     - np.extract(condition, array)

| Parameter   | Description       |
| ----------- | ----------------- |
| `condition` | Boolean condition |
| `array`     | Input array       |
