list_number=[]
list_score=[]
global student_number
while student_number==0:
    global student_number
    student_number=input("Enter Student number:")
    global score
    score=input('Enter score of student:')
    list_number.append(student_number)
    list_score.append(score)
print(list_number) 