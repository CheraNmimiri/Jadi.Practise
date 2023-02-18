from math import floor
number=input("Enter a number:")
list1=[]
list2=[]
if len(number)%2==0:
    for i in range(0,(len(number)/2)-1):
        list1.append(number[i])
    for i in range((len(number)/2),(len(number)-1)):
        list2.append(number[i])
    list2.reverse()
    if list1==list2:
        print("%d is symmetrical." % (number))
    else:
        print("%d is not symmetrical. % (number)")
    
elif len(number)%2==1:
    for i in range(0,(floor(len(number)/2))-1):
        list1.append(number[i])
    for i in range((floor(len(number)/2)+1),(len(number)-1)):
        list2.append(number[i])
    list2.reverse()
    print("%d is not symmetrical.")
    
    