#NumPy Notes

## Array:
An array in NumPy is a data structure used to store multiple values in a single variable in an organized way.
###It is similar to a Python list, but:
- Faster  
- Uses less memory
- Supports mathematical operations easily

### Types of Array:
- 1) 0-D Array (Scalar)	Stores a single value as an array.  
Example: np.array(5)
- 2) 1-D Array	Stores elements in a single row/list.  	
Example: np.array([1, 2, 3])
- 3) 2-D Array	Stores data in rows and columns (matrix form).  
Example: np.array([[1,2],[3,4]])
- 4) 3-D Array	Stores multiple 2-D arrays together.  
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

| Parameter | Meaning                                |
| --------- | ---------------------------------------|
| `array`   | Original array                         |
| `values`  | Value(s) to add                        |
| `axis`    | Where to add (optional for 1d arrray)  |


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

### 12) Concatenate 2d array