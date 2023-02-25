import numpy as np 
input_mat = np.array([])
print("type the matrix row-wise and enter 0 in space of blank space")
for i in range (9):
    val = input()
    input_mat = np.append(input_mat, val)

input_mat = np.reshape(input_mat, (3,3))
print(input_mat)