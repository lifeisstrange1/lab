# 30 sept
# power method : eigen value problem

import numpy as np
from numpy.linalg import norm

A = np.array([[2,1,2], [4,2,4], [2,1,2]])
x = np.array([[1,0,0]]).T

tol = 0.001

ev = 0
ev_prev = 0

while abs(ev - ev_prev) < tol:
    x = A @ x / norm(A @ x)
    ev = (x.T @ A @ x) / (x.T @ x)
    
    
print('eigen value = ', float(ev))
print('eigen vector = ', x)


