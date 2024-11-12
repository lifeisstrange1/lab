# 30 sept
# gauss jacobi / seidel method

import numpy as np
from numpy.linalg import norm, solve

A = np.array([[3,2,4], [2,1,1], [1,3,5]])
B = np.array([7,4,2])

n = B.size

X = np.zeros(n)

itr = 0
err = 1000

while err > 1e-06:
      itr = itr + 1
      X0 = X.copy()
      
      for i in range(n):
          X[i] = (B[i]-np.sum(A[i]*X)+A[i,i]*X[i])/A[i,i]
          
          
      err = norm(X-X0)
      
      
print(X)
print('no. of iterations : ', itr)          
          
print('solution by linalg module')
print(solve(A,B))          
       
      




