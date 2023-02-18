from math import pi
radius=float(input("Enter radius:"))
height=float(input("Enter height:"))
def area():
    return (2*(pi*(radius**2))+(2*pi*radius)*height)
def volume():
    return (pi*(radius**2))*height
print(f"Area is : {area():.2f}")
print(f"Volume is : {volume():.2f}")