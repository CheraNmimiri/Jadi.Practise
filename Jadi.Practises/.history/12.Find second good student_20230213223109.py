list_number=[]
list_score=[]
x=int(input("How much you have student?"))
y=0
while y<x:
    student_number=input("Enter Student number:")
    score=input('Enter score of student:')
    list_number.append(student_number)
    list_score.append(score)
    y+=1
high_score=max(list_score)
list_score.remove(high_score)
second_high_score=max(list_score)
q=index(second_high_score)
second_high_score_
print("Second high score student is %d with score %d." %())

