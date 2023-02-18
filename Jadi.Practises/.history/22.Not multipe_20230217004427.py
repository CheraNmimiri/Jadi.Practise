list1=[]
x=1
y=1
q=0
while x*y!=0:
    list1=[]
    q=0
    if y>0:
        x=int(input("Enter first number:"))
        y=int(input("Enter second number:"))
        for i in range(abs(y)):
            i=x
            list1.append(i)
        for j in list1:
            q=q+j
        print(q)
    elif y < 0:
        if x > 0:
            x=int(input("Enter first number:"))
            y=int(input("Enter second number:"))
            for i in range(abs(y)):
                i=x
                list1.append(i)
            for j in list1:
                q=q+j
            print(-q)
        elif x > 0:
             x=int(input("Enter first number:"))
             y=int(input("Enter second number:"))
            for i in range(abs(y)):
                i=x
                list1.append(i)
            for j in list1:
                q=q+j
            print(q)
        

