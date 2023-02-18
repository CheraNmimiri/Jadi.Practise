id=int(input("Enter employee number:"))
h_work=int(input("Enter hours work employee:"))
salary_per_hour=int(input("Enter salary per hour:"))
total_salary=salary_per_hour*h_work
if h_work > 40:
    overtime=h_work-40
    ovts=overtime*salary_per_hour
    print(total_salary)
