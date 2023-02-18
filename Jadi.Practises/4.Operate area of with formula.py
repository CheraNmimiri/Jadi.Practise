from math import tan,pi
amount_of_sides=float(input("Enter the amount of sides : "))
length_of_side=float(input("Enter the length : "))
formula=(amount_of_sides*(length_of_side**2))/(4+tan(pi/amount_of_sides))
print("Answer is %.2f" % formula)