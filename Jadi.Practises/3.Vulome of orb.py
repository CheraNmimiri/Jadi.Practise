from math import pi
def volume_orb():
    global radius
    radius=float(input("Enter radius:"))
    return (4/3)*(pi*(radius**3))
def area_orb():
    return float(4*(pi*(radius**2)))

print(f"Volume of orb is :{volume_orb():.2f}")
print(f"Area of orb is :{area_orb():.2f}")