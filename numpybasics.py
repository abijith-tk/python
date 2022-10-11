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


# dtype is used to find the data type of the array
print(a.dtype)

# itemsize is used to find the bytes of each element in the array
print(a.itemsize)

# array() is used to create an array using python tuple or list
# syntax, array(*tuple/list*,dtype=*data type*)
b=array([1,2,3,4])
print(b)

# creating multi-dimensional arrays using array()

c=array([[1,2],[2,3]])
print(c)

