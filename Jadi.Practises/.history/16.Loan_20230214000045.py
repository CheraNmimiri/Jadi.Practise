month=int(input("Enter intended month:"))
r_amount=int(input("Enter required amount of money customer need:"))
interest_rate=float(input("Enter interest rate of that:"))
last_money=(r_amount*12)/(12-(month*(interest_rate/100)))
month_pay=last_money/month
print("Amount of money back should be pay is %f and every month customer must pay %f." % (last_money,month_pay)
