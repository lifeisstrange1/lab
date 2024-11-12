# 14/10/2024  least square fitting

import numpy as np
from numpy.linalg import solve
import matplotlib.pyplot as plt

x = np.array([2,4,6,8,10])
y = np.array([42.0,48.4,51.3,56.3,58.3])

n = x.size
sx = np.sum(x)
sy = np.sum(y)

sx2 = np.sum(x**2)
sxy = np.sum(x*y)

A = np.array([[n,sx],[sx,sx2]])
B = np.array([sy,sxy])

C = solve(A,B)
a0, a1 = C

print(C)

yfit = a0 + a1*x
plt.plot(x,y,'o')
plt.plot(x,yfit)
plt.show()

