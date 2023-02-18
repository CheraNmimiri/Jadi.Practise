salary=float(input("Enter salary of employee:"))
insurance=salary*0.07
tax=salary*0.01
last_salary=salary-insurance-tax
print("Salary of employee is %.0f and price of insurance is %.0f and price of tax is %.0f.so next that salary equal:%.0f" % (salary,insurance,tax,last_salary))