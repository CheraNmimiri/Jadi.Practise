number=int(input("Enter a number:"))
list1=[]
for i in range(2,(number/2)+1):
    if number%i ==0:
        list1.append(i)
    else:
        pass
for i in list1:
    x=x+i
