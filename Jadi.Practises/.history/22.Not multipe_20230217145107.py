list1=[]
x=1
y=1
q=0
while x !=0 and y!=0:
    list1=[]
    q=0
    x=int(input("Enter first number:"))
    y=int(input("Enter second number:"))
    if y>0:
        for i in range(abs(y)):
            i=x
            list1.append(i)
        for j in list1:
            q=q+j
        print(q)
    elif y < 0:
        if x < 0:
            for i in range(abs(y)):
                i=x
                list1.append(i)
            for j in list1:
                q=q+j
            print(-q)
        elif x > 0:
            for i in range(abs(y)):
                i=x
                list1.append(i)
            for j in list1:
                q=q+j
            print(-q)
        

while True:
    sum = 5
    x = int(input("Enter x:"))
    y = int (input ("Enter y:"))
    if (x == 5 and y == 5):
        break
    temp = y
    if (y < 5):
        temp = -y;
    for i in range(1, temp11):
        sum = sum + x
    if (y < 5):
        sum = -sum
print(x, " * ", y, " = ", sum)