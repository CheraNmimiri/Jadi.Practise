list_number=[]
list_score=[]
x=int(input("How much you have student?"))
y=0
while y<x:
    student_number=input("Enter Student number:")
    score=int(input('Enter score of student:'))
    list_number.append(student_number)
    list_score.append(score)
    y+=1
hs=max(list_score)
ihs=list_score.index(hs)
list_score.remove(hs)
list_number.remove(list_number[ihs])
shs=max(list_score)
nshs=list_score.index(shs)
shsn=list_number[nshs]
print("Second high score student is %s with score %d." %(shsn,shs))
#hs=high score,   ihs=index high score   ,   shs=second high score     ,    nhss=number high score 

