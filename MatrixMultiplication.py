# to-do
# compare computational efficiency of vanilla python vs numpy @ notation function when multiplying laaaarge scale matrices. 

import numpy as np

A_mat = np.array([[10, 20, 30], [100, 200, 300], [1, 2, 3]]) # 3 x 3
B_mat = np.array([[1, 5],[10, 20], [100, 200]])              # 3 x 2

C_mat = np.array([[0,0,0],[0,0,0],[0,0,0]])

print("AxB:\n")
print((A_mat @ B_mat)) # 3x3 @ 3x2 ====> OK


# print(B_mat @ A_mat) #3x2 @ 3x3 ====> Not OK (The order of matrices in multiplication matters.)


for i in range(len(A_mat)):
    for j in range(len(B_mat[0])):
        for k in range(len(B_mat)):
            print("A(",i,k,")",A_mat[i][k], " x B(",k,j,")", B_mat[k][j],"=", A_mat[i][k] * B_mat[k][j]) #in python, concatenate with ","
            C_mat[i][j] += A_mat[i][k] * B_mat[k][j]
    
print(C_mat)