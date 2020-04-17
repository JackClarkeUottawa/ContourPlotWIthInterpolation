"""
Q.1 a) I would use LU factorization with the crout algorithm because it uses the least amount of memory and is easiest to write
b)
"""

A = [[6,3,2],
     [3,7,1],
     [2,2,6]]
def LUdecompCrout(A):
    S = [0,1]
    L = [[0,0,0],
         [0,0,0],
         [0,0,0]]
    U = [[0,0,0],
         [0,0,0],
         [0,0,0]]
    S[0] = len(A) # S[0] is the number of rows
    S[1] = len(A[0]) # S[1] is the number of columns
    for k in range(0, 3):
        U[k][k] = 1

        for j in range(k, 3):
            sum0 = sum([L[j][s] * U[s][k] for s in range(0, j)])  # range from index 0
            L[j][k] = A[j][k] - sum0  # reversed index
        print("L: ")
        print(L)
        for j in range(k + 1, 3):
            sum1 = sum([L[k][s] * U[s][j] for s in range(0, k)])  # range from index 0
            U[k][j] = (A[k][j] - sum1) / L[k][k]
        print("U: ")
        print(U)
    print(L)
    print(U)
    return L, U


LUdecompCrout(A)
"""Q4."""
import numpy as np
def torad(a):
    return(a*2*np.pi/360)
A = np.array([[np.cos(torad(45)),0,0,-1,np.cos(torad(30)),0,0,0,0],
              [np.sin(torad(45)),0,1,0,np.sin(torad(30)),0,0,0,0],
              [0,1,0,0,0,-1,0,0,0],
              [0,0,-1,0,0,0,0,0,0],
              [0,0,0,1,0,0,0,0,-np.sin(torad(45))],
              [0,0,0,0,0,0,1,0,np.cos(torad(45))],
              [0,0,0,0,np.cos(torad(30)),1,0,-1,0],
              [0,0,0,0,np.sin(30),0,1,0,0],
              [0,0,0,0,0,0,0,1,np.cos(torad(45))]])
B = np.array([0,-1000,0,0,500,0,0,500,0])
print(np.matmul(np.linalg.inv(A),B))