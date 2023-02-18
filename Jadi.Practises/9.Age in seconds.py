from math import pow
age=int(input("Enter your age:"))
one_years=3.156*pow(10,7)
age_in_seconds=one_years*age
print(f"Your age in seconds is : {age_in_seconds:.0f}")
