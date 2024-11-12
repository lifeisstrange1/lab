
# write a python program to use bisection method and find root of a function 


import numpy as np

a = float(input("enter the first guess : "))
b = float(input("enter the second guess : "))
e = float(input("enter the permissible error : "))

def f(x):
    return  x + np.exp(-x**2)*np.cos(x)
    
       
def bisect(a,b,e):
    i = 1
    x = 0
    condition = True
    while condition:
          g = f(x)
          x = (a+b)/2
          if f(x)<0:
             a = x
          else:
             b = x
             
          print("for iteration : ", i, "value of x: ",x, "value of f(x): ", f(x))
          i = i+1
          condition = abs(b-a)>e
          
    print("required root is :", x)
          


if f(a)*f(b)>0:
   print("given values do not bracket the root")
   print("guess the values again")
   
else: 
   bisect(a,b,e)
      
                 
      	       
      	            
      	       
      	       
      		
