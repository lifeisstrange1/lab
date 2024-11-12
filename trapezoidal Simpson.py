# trapeziodal 
# simpson 1/3 rule


import numpy as np

def f(x):
    return np.sqrt(x)
    
a, b, n = 0, 1, 10
h = (b-a)/n

I1 = 0.5*h*(f(a) + f(b) + 2*sum([f(a+i*h) for i in range(1,n)]))

print('value using trapeziodal = ', I1)    
    
s_odd = 4*sum([f(a+i*h) for i in range (1,n,2)])
s_even = 2*sum([f(a+i*h) for i in range(2,n-1,2)])

I2 = h/3 * (f(a) + f(b) + s_odd + s_even)

print('value using simpsons 1/3 rule = ', I2)


