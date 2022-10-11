import numpy as np

# numpy basics

# reshape() is used to specify the shape of the matrix
a=np.arange(10).reshape(5,2)

# ndim is used to find array dimension
print(a.ndim)

# shape is used to find the shape of the matrix/array 
print(a.shape)

# size is used to find the total number of elements in the array.
# that is product of the shape
print(a.size)
