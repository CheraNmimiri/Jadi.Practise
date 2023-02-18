count=int(input("Enter number of employee:"))
while x < count:
    id=input("Enter id of employee:")
    hw=float(input("Enter how many work that employee:"))
    pph=int(input("Enter price per hour for that employee:"))
    if hw <= 40:
        salary=pph*hw
        print("Salary is equal %d for %d hours and without overtime.")
    elif hw > 40:
        overtime=hw-40
        ovp=(1.5*pph)*overtime
        salary=
