def whole(number):
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
        print("%d is a Whole number." % (number))
    else:
        print("%d isn't whole number. " % (number))
    x=input("If you like to continue enter Y and other enter N:")
    if x=='y' or x=='Y':
        whole()
    elif x=='n' or x=='Y':
    



