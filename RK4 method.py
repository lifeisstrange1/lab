# rk4 method
import numpy as np

x, y = 0, 2
h = 0.7
y2 = [2]
y_al = []


def f(x,y): return (x**2)/y
def g(x): return ((2*x**3)/3 + 4)**0.5

for i in range(0,3):
     
     k1 = h * f(x, y)
     k2 = h * f(x + 0.5*h, y + 0.5*k1)
     k3 = h * f(x + 0.5*h, y + 0.5*k2)
     k4 = h * f(x + h, y + k3)
     y = y + (k1 + 2*k2 + 2*k3 + k4)/6.0
     x = x + h
     
     y2.append(y)


X = 0     
for i in range(0,4):
    al = g(X)
    X = X + 0.7
    y_al.append(al)
    
          
     
y2 = np.array(y2)   
y_al = np.array(y_al)     
print('RK4 result = ', y2) 
print('Analytic result = ', y_al)    
print('Error = ', (y_al-y2)/y_al*100)

 
