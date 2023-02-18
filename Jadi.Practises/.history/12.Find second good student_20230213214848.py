list_number=[]
list_score=[]
student_number=input("Enter Student number:")
score=input('Enter score of student:')
if student_number !="p":
    student_number=input("Enter Student number(if you like to end that please type p here):")
    score=input('Enter score of student:')
    list_number.append(student_number)
    list_score.append(score)
elif student_number=="p":
    break
print(list_number)