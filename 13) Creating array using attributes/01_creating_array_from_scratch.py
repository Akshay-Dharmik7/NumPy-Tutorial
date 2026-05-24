import numpy as np

# creating array of zeros
zeros = np.zeros((2, 3))
print(zeros)

# creating array of one
ones = np.ones((2, 3))
print(ones)

# creating array of constant value
full = np.full((2, 3), 8)
print(full)

# creatng array for perticular sequence
# ex: 1 to 10, 'a' to 'z'
sequence = np.arange(1, 10, 2)
print(sequence)

# creating array of random values
random_arr = np.random.random((3, 2))
print(random_arr)