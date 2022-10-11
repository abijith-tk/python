import numpy as np

# numpy basics
# arange() is used to add a sequence of numbers to an array
# syntax, arange(start,stop,step)   * start,update are optional arguments
# reshape() is used to specify the shape of the matrix
a=np.arange(10).reshape(5,2)
# reshape(-1)  : to change the array into a single dimensional array
print(a.reshape(-1))

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

c=np.array([[1,2],[2,3]],dtype=float)
print(c)

# we can access the array elements by specifying their indexes9
print(c[0,1])
print(c[1][0])

# zeros() is used to create an array of zeroes
# ones() is used to create an array of ones
# empty() is used to create an empty array array whose initial content is random and depends on the state of the memory.
 
c=np.zeros((3,4))
d=np.ones((2,3))
e=np.empty((2,2))
print(c)
print(d)
print(e)

# eye(),identity() is used to create an identity matrix
identity_matrix=np.eye(4)
print(identity_matrix)
print(np.identity(5))

# linspace() similiar to arange(), floating point values
# syntax, linspace(start,stop,number of elements,dtype=  )
f=np.linspace(1,5,20,dtype=np.half)  # np.half : built-in method change precision
print(f)
g=np.array([1,2],dtype='U')    # U : unicode string , S : byte string
print(g)

# astype() : creates a copy of an array and convert the data type of the copy
h=c.astype('i')
print(h)



