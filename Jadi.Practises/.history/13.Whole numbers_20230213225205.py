number=int(input("Enter a number:"))
list1=[]
for i in range(2,(number/2)+1):
    if i % number ==0:
        list1.append(i)