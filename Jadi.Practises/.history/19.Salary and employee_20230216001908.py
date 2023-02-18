id=int(input("Enter employee number:"))
h_work=int(input("Enter hours work employee:"))
salary_per_hour=int(input("Enter salary per hour:"))
total_salary=salary_per_hour*h_work
if h_work > 40:
    salary_per_hour_new=h_work*(salary_per_hour*1.5)
    print("id %d Total salary with over time = %d" % (id,total_salary_new))
elif h_work <=40:
 print("id %d Total salary without overtime = %d" % (id,total_salary))
