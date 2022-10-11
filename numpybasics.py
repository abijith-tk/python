import numpy as np

# numpy basics
# arange() is used to add a sequence of numbers to an array
# syntax, arange(start,stop,step)   * start,update are optional arguments
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
b=np.array([1,2,3,4])
print(b)

# creating multi-dimensional arrays using array()

c=np.array([[1,2],[2,3]])
print(c)

# zeros() is used to create an array of zeroes
# ones() is used to create an array of ones
# empty() is used to create an empty array array whose initial content is random and depends on the state of the memory.
 
c=np.zeros((3,4))
d=np.ones((2,3))
e=np.empty((2,2))
print(c)
print(d)
print(e)

# linspace() similiar to arange(), floating point values
# syntax, linspace(start,stop,number of elements
f=np.linspace(1,5,20)
print(f)

