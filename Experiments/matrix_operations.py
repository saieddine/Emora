import numpy as np
import math 
A=np.array([[1,2],[3,4]])
B=np.array([[10,20],[30,40]])
addition=A+B
element_multiplication=A*B
matrix_multiplication=A@B
print(addition)
print(element_multiplication)
print(matrix_multiplication)
print(A.shape)