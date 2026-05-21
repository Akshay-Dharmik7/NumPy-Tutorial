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
