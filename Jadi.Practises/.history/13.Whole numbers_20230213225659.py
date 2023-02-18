number=int(input("Enter a number:"))
list1=[]
x=0
for i in range(2,(number/2)+1):
    if number%i ==0:
        list1.append(i)
    else:
        pass
for i in list1:
    x=x+i
if x ==number:
    print("That number is a Whole number.")

