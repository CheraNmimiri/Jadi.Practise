list1=[]
x=1
y=1
while x*y!=0:
    x=int(input("Enter first number:"))
    y=int(input("Enter second number:"))
    for i in range(y+1):
        i=x
        list1.append(i)
    for j in list1:
        j=j+x
    print(j)
