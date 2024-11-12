# 11 nov 2024
# euler method

import numpy as np

def f(x,y): return (x**2)/y
def g(x): return ((2*x**3)/3 + 4)**0.5

x, y = 0, 2
h = 0.7
y1 = [2]
y_al = []


for i in range(0,3):
    
    y = y + h * f(x,y)
    x = x + h 
    
    y1.append(y)
    

X = 0     
for i in range(0,4):
    al = g(X)
    X = X + 0.7
    y_al.append(al)
    
y1 = np.array(y1)   
y_al = np.array(y_al)    
print('Euler result = ', y1)  
print('Analytic result = ', y_al) 
print('Error = ', (y_al-y1)/y_al*100) 


 





    
    
