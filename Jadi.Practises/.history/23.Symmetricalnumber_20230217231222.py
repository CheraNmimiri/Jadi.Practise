number=input("Enter a number:")
list1=[]
list2=[]
if len(number)%2==0:
    for i in range(0,(len(number)/2)-1):
        list1.append(number[i])
    for i in range((len(number)/2),(len(number)-1)):
        list2.append(number[i])
    list2.reverse()
    