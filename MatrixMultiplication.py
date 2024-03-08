import numpy as np

A_mat = np.array([[10, 20, 30], [100, 200, 300], [1, 2, 3]])
B_mat = np.array([[1, 5],[10, 20], [100, 200]])

print("AxB:\n")
print((A_mat @ B_mat)) # 3x3 @ 3x2 ====> OK

print("\nBxA:\n")
print(B_mat @ A_mat) #3x2 @ 3x3 ====> Not OK (The order of matrices in multiplication matters.)