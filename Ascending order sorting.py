
# write a python program to sort a list in ascending order 


list = [27, 34, 10, 33, 17, 78, 65,13,98,3,16]

for i in range(len(list)):
    for j in range(len(list)):
        if list[i] < list[j]:
           list[i], list[j] = list[j], list[i]

           
print(list)



