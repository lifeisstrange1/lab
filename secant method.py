# 30 sept
# secant method

import numpy as np

def f(x):
    return x**6 - x - 1 
    
x0, x1 = eval(input('x0,x1 \n'))
itr = 0
tol = 1e-06

while abs(x1-x0)>tol:
      itr = itr + 1
      x2 = x1 - f(x1) * (x1-x0) / (f(x1) - f(x0))
      x0 , x1 = x1, x2
      
print('Root = ', x1)
print('iterations = ', itr)

