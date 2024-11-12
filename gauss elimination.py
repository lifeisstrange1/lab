# 23 sept

import numpy as np


A1 = np.array([[3,2,4], [2,1,1], [1,3,5]])
b = np.array([7,4,2])


A = np.array([[3,2,4,7],
              [2,1,1,4], 
              [1,3,5,2]], dtype = 'float')
              
              
n = len(A)


def GE(A,n):
    for k in range(n-1):
        for i in range(k+1,n):
            ratio = A[i,k]/A[k,k]
            A[i,:] = A[i,:] - ratio*A[k,:]
            
    return                     
              
def BS(A,n):
    B = A[:,-1]
    for i in range(n-1, -1, -1):
        X[i] = (B[i]-sum(A[i, i+1:n]*X[i+1:n]))/A[i,i]
        
    return
    
GE(A,n)
print(A)

X = np.zeros(n)    

BS(A,n)

print(X)

print(np.linalg.solve(A1,b))




        
