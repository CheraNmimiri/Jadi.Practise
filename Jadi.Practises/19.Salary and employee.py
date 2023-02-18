count=int(input("Enter number of employee:"))
x=0
while x < count:
    id=input("Enter id of employee:")
    hw=float(input("Enter how many work that employee:"))
    pph=int(input("Enter price per hour for that employee:"))
    if hw <= 40:
        salary=pph*hw
        print("Salary is equal %d for %d hours and without overtime." % (salary,hw))
    elif hw > 40:
        overtime=hw-40
        ovp=(1.5*pph)*overtime
        salary=(40*pph)
        tsalary=salary+ovp
        print("Salary for 40h equal %d and for %d equal %d and total salary is %d " % (salary,overtime,ovp,tsalary))
    x+=1    

