

rows = int(input("enter no. of rows: "))

if rows <= 0 :
	print('no. of rows should be greater than zero')
	
else :
	for i in range (1, rows+1):
	    print(str(1)*i)
