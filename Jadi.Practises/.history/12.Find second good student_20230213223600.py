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
high_score=max(list_score)

list_score.remove(high_score)
second_high_score=max(list_score)
number=list_score.index(second_high_score)
second_high_score_number=list_number[q]
print("Second high score student is %s with score %d." %(second_high_score_number,second_high_score))

