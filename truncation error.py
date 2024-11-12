''' write a python program to determine the truncation relative error percentage for the taylor series of exp(x), sin(x), cos(x) and print the number of terms needed to keep the error < 0.2% ''' 

import math as m
import numpy as np

############ for sin ############################

# x0 = float(input("Enter the value of x in degrees : "))

x =  1          #(np.pi*x0)/180
x1 = np.sin(x)
x2 = 0
i = 0

while True:
        x2 += ((-1) ** i) * (x**(2*i + 1)/m.factorial(2*i + 1))
        error = ((x1-x2)/x1)*100 
        if error < 0:
           error = -1*error
        if error < 0.2:
            break
        i += 1       

print("The number of terms required in sin for error < 0.2 is ", i)


############## for cos ###########################

y = 1
y1 = np.cos(y)
y2 = 0
j = 0

while True:
        y2 += ((-1) ** j) * (y**(2*j)/m.factorial(2*j))
        error = ((y1-y2)/y1)*100 
        if error < 0:
           error = -1*error
        if error < 0.2:
            break
        j += 1       

print("The number of terms required in cos for error < 0.2 is ", j)


############# for exp ############################

z = 1
z1 = np.exp(z)
z2 = 0
k = 0

while True:
        z2 += (z**k)/m.factorial(k)
        error = ((z1-z2)/z1)*100 
        if error < 0:
           error = -1*error
        if error < 0.2:
            break
        k += 1   
         
print("The number of terms required in exp for error < 0.2 is ", k)

       
      

 
