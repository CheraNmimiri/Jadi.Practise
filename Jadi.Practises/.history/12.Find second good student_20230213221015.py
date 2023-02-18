list_number=[]
list_score=[]
student_number=0
score=0
while student_number !="p":
    student_number=input("Enter Student number(if you like to end that please type p here):")
    score=input('Enter score of student:(if you like to end that please type p here)')
    if student_number != "p":
        pass
    
    list_number.append(student_number)
    list_score.append(score)
list_number.remove("p")
print(list_number)