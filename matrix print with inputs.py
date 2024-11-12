# write a python program to print a matrix taking no. of rows and columns as input from the user, and elements also as input from the user row-wise


R = int(input("Enter the number of rows : "))
C = int(input("Enter the number of columns : "))

matrix = []

print("Enter the entries row-wise : ")

for i in range(R):		
	a =[]
	for j in range(C):	 
		a.append(int(input()))
	matrix.append(a)


for i in matrix:
    print(i)

