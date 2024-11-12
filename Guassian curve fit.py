# 21/10/2024

import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit


def gaussian(x, A, x0, sigma):
    return A*np.exp(-((x-x0)/sigma)**2)

def derivative(x, A, x0, sigma):
    return -0.5*(1/sigma**2)*A*np.exp(-((x-x0)/sigma)**2)*(x-x0)
   

A, x0, sigma = 1,4,1
    
x = np.linspace(-10,10,100) + 0.1*np.random.random(100)

y = gaussian(x,A,x0,sigma) + 0.1*np.random.random(100)

# dy = derivative(x, A, x0, sigma) + 0.1*np.random.random(100)

coef, error = curve_fit(gaussian, x, y)
coef1, error1 = curve_fit(derivative, x, y)

print(coef)

plt.plot(x,y, 'o')
# plt.plot(x, dy, 'o')
plt.plot(x, gaussian(x, coef[0], coef[1], coef[2]))
plt.plot(x, derivative(x, coef[0], coef[1], coef[2]))
plt.show()
