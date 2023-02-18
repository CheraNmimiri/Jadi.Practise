fn,sn,tn=map(int,(input("Enter three number:").split()))
list1=[fn,sn,tn]
list1.sort()

for i in list1:
    print(i,end=" ")


