id=int(input("Enter employee number:"))
h_work=int(input("Enter hours work employee:"))
salary_per_hour=int(input("Enter salary per hour:"))
total_salary=salary_per_hour*h_work
if h_work > 40:
    overtime=h_work-40
    ovts=overtime*salary_per_hour*3)
    total_salary_new=total_salary*ovts
    print("id %d Total salary with over time = %d" % (id,total_salary))
elif h_work <=40:
 print("id %d Total salary without overtime = %d" % (id,total_salary))
