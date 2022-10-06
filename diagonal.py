# Sum of diagonal elements of a matrix

import numpy as np
mat=np.arange(16).reshape(4,4)
dia=mat.diagonal()
print(dia)     # to print diagonal elements
print(dia.sum())
print(mat.trace())       # to print sum of diagonal elements
